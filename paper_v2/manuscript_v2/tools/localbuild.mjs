// Local build harness: runs the Emscripten pdfTeX (from the texlive.js project) inside Node.
// Usage: node localbuild.mjs <document-dir> <main-file>
// The document dir is copied into the engine's MEMFS, then pdfTeX is run on <main-file>.
import fs from 'fs';
import path from 'path';
import vm from 'vm';
const ROOT = process.env.TEXLIVE_JS || '/tmp/tljs/texlive.js-master';
const DOC = process.argv[2], MAIN = process.argv[3] || 'main.tex';
const ctx = { console: { log(){}, warn(){}, error(...a){ console.log('ERR', ...a); } }, setTimeout, clearTimeout,
  setInterval, clearInterval, process, Buffer, Uint8Array, Int8Array, ArrayBuffer, DataView, Promise,
  Math, Date, JSON, Error, TypeError, RangeError, performance: { now: () => Date.now() } };
ctx.global = ctx; ctx.self = ctx; ctx.window = undefined;
ctx.navigator = { userAgent: 'node', hardwareConcurrency: 2, platform: 'linux' };
const MSG = [];
ctx.postMessage = (m) => MSG.push(JSON.parse(m));
ctx.XMLHttpRequest = class { open(){} set responseType(t){} send(){} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(ROOT + '/pdftex-worker.js', 'latin1'), ctx, { filename: 'pdftex-worker.js' });
const msg = (command, args) => ctx.self.onmessage({ data: JSON.stringify({ command, arguments: args, msg_id: 1 }) });
let nf = 0;
(function walk(rel) {
  const abs = ROOT + '/texlive' + rel;
  for (const e of fs.readdirSync(abs, { withFileTypes: true })) {
    const r = rel + '/' + e.name;
    if (e.isDirectory()) { msg('FS_createPath', ['/', r.slice(1), true, true]); walk(r); }
    else { const i = r.lastIndexOf('/'); msg('FS_createDataFile', [i ? r.slice(0, i) : '/', r.slice(i + 1), fs.readFileSync(ROOT + '/texlive' + r, 'latin1'), true, true]); nf++; }
  }
})('');
(function walkDoc(dir, rel) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const r = rel ? rel + '/' + e.name : e.name;
    if (e.isDirectory()) { msg('FS_createPath', ['/', r, true, true]); walkDoc(path.join(dir, e.name), r); }
    else { const i = r.lastIndexOf('/'); msg('FS_createDataFile', [i ? '/' + r.slice(0, i) : '/', e.name, fs.readFileSync(path.join(dir, e.name), 'latin1'), true, true]); nf++; }
  }
})(DOC, '');
console.log('MEMFS: texlive files +', nf - 3475, 'document files');
try { ctx.self.onmessage({ data: JSON.stringify({ command: 'run', arguments: ['-interaction=nonstopmode', '-output-format', 'pdf', MAIN], msg_id: 9 }) }); }
catch (e) { console.log('run threw', String(e).slice(0, 300)); }
const out = MSG.filter(m => m.command === 'stdout').map(m => m.contents).join('\n');
const err = MSG.filter(m => m.command === 'stderr').map(m => m.contents).join('\n');
fs.writeFileSync('/tmp/lastbuild.log', out + '\n=== stderr ===\n' + err);
const errs = out.split('\n').filter(l => /^!|not found|Undefined control|Emergency|Fatal/.test(l)).slice(0, 12);
console.log('--- first errors ---'); console.log(errs.join('\n') || '(none)');
msg('FS_readFile', ['/output.pdf']);
let pdf = MSG.filter(m => m.command === 'result').pop();
if (!pdf || !pdf.result || !pdf.result.startsWith('%PDF')) { msg('FS_readFile', ['/' + MAIN.replace('.tex', '.pdf')]); pdf = MSG.filter(m => m.command === 'result').pop(); }
if (pdf && pdf.result && pdf.result.startsWith('%PDF')) {
  fs.writeFileSync('/tmp/localbuild.pdf', Buffer.from(pdf.result, 'latin1'));
  console.log('PDF written /tmp/localbuild.pdf', fs.statSync('/tmp/localbuild.pdf').size, 'bytes');
} else console.log('no PDF; log at /tmp/lastbuild.log');
