import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # just send back the same data, but upper-cased
        msg = []
        msg.append("<html> lang=\"en\"")
        msg.append("    <head>")
        msg.append("        <title>404 Not Found</title>")
        msg.append("    </head>")
        msg.append("    <body>")
        msg.append("        <h1>404 Not Found</h1>")
        msg.append("        <p>The server did not find the file requested.</p>")
        msg.append("        <hr>")
        msg.append("        <center>")
        msg.append("            <p>pyServe 0.0.1</p>")
        msg.append("        </center>")
        msg.append("    </body>")
        msg.append("</html>")

        msg_raw = ''.join(f'{v}\r\n' for v in msg)

        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(msg_raw),
            'Connection': 'close',
        }

        response_headers_raw = ''.join(f'{k}: {v}\r\n' for k, v in response_headers.items())

        resp = "HTTP/1.1 404 Not Found\r\n"+response_headers_raw+"\r\n"+msg_raw
        resp_bytes = bytes(resp, "utf-8")
        print(resp_bytes)
        self.request.sendall(resp_bytes)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    print(f"Running server om {HOST}:{PORT}")
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
