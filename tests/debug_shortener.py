#!/usr/bin/env python3
"""
Debug script to test URL shortener step by step
"""

import time
import urllib.request
import urllib.error
from app.url_shortener import URLShortener

def debug_url_shortener():
    print("🔍 Debugging URL Shortener...")
    print("="*50)
    
    # Create shortener
    shortener = URLShortener()
    print(f"✅ URLShortener created")
    print(f"   Host: {shortener.host}:{shortener.port}")
    print(f"   Display host: {shortener.display_host}")
    
    # Wait for server to start
    time.sleep(2)
    
    # Test URL
    test_url = "https://google.com"
    print(f"\n📝 Testing with URL: {test_url}")
    
    # Create shortened URL
    shortened = shortener.shorten_url_functional(test_url)
    print(f"✅ Shortened URL created: {shortened}")
    
    # Extract short code
    short_code = shortened.split('/')[-1]
    print(f"🔑 Short code: {short_code}")
    
    # Test database lookup directly
    retrieved_url = shortener.get_original_url(short_code)
    print(f"🗄️  Database lookup result: {retrieved_url}")
    
    if retrieved_url == test_url:
        print("✅ Database lookup works!")
    else:
        print("❌ Database lookup failed!")
        return
    
    # Test HTTP request to local server
    try:
        print(f"\n🌐 Testing HTTP request to: {shortened}")
        
        # Create request that doesn't follow redirects
        req = urllib.request.Request(shortened)
        
        try:
            response = urllib.request.urlopen(req)
            print(f"📊 Response status: {response.getcode()}")
            print("❌ Got 200 instead of 302 redirect")
        except urllib.error.HTTPError as e:
            if e.code == 302:
                redirect_url = e.headers.get('Location')
                print(f"� Response status: 302 (redirect)")
                print(f"�🔄 Redirect location: {redirect_url}")
                
                if redirect_url == test_url:
                    print("✅ Redirection works perfectly!")
                else:
                    print(f"❌ Wrong redirect URL. Expected: {test_url}, Got: {redirect_url}")
            else:
                print(f"❌ Unexpected HTTP error: {e.code}")
            
    except urllib.error.URLError:
        print("❌ Could not connect to server. Server may not be running.")
    except Exception as e:
        print(f"❌ Error testing HTTP request: {e}")
    
    # Test terminal link
    terminal_link = shortener.create_terminal_link("https://github.com")
    print(f"\n🔗 Terminal link example:")
    print(f"   Raw: {repr(terminal_link)}")
    print(f"   Rendered: {terminal_link}")
    
    print(f"\n⏳ Server will run for 30 seconds...")
    print(f"🖱️  Try manually opening: {shortened}")
    
    try:
        time.sleep(30)
    except KeyboardInterrupt:
        pass
    
    print("\n👋 Stopping server...")
    shortener.close()
    print("✅ Debug completed!")

if __name__ == "__main__":
    debug_url_shortener()