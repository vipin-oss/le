#!/usr/bin/env python3
"""serve_share.py - static file server for the submission/download artefacts, with byte-range support.

Why this exists: the built zips live in PAPER_PROJECT/packages/ (gitignored, generated on demand) and the
user downloads them through the sandbox preview proxy. `python3 -m http.server` is not enough for a 59 MB
file because it ignores the Range header, so a browser that restarts or resumes a download gets a 200 from
byte 0 again. This handler answers Range with 206 + Content-Range and keeps Last-Modified truthful (it is
taken from the file, not from the request time, otherwise a resumable client sees the entity change under it).

Usage
    python3 tools/serve_share.py [--root DIR] [--port N]      default root: /home/user/share, port 8099
    The root should contain symlinks (or copies) of the files to publish. Bind is 0.0.0.0.
"""
import argparse
import os
import socketserver
from http.server import SimpleHTTPRequestHandler


class RangeHandler(SimpleHTTPRequestHandler):
    # ---- truthful mtime for the directory listing -------------------------------------------
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path) and 'Range' in self.headers:
            start, end = self._parse_range(self.headers['Range'], os.path.getsize(path))
            if start is None:
                self.send_error(416, 'Range not satisfiable')
                return None
            f = open(path, 'rb')
            f.seek(start)
            length = end - start + 1
            self.send_response(206)
            self.send_header('Content-Type', self.guess_type(path))
            self.send_header('Content-Length', str(length))
            self.send_header('Content-Range', f'bytes {start}-{end}/{os.path.getsize(path)}')
            self.send_header('Last-Modified', self.date_time_string(os.stat(path).st_mtime))
            self.end_headers()
            if length < 1024 * 1024:
                self.wfile.write(f.read(length))
                f.close()
                return None
            self.copyfile_chunked(f, length)
            return None
        return SimpleHTTPRequestHandler.send_head(self)

    def copyfile_chunked(self, source, remaining):
        while remaining > 0:
            chunk = source.read(min(64 * 1024, remaining))
            if not chunk:
                break
            try:
                self.wfile.write(chunk)
            except (BrokenPipeError, ConnectionResetError):
                break
            remaining -= len(chunk)
        source.close()

    @staticmethod
    def _parse_range(hdr, size):
        try:
            unit, _, spec = hdr.partition('=')
            if unit.strip().lower() != 'bytes':
                return None, None
            first = spec.split(',')[0].strip()
            if first.startswith('-'):
                n = int(first[1:])
                return max(0, size - n), size - 1
            a, _, b = first.partition('-')
            start = int(a)
            end = int(b) if b else size - 1
            if start >= size or end < start:
                return None, None
            return start, min(end, size - 1)
        except Exception:
            return None, None

    # ---- listing keeps the real mtimes (SimpleHTTPRequestHandler uses them already) ---------
    def list_directory(self, path):
        entries = sorted(os.listdir(path))
        body = ['<!DOCTYPE html><meta charset="utf-8"><title>submission artefacts</title>',
                '<h1>Submission artefacts</h1><ul>']
        for name in entries:
            fp = os.path.join(path, name)
            if os.path.isdir(fp):
                continue
            real = os.path.realpath(fp)
            size = os.path.getsize(real)
            body.append(f'<li><a href="/{name}">{name}</a> &nbsp; {size:,} bytes</li>')
        body.append('</ul>')
        data = '\n'.join(body).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)
        return None

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        SimpleHTTPRequestHandler.end_headers(self)


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='/home/user/share')
    ap.add_argument('--port', type=int, default=8099)
    a = ap.parse_args()
    os.makedirs(a.root, exist_ok=True)
    os.chdir(a.root)
    # the handler resolves paths against the process cwd; symlinks are followed by translate_path
    print(f'serving {a.root} on 0.0.0.0:{a.port} (range-capable)')
    with Server(('0.0.0.0', a.port), RangeHandler) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    main()
