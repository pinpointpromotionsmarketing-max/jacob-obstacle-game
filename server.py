#!/usr/bin/env python3
import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🎮 Jacob's Obstacle Game running at: http://localhost:{PORT}")
    print(f"Share this link with Jacob: http://localhost:{PORT}")
    httpd.serve_forever()
