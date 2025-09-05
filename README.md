# G-Wiki: Google Sheets + GitHub Pages Business Directory

A community business directory that uses Google Sheets as a data source and GitHub Pages for hosting. This approach provides an easy-to-manage, collaborative platform for maintaining business listings.

## Features

- 📊 **Google Sheets Integration**: All data stored in Google Sheets for easy editing
- 🔄 **Automatic Sync**: Python script syncs data from Google Sheets to Jekyll
- 🌐 **Static Site**: Fast, reliable hosting with GitHub Pages
- 🔍 **Search & Categories**: Easy navigation and discovery
- 📱 **Responsive Design**: Works on all devices
- 👥 **Community Driven**: Anyone can contribute via Google Sheets

## Quick Start

### 1. Set Up Google Sheets

1. Create a new Google Sheet with these columns:
   - Name
   - Category
   - Description
   - Phone
   - Website
   - Address
   - Additional Info

2. Get your Google Sheets API credentials:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Google Sheets API
   - Create credentials (API key)

### 2. Configure the Site

1. Fork this repository
2. **IMPORTANT: Never put API keys in your code!** Instead:
   
   **For local development:**
   ```bash
   cp .env.example .env
   # Edit .env and add your actual values
   ```
   
   **For GitHub deployment:**
   - Go to your repository Settings → Secrets and Variables → Actions
   - Add secrets:
     - `GOOGLE_SHEETS_ID`: Your spreadsheet ID
     - `GOOGLE_API_KEY`: Your API key

3. Update repository and URL settings in `_config.yml`

### 3. Sync Data

Run the sync script to fetch data from Google Sheets:

```bash
cd scripts
python3 sync_data.py
```

### 4. Build and Deploy

The site will automatically build and deploy when you push to GitHub (if using GitHub Pages).

For local development:
```bash
bundle install
bundle exec jekyll serve
```

## Environment Variables

**🔒 Security First: Never commit API keys to your repository!**

For local development, create a `.env` file:
```bash
cp .env.example .env
# Edit .env with your actual values
```

For GitHub deployment, set these as repository secrets:
- `GOOGLE_SHEETS_ID`: Your spreadsheet ID  
- `GOOGLE_API_KEY`: Your API key

The script will automatically use environment variables from either source.

## File Structure

```
├── _config.yml              # Jekyll configuration
├── _layouts/
│   └── business.html         # Business page template
├── scripts/
│   └── sync_data.py         # Data sync script
├── api/
│   └── businesses.json      # Generated API data
├── _businesses/             # Generated business pages
├── index.md                 # Homepage
├── categories.md            # Categories page
└── about.md                 # About page
```

## Automation

Set up GitHub Actions to automatically sync data:

1. Add your Google Sheets credentials as repository secrets
2. The workflow will run the sync script and commit changes
3. GitHub Pages will automatically rebuild the site

## Contributing

1. Add/edit businesses in the Google Sheet
2. The sync script will generate updated pages
3. Submit a pull request with the changes

## Security Best Practices

- ✅ **DO:** Use environment variables for API keys
- ✅ **DO:** Set secrets in GitHub repository settings
- ✅ **DO:** Use `.env` files for local development (git-ignored)
- ❌ **DON'T:** Put API keys directly in code
- ❌ **DON'T:** Commit `.env` files to git
- ❌ **DON'T:** Share API keys in public channels

## Customization

- Modify `_layouts/business.html` to change business page layout
- Update styles in the page files or add a custom CSS file
- Customize the data sync script for different sheet structures

## License

MIT License - feel free to use this for your community!
