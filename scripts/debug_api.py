#!/usr/bin/env python3
import os
import requests
from pathlib import Path

def load_env_file():
    env_file = Path(__file__).parent.parent / '.env'
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

load_env_file()

SPREADSHEET_ID = os.environ.get('GOOGLE_SHEETS_ID')
API_KEY = os.environ.get('GOOGLE_API_KEY')

print(f"Testing Google Sheets API...")
print(f"Spreadsheet ID: {SPREADSHEET_ID}")
print(f"API Key: {API_KEY[:10]}..." if API_KEY else "API Key: None")

# Test: Get data from Businesses sheet directly
data_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Businesses?key={API_KEY}"
print(f"\nTesting URL: {data_url}")

try:
    response = requests.get(data_url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ SUCCESS! Data retrieved")
        
        if 'values' in data:
            rows = data['values']
            print(f"Found {len(rows)} rows")
            
            if rows:
                print(f"Headers: {rows[0]}")
                
                if len(rows) > 1:
                    print("Sample data rows:")
                    for i, row in enumerate(rows[1:3], 1):  # Show first 2 data rows
                        print(f"  Row {i}: {row}")
            else:
                print("No data in sheet")
        else:
            print("No 'values' key in response")
            
    else:
        print(f"❌ ERROR: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"❌ EXCEPTION: {e}")
