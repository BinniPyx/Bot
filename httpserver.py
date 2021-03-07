from http.server import BaseHTTPRequestHandler, HTTPServer
class HandleRequests(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self._set_headers()
        self.wfile.write("received get request")
HTTPServer(("localhost",80), HandleRequests).serve_forever()
 	