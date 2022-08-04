#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
from sys import argv
import argparse


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        if len(argv) > 1:
            try:
                output = open(f"{argv[1]}", "wb")
            except:
                print("Error opening file")
        content_length = int(
            self.headers["Content-Length"]
        )  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)
        if args.f != None:
            try:
                output = open(f"{argv[1]}", "wb")
            except:
                print("Error opening file")
                exit(1)
            try:
                output_data = base64.b64decode(post_data)
                output.write(output_data)  # <--- Gets the data itself
            except:
                print("Error decoding data from base64")
                exit(1)
        else:
            try:
                output_data = base64.b64decode(post_data)
                print("")
                print(output_data.decode())  # <--- Gets the data itself
                print("")
            except:
                print("Error decoding data from base64")
                exit(1)

        print("File received successfully")

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode("utf-8"))
        exit(1)


def run(server_class=HTTPServer, handler_class=S):
    server_address = ("", args.p)
    httpd = server_class(server_address, handler_class)
    print("Listening for connections\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="PowerShell Web Beacon")
    parser.add_argument(
        "-f",
        type=str,
        help="file to save output to, default is stdout",
        default=None,
    )
    parser.add_argument(
        "-p",
        type=int,
        help="port for the server to listen at, default is 8000",
        default=8000,
    )
    args = parser.parse_args()

    port = args.p
    run()
    print(f"listening on port {port}")
