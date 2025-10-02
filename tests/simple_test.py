#!/usr/bin/env python3
"""
Simple debug test for URL shortener
"""

import time
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_functionality():
    print("🔍 Testing URL Shortener Step by Step")
    print("="*50)
    
    try:
        print("1️⃣ Importing URLShortener...")
        from app.url_shortener import URLShortener
        print("✅ Import successful")
        
        print("\n2️⃣ Creating URLShortener instance...")
        shortener = URLShortener(port=8888, display_host='cf.link')
        print("✅ URLShortener created")
        
        print("\n3️⃣ Waiting for server to start...")
        time.sleep(2)
        
        print("\n4️⃣ Testing URL creation...")
        test_url = "https://google.com"
        shortened = shortener.shorten_url_functional(test_url)
        print(f"✅ Created shortened URL: {shortened}")
        
        print("\n5️⃣ Testing database lookup...")
        short_code = shortened.split('/')[-1]
        retrieved = shortener.get_original_url(short_code)
        print(f"✅ Retrieved URL: {retrieved}")
        
        if retrieved == test_url:
            print("✅ Database works correctly!")
        else:
            print(f"❌ Database mismatch: expected {test_url}, got {retrieved}")
        
        print("\n6️⃣ Testing terminal link creation...")
        terminal_link = shortener.create_terminal_link("https://github.com")
        print(f"✅ Terminal link created: {len(terminal_link)} characters")
        
        print("\n7️⃣ Server status check...")
        if shortener.server and shortener.server_thread.is_alive():
            print("✅ Server is running")
        else:
            print("❌ Server is not running")
        
        print(f"\n🌐 Server should be accessible at: http://localhost:8888")
        print(f"🔗 Try opening this URL manually: {shortened}")
        
        print("\n⏳ Keeping server alive for 60 seconds...")
        print("   Try clicking the URL above in your browser")
        print("   You should see debug messages when you click")
        
        for i in range(60, 0, -1):
            if i % 10 == 0:
                print(f"\n   ⏱️  {i} seconds remaining...")
            time.sleep(1)
        
        print("\n\n8️⃣ Cleaning up...")
        shortener.close()
        print("✅ Cleanup complete")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_basic_functionality()