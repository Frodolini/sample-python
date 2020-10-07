import os
import http.server
import socketserver

from http import HTTPStatus

a = "Frodolini"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = a, 'Hei på deg fremmede paa internettet! Du førespurde %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
