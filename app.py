from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.path[1:].encode())
        self.wfile.write(b'\n')
        self.wfile.write(b'Hello World!')

def main():
    httpd = HTTPServer(('localhost', 8080), RequestHandler)
    print('Serving HTTP on port 8080...')
    httpd.serve_forever()

if __name__ == '__main__':
    main()