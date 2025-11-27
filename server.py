import http.server
import socketserver
import webbrowser
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Change directory to where script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving Chess App at http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        # Automatically open the browser
        webbrowser.open(f"http://localhost:{PORT}/chess.html")
        httpd.serve_forever()
except OSError:
    print(f"Port {PORT} is busy. Try closing other servers or wait a moment.")