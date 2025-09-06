#!/usr/bin/env python3
import os
import requests
from pathlib import Path

# Load environment variables from .env file
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

print(f"Spreadsheet ID: {SPREADSHEET_ID}")
print(f"API Key: {API_KEY[:10]}..." if API_KEY else "API Key: None")

# Test 1: Get spreadsheet info
url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?key={API_KEY}"
print(f"\nTesting spreadsheet access...")
print(f"URL: {url}")

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Spreadsheet found: {data.get('properties', {}).get('title', 'Unknown')}")
        
        # List all sheets
        sheets = data.get('sheets', [])
        print(f"Available sheets:")
        for sheet in sheets:
            sheet_name = sheet['properties']['title']
            print(f"  - {sheet_name}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Response: {response.text}")
# Test 2: Get data from Businesses sheet
print(f"\n" + "="*50)
print("Testing Businesses sheet data...")
data_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Businesses?key={API_KEY}"
print(f"URL: {data_url}")

try:
    response = requests.get(data_url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Data retrieved successfully!")
        if 'values' in data:
            print(f"Rows found: {len(data['values'])}")
            if data['values']:
                print(f"Headers: {data['values'][0]}")
                if len(data['values']) > 1:
                    print(f"First row: {data['values'][1]}")
        else:
            print("⚠️  No 'values' in response - sheet might be empty")
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ Exception: {e}")
