import sqlite3
import string
import random
import threading
import atexit
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleRedirectHandler(BaseHTTPRequestHandler):
    def __init__(self, url_shortener_instance, *args, **kwargs):
        self.url_shortener = url_shortener_instance
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        # Extract the short code from the path
        short_code = self.path.lstrip('/')
        
        # Handle empty path (homepage)
        if not short_code:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
            <html><body>
            <h1>Corefinder URL Shortener</h1>
            <p>Server is running!</p>
            </body></html>
            ''')
            return
        
        # Look up the original URL
        original_url = self.url_shortener.get_original_url(short_code)
        
        if original_url:
            self.send_response(302)
            self.send_header('Location', original_url)
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<html><body><h1>404 Not Found</h1><p>Short code "{short_code}" not found.</p></body></html>'.encode())
    
    def log_message(self, format, *args):
        # Suppress all server logs to keep terminal clean
        pass

class URLShortener:
    def __init__(self, db_name='url_shortener.db', host='localhost', port=8080, display_host='cf.link'):
        self.db_name = db_name
        self.host = host
        self.port = port
        self.display_host = display_host
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.server = None
        self.server_thread = None
        self.create_table()
        self._start_server()
        atexit.register(self._stop_server)

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY,
                    original_url TEXT NOT NULL,
                    short_code TEXT NOT NULL UNIQUE
                )
            ''')

    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choice(characters) for _ in range(length))
            if not self.get_original_url(short_code):
                return short_code

    def get_original_url(self, short_code):
        # Use a new connection for thread safety
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT original_url FROM urls WHERE short_code=?
        ''', (short_code,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def _start_server(self):
        """Start the redirect server in background"""
        def run_server():
            handler = lambda *args, **kwargs: SimpleRedirectHandler(self, *args, **kwargs)
            
            # Try multiple ports if the default is busy
            ports_to_try = [self.port, self.port + 1, self.port + 2, 9000, 9001, 9002]
            
            for port in ports_to_try:
                try:
                    self.server = HTTPServer((self.host, port), handler)
                    self.port = port  # Update the port if we had to change it
                    self.server.serve_forever()
                    break
                except OSError as e:
                    if port == ports_to_try[-1]:  # Last port tried
                        # Server failed to start on any port - continue silently
                        pass
                    else:
                        # Port busy, try next port
                        continue
                except Exception as e:
                    # Server failed to start - continue silently
                    break
        
        self.server_thread = threading.Thread(target=run_server, daemon=True)
        self.server_thread.start()
        
        # Give server time to start
        time.sleep(1.0)
    
    def create_terminal_link(self, original_url):
        """Create a terminal hyperlink that shows display_host but links to localhost"""
        # Add http:// if not present
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'http://' + original_url
            
        short_code = self.generate_short_code()
        
        # Store in database
        conn = sqlite3.connect(self.db_name)
        with conn:
            conn.execute('''
                INSERT INTO urls (original_url, short_code)
                VALUES (?, ?)
            ''', (original_url, short_code))
        conn.close()
        
        # Create the actual working URL
        working_url = f"http://{self.host}:{self.port}/{short_code}"
        display_url = f"http://{self.display_host}/{short_code}"
        
        # Return terminal hyperlink (shows display_host but links to localhost)
        # Format: \033]8;;URL\033\\DISPLAY_TEXT\033]8;;\033\\
        return f"\033]8;;{working_url}\033\\{display_url}\033]8;;\033\\"
    
    def _stop_server(self):
        """Stop the redirect server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()

    def close(self):
        self._stop_server()
        self.conn.close()