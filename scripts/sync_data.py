#!/usr/bin/env python3
import os
import json
import requests
from datetime import datetime
from pathlib import Path

# Load environment variables from .env file for local development
def load_env_file():
    """Load environment variables from .env file if it exists"""
    env_file = Path(__file__).parent.parent / '.env'
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

# Load .env file for local development
load_env_file()

# Configuration - use environment variables for security
SPREADSHEET_ID = os.environ.get('GOOGLE_SHEETS_ID')
API_KEY = os.environ.get('GOOGLE_API_KEY')
SHEET_NAME = 'Businesses'  # Name of the sheet tab

if not SPREADSHEET_ID or not API_KEY:
    print("Error: Missing required environment variables!")
    print("Please set GOOGLE_SHEETS_ID and GOOGLE_API_KEY")
    print("For local development, create a .env file based on .env.example")
    print("For GitHub Actions, set these as repository secrets")
    exit(1)

def fetch_sheet_data():
    """Fetch data from Google Sheets API"""
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{SHEET_NAME}?key={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_businesses(data):
    """Convert sheet data to business objects"""
    if not data or 'values' not in data:
        return []
    
    rows = data['values']
    if len(rows) < 2:  # Need header + at least one row
        return []
    
    headers = [h.lower().replace(' ', '_') for h in rows[0]]
    businesses = []
    
    for row in rows[1:]:
        # Pad row if it's shorter than headers
        while len(row) < len(headers):
            row.append('')
        
        business = {}
        for i, header in enumerate(headers):
            business[header] = row[i] if i < len(row) else ''
        
        # Create slug for URL
        business['slug'] = business.get('name', '').lower().replace(' ', '-').replace('&', 'and')
        business['slug'] = ''.join(c for c in business['slug'] if c.isalnum() or c == '-')
        
        businesses.append(business)
    
    return businesses

def generate_json_data(businesses):
    """Generate JSON data file"""
    data = {
        'last_updated': datetime.now().isoformat(),
        'businesses': businesses
    }
    
    # Create api directory if it doesn't exist
    os.makedirs('api', exist_ok=True)
    
    with open('api/businesses.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated api/businesses.json with {len(businesses)} businesses")

def generate_business_pages(businesses):
    """Generate individual business pages"""
    os.makedirs('_businesses', exist_ok=True)
    
    for business in businesses:
        if not business.get('name'):
            continue
            
        filename = f"_businesses/{business['slug']}.md"
        
        content = f"""---
layout: business
title: "{business.get('name', '')}"
category: "{business.get('category', '')}"
phone: "{business.get('phone', '')}"
website: "{business.get('website', '')}"
address: "{business.get('address', '')}"
slug: "{business['slug']}"
---

{business.get('description', '')}

## Contact Information

{f"**Phone:** {business.get('phone', '')}" if business.get('phone') else ""}
{f"**Website:** [{business.get('website', '')}]({business.get('website', '')})" if business.get('website') else ""}
{f"**Address:** {business.get('address', '')}" if business.get('address') else ""}

## Category
{business.get('category', '')}

{f"## Additional Info\\n{business.get('additional_info', '')}" if business.get('additional_info') else ""}
"""
        
        with open(filename, 'w') as f:
            f.write(content)
    
    print(f"Generated {len(businesses)} business pages")

def main():
    print("Fetching data from Google Sheets...")
    data = fetch_sheet_data()
    
    if not data:
        print("Failed to fetch data")
        return
    
    businesses = process_businesses(data)
    print(f"Processed {len(businesses)} businesses")
    
    generate_json_data(businesses)
    generate_business_pages(businesses)
    
    print("Data sync complete!")

if __name__ == "__main__":
    main()
