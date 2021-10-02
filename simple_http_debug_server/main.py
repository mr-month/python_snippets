import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class RequestHandler(BaseHTTPRequestHandler):
    def _handle_request(self):
        self.send_response(200)
        self.end_headers()

        payload = json.dumps({
                "method": self.command,
                "path": self.path,
                "requestline": self.requestline,
                "client_address": self.client_address,
                "headers": {header: value for header, value in self.headers.items()},
            },
            indent=4,
        )

        self.wfile.write(bytes(payload, "utf-8"))

    def do_GET(self):
        self._handle_request()

    def do_HEAD(self):
        self._handle_request()

    def do_POST(self):
        self._handle_request()

    def do_PUT(self):
        self._handle_request()

    def do_DELETE(self):
        self._handle_request()

    def do_CONNECT(self):
        self._handle_request()

    def do_OPTIONS(self):
        self._handle_request()

    def do_TRACE(self):
        self._handle_request()

    def do_PATCH(self):
        self._handle_request()


httpd = HTTPServer(('0.0.0.0', int(os.environ.get("HTTP_DEBUGGER_PORT", 5000))), RequestHandler)
httpd.serve_forever()

