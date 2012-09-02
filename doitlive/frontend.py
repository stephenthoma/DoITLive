import time
import BaseHTTPServer


HOST_NAME = 'localhost'
PORT_NUMBER = 80


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(s):
        s.send_response(200)
        if s.path.endswith('.css'):
            s.send_header("Content-type", "text/css")
        elif s.path.endswith('.html'):
            s.send_header("Content-type", "text/html")
        s.end_headers()
        
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        f = open('../bootstrap/index.html')
        x = f.read()
        s.wfile.write(x)


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - {0}:{1}".format(HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - {0}:{1}".format(HOST_NAME, PORT_NUMBER)