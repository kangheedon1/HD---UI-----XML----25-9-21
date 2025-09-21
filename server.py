#!/usr/bin/env python3
"""
Simple HTTP server to serve the BAS 29.3.1 Generator UI
"""

import http.server
import socketserver
import json
import urllib.parse
from bas_generator import BAS291Generator
import os

class BASServerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='/home/runner/work/HD---UI-----XML----25-9-21/HD---UI-----XML----25-9-21', **kwargs)
        self.generator = BAS291Generator()
    
    def do_POST(self):
        if self.path == '/generate':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                config = json.loads(post_data.decode('utf-8'))
                xml_output = self.generator.generate_bas_config(config)
                
                response = {
                    'success': True,
                    'xml': xml_output,
                    'message': 'XML generated successfully'
                }
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                response = {
                    'success': False,
                    'error': str(e),
                    'message': 'Error generating XML'
                }
                
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def start_server(port=8000):
    with socketserver.TCPServer(("", port), BASServerHandler) as httpd:
        print(f"🚀 HD BAS 29.3.1 Generator Server starting on port {port}")
        print(f"📱 Open your browser and go to: http://localhost:{port}")
        print("🔧 Generator ready for BAS configuration creation")
        print("=" * 60)
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()