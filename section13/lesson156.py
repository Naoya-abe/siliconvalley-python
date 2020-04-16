# socketserverとhttp.serverとwebbrowser

import http.server
import socketserver

# withステートメントでhostとportを指定してserverを立ち上げる  リクエストを処理するためのhandlerを指定
with socketserver.TCPServer(('127.0.0.1', 8000), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
