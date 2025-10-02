#!/usr/bin/env python3
"""
Quick test script to verify URL shortener functionality
"""

import time
from app.url_shortener import URLShortener

def test_url_shortener():
    print("🔗 Testing URL Shortener...")
    print("="*40)
    
    # Create shortener
    shortener = URLShortener()
    
    # Wait for server to start
    time.sleep(1)
    
    # Test URL
    test_url = "https://github.com/Corefinder89"
    
    # Create different types of URLs
    display_url = shortener.shorten_url_for_display(test_url)
    working_url = shortener.shorten_url_functional(test_url)
    terminal_link = shortener.create_terminal_link("https://google.com")
    url_mapping = shortener.create_display_with_working_url("https://wikipedia.org")
    
    print(f"Original URL: {test_url}")
    print(f"Display URL (pretty): {display_url}")
    print(f"Working URL (functional): {working_url}")
    print(f"Terminal hyperlink: {terminal_link}")
    print(f"URL mapping: Display={url_mapping['display']}, Working={url_mapping['working']}")
    print(f"Server running at: http://{shortener.host}:{shortener.port}")
    print(f"Display host set to: {shortener.display_host}")
    
    # Test database lookup
    short_code = working_url.split('/')[-1]
    retrieved_url = shortener.get_original_url(short_code)
    
    print(f"Short code: {short_code}")
    print(f"Retrieved URL: {retrieved_url}")
    
    if retrieved_url == test_url:
        print("✅ Database lookup works!")
    else:
        print("❌ Database lookup failed!")
    
    print("\n🖱️  Try clicking these URLs:")
    print(f"   Display URL: {display_url} (won't work - just for show)")
    print(f"   Working URL: {working_url} (click this one!)")
    print(f"   Terminal Link: {terminal_link} (shows cf.link but works!)")
    print(f"   URL Mapping: {url_mapping['display']} → {url_mapping['working']}")
    print("\n⏳ Server will run for 30 seconds...")
    
    try:
        time.sleep(30)
    except KeyboardInterrupt:
        pass
    
    print("\n👋 Stopping server...")
    shortener.close()
    print("✅ Test completed!")

if __name__ == "__main__":
    test_url_shortener()