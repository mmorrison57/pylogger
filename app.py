#!/usr/bin/env python3
"""
Simple WSGI app that logs messages to both stdout and stderr, then serves an HTML page.
"""

import sys
from wsgiref.simple_server import make_server

def dual_log(level: str, message: str) -> None:
    """
    Log a message to both stdout and stderr, with the level at the very start.
    """
    line = f"{level} {message}\n"
    # write to stdout
    sys.stdout.write(line)
    # write to stderr
    sys.stderr.write(line)

def application(environ, start_response):
    # Log on each request
    dual_log('DEBUG', 'Starting page render.')
    dual_log('INFO',  'Page viewed: Welcome page loaded.')
    dual_log('WARN',  'Just a sample warning.')
    dual_log('ERROR', 'Sample error occurred.')

    # HTML response
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Python Logger Demo</title>
  <style>
    body { font-family: sans-serif; margin: 2rem; }
    h1 { color: #0078D4; }
    p { font-size: 1.1rem; }
  </style>
</head>
<body>
  <h1>✅ Python Logger Demo</h1>
  <p>This page is live! Check your console or Azure “Log stream” to see DEBUG, INFO, WARN, and ERROR entries.</p>
  <button onclick="location.reload()">Reload &amp; Log Again</button>
</body>
</html>
"""
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [html.encode('utf-8')]

app = application

if __name__ == '__main__':
    port = 8000
    print(f"Starting server on http://localhost:{port}/", file=sys.stderr)
    with make_server('', port, application) as httpd:
        httpd.serve_forever()

