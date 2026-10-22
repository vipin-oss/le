#!/usr/bin/env node
/* Deterministic, vector-preserving SVG -> PDF conversion for manuscript figures.
 * Usage: node render_svg_pdf.js [source-dir] [output-dir]
 * Requires the pinned dependencies in package-lock.json and a font with Unicode
 * glyph coverage. This creates one single-page PDF per SVG.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const PDFDocument = require('pdfkit');
const SVGtoPDF = require('svg-to-pdfkit');

const root = path.resolve(__dirname, '..');
const sourceDir = path.resolve(process.argv[2] || path.join(root, 'master/figures/source'));
const outputDir = path.resolve(process.argv[3] || sourceDir);
const fontDir = '/usr/share/fonts/truetype/dejavu';
const fontFiles = {
  DejaVuSans: path.join(fontDir, 'DejaVuSans.ttf'),
  'DejaVuSans-Bold': path.join(fontDir, 'DejaVuSans-Bold.ttf'),
  'DejaVuSans-Oblique': path.join(fontDir, 'DejaVuSans.ttf'),
  'DejaVuSans-BoldOblique': path.join(fontDir, 'DejaVuSans-Bold.ttf'),
};

function dimensions(svg, file) {
  const match = svg.match(/viewBox\s*=\s*["']\s*(-?[\d.]+)[ ,]+(-?[\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)\s*["']/i);
  if (!match) throw new Error(`${file}: missing finite positive viewBox`);
  const width = Number(match[3]);
  const height = Number(match[4]);
  if (!(width > 0 && height > 0 && Number.isFinite(width) && Number.isFinite(height))) {
    throw new Error(`${file}: invalid viewBox dimensions`);
  }
  // SVG CSS pixels are 1/96 inch; PDF points are 1/72 inch.
  return {width: width * 0.75, height: height * 0.75};
}

function convert(file) {
  const svg = fs.readFileSync(file, 'utf8');
  const {width, height} = dimensions(svg, file);
  const output = path.join(outputDir, `${path.basename(file, '.svg')}.pdf`);
  const doc = new PDFDocument({autoFirstPage: false, compress: true, pdfVersion: '1.7'});
  doc.registerFont('DejaVuSans', fontFiles.DejaVuSans);
  doc.registerFont('DejaVuSans-Bold', fontFiles['DejaVuSans-Bold']);
  doc.registerFont('DejaVuSans-Oblique', fontFiles['DejaVuSans-Oblique']);
  doc.registerFont('DejaVuSans-BoldOblique', fontFiles['DejaVuSans-BoldOblique']);
  doc.addPage({size: [width, height], margin: 0});
  const outputStream = fs.createWriteStream(output);
  const warnings = [];
  doc.pipe(outputStream);
  SVGtoPDF(doc, svg, 0, 0, {
    width,
    height,
    preserveAspectRatio: 'xMidYMid meet',
    fontCallback: (family, bold, italic) => {
      if (/dejavu/i.test(family)) {
        return bold ? (italic ? 'DejaVuSans-BoldOblique' : 'DejaVuSans-Bold')
                    : (italic ? 'DejaVuSans-Oblique' : 'DejaVuSans');
      }
      return bold ? 'DejaVuSans-Bold' : 'DejaVuSans';
    },
    warningCallback: message => warnings.push(String(message)),
  });
  doc.end();
  return new Promise((resolve, reject) => {
    outputStream.on('finish', () => {
      const bytes = fs.statSync(output).size;
      if (bytes < 1000) return reject(new Error(`${output}: unexpectedly small PDF (${bytes} bytes)`));
      if (warnings.length) {
        for (const warning of warnings) console.error(`WARN ${path.basename(file)}: ${warning}`);
      }
      console.log(`${path.basename(file)} -> ${path.basename(output)} (${bytes} bytes; ${warnings.length} SVG warnings)`);
      resolve({file, output, bytes, warnings});
    });
    outputStream.on('error', reject);
  });
}

(async () => {
  if (!fs.existsSync(fontFiles.DejaVuSans)) throw new Error(`Unicode font not found: ${fontFiles.DejaVuSans}`);
  if (!fs.existsSync(sourceDir)) throw new Error(`SVG source directory not found: ${sourceDir}`);
  fs.mkdirSync(outputDir, {recursive: true});
  const files = fs.readdirSync(sourceDir).filter(name => name.toLowerCase().endsWith('.svg')).sort();
  if (!files.length) throw new Error(`No SVG files found in ${sourceDir}`);
  const results = [];
  for (const name of files) results.push(await convert(path.join(sourceDir, name)));
  console.log(`Converted ${results.length} SVG figures to vector PDF in ${outputDir}`);
  if (results.some(result => result.warnings.length)) process.exitCode = 2;
})().catch(error => { console.error(error.stack || error); process.exit(1); });
