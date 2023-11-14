from http.server import BaseHTTPRequestHandler, HTTPServer
from textwrap import dedent

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(dedent("""
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    * { font-family: sans-serif; }
                </style>"""+("""
                <script>
                    function sendData(){
                        fetch("/receive-data", {method:"post", body: JSON.stringify({some: "data"})});
                    }
                </script>""" if "button" in self.path else "") + """
            </head>
            <body>
                hello :)"""+(
                    "<br /> <br /> i've seen you before :)" if self.headers.get("cookie") else ""
                )+("""
                <br /><br />
                <button onclick="sendData()">Send Data via POST request</button>""" if "button" in self.path else "") +
            """</body>
        </html>""").strip().encode("utf-8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Set-Cookie", "trackthisperson=wherevertheygo")
        self.end_headers()
        self.wfile.write(b"thanks :)")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
