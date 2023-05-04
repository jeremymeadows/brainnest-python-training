# http server

import http.server
import socketserver

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler
http = socketserver.TCPServer(('127.0.0.1', PORT), handler)

print('serving at port', PORT)
http.serve_forever()
