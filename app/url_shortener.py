import sqlite3
import string
import random

class URLShortener:
    def __init__(self, db_name='url_shortener.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

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

    def shorten_url(self, original_url):
        short_code = self.generate_short_code()
        with self.conn:
            self.conn.execute('''
                INSERT INTO urls (original_url, short_code)
                VALUES (?, ?)
            ''', (original_url, short_code))
        return short_code

    def get_original_url(self, short_code):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT original_url FROM urls WHERE short_code=?
        ''', (short_code,))
        result = cursor.fetchone()
        return result[0] if result else None

    def close(self):
        self.conn.close()