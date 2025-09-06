#!/usr/bin/env python3
"""
Test script to verify GitHub secrets are properly set
"""
import os

def test_secrets():
    print("=== Testing GitHub Secrets ===")
    
    # Get environment variables
    sheets_id = os.environ.get('GOOGLE_SHEETS_ID')
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    print(f"GOOGLE_SHEETS_ID exists: {sheets_id is not None}")
    print(f"GOOGLE_SHEETS_ID length: {len(sheets_id) if sheets_id else 0}")
    print(f"GOOGLE_SHEETS_ID starts with: {sheets_id[:10] + '...' if sheets_id and len(sheets_id) > 10 else sheets_id}")
    print()
    print(f"GOOGLE_API_KEY exists: {api_key is not None}")
    print(f"GOOGLE_API_KEY length: {len(api_key) if api_key else 0}")
    print(f"GOOGLE_API_KEY starts with: {api_key[:10] + '...' if api_key and len(api_key) > 10 else api_key}")
    print()
    
    if not sheets_id:
        print("❌ GOOGLE_SHEETS_ID is missing!")
        print("   Check that the repository secret is named exactly 'GOOGLE_SHEETS_ID'")
    elif len(sheets_id) < 20:
        print("⚠️  GOOGLE_SHEETS_ID seems too short (should be ~44 characters)")
    else:
        print("✅ GOOGLE_SHEETS_ID looks good")
    
    if not api_key:
        print("❌ GOOGLE_API_KEY is missing!")
        print("   Check that the repository secret is named exactly 'GOOGLE_API_KEY'")
    elif len(api_key) < 30:
        print("⚠️  GOOGLE_API_KEY seems too short (should be ~39 characters)")
    else:
        print("✅ GOOGLE_API_KEY looks good")
    
    print("\n=== All Environment Variables ===")
    for key, value in sorted(os.environ.items()):
        if 'GOOGLE' in key or 'API' in key or 'SHEET' in key:
            print(f"{key}: {value[:10] + '...' if value and len(value) > 10 else value}")

if __name__ == "__main__":
    test_secrets()
