from http.server import HTTPServer, BaseHTTPRequestHandler;
from io import BytesIO;
from urllib.parse import urlparse;
from urllib.parse import parse_qs;
from urllib.request import urlopen;
from urllib.request import URLError, HTTPError;

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200);
        self.end_headers();
        r = None;
        try:
            r = urlopen('https://graph.microsoft.com/v1.0/me/');
        except (HTTPError, URLError, Exception) as error:
            print(error.__str__());
        print(r);
        tpl = urlparse(self.path);
        dic = parse_qs(tpl.query);
        self.wfile.write(b'Hello, ' + (dic['azureid'][0]).encode('ascii'));

    def do_POST(self):
        content_length = int(self.headers['Content-Length']);
        body = self.rfile.read(content_length);
        self.send_response(200);
        self.end_headers();
        response = BytesIO();
        response.write(b'This is POST request. ');
        response.write(b'Received: ');
        response.write(body);
        self.wfile.write(response.getvalue());


httpd = HTTPServer(('localhost', 8081), SimpleHTTPRequestHandler);
print("Starting server");
httpd.serve_forever();