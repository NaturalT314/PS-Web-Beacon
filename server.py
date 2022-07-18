#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
from sys import argv

from requests import post


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        try:
            output = open(f"{argv[1]}", "wb")
        except:
            print("Error opening file")
        content_length = int(
            self.headers["Content-Length"]
        )  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)
        try:
            output_data = base64.b64decode(post_data)
            output.write(output_data)  # <--- Gets the data itself
        except:
            print("Error decoding data from base64")

        print("File received successfully")

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode("utf-8"))
        exit(1)


def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Listening for connections\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == "__main__":

    if len(argv) < 2:
        print(
            """Usage::
    ./server.py [<output-file>] [<port>]
    ./server.py [<output-file>]
    """
        )
        exit(1)
        port = int(argv[1])
        run(port)
        print(f"listening on port {port}")
    else:
        port = 8000
        print(f"listening on port {port}")
        run()
