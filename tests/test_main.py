#!/usr/bin/env python3
"""
Minimal test of main.py functionality
"""

def test_main():
    print("🧪 Testing main.py import and execution...")
    
    try:
        print("1️⃣ Importing main module...")
        from app.main import main
        print("✅ Import successful")
        
        print("\n2️⃣ Calling main function...")
        main()
        
    except KeyboardInterrupt:
        print("\n👋 Interrupted by user")
    except Exception as e:
        print(f"❌ Error in main: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_main()