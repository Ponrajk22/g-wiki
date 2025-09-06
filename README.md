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

2. Get your Google Sheets API credentials and Sheet ID:

<details>
<summary><strong>📝 How to Create Google API Key (Click to expand)</strong></summary>

#### Step-by-Step Guide to Create Google Sheets API Key

1. **Go to Google Cloud Console**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Sign in with your Google account

2. **Create or Select a Project**
   - Click the project dropdown at the top
   - Either select an existing project or click "New Project"
   - If creating new: Give it a name like "G-Wiki Business Directory"

3. **Enable Google Sheets API**
   - In the left sidebar, go to "APIs & Services" → "Library"
   - Search for "Google Sheets API"
   - Click on it and press "Enable"

4. **Create API Credentials**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "API Key"
   - Copy the generated API key immediately
   - **Important**: Keep this key secure and never share it publicly

5. **Restrict the API Key (Recommended)**
   - Click on the pencil icon next to your new API key
   - Under "Application restrictions": Choose "HTTP referrers" if using for web
   - Under "API restrictions": Select "Restrict key" and choose "Google Sheets API"
   - Save the restrictions

6. **Test Your API Key**
   - You can test it works by visiting: 
   ```
   https://sheets.googleapis.com/v4/spreadsheets/YOUR_SHEET_ID/values/Sheet1?key=YOUR_API_KEY
   ```

</details>

<details>
<summary><strong>🔗 How to Get Google Sheet ID (Click to expand)</strong></summary>

#### Finding Your Google Sheet ID

The Google Sheet ID is found in the URL of your spreadsheet:

**Example URL:**
```
https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit#gid=0
```

**The Sheet ID is the long string between `/d/` and `/edit`:**
```
1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
```

#### Steps to Get Sheet ID:

1. **Open your Google Sheet**
   - Go to [Google Sheets](https://sheets.google.com)
   - Open the spreadsheet you want to use

2. **Copy the URL**
   - Look at the address bar in your browser
   - Copy the entire URL

3. **Extract the Sheet ID**
   - Find the part between `/spreadsheets/d/` and `/edit`
   - This long string of letters and numbers is your Sheet ID

4. **Make Your Sheet Public (Required for API Access)**
   - Click "Share" button in your Google Sheet
   - Click "Change to anyone with the link"
   - Set permission to "Viewer"
   - Click "Done"

**Note**: Your sheet must be publicly readable for the API to access it, but others won't be able to edit without permissions.

</details>

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

<details>
<summary><strong>🔧 Local Development Setup (Click to expand)</strong></summary>

#### Setting Up Environment Variables Locally

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file:**
   ```bash
   # Open in your preferred editor
   nano .env
   # or
   code .env
   ```

3. **Add your actual values:**
   ```env
   GOOGLE_SHEETS_ID=your_actual_sheet_id_here
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

4. **Verify the file is git-ignored:**
   - The `.env` file should already be in `.gitignore`
   - This prevents accidentally committing your secrets

5. **Test your setup:**
   ```bash
   # Activate virtual environment
   source .venv/bin/activate
   
   # Run the sync script
   python scripts/sync_data.py
   ```

</details>

<details>
<summary><strong>🚀 GitHub Deployment Setup (Click to expand)</strong></summary>

#### Setting Up Repository Secrets for GitHub Actions

1. **Go to Repository Settings:**
   - Navigate to your GitHub repository
   - Click on "Settings" tab
   - Go to "Secrets and variables" → "Actions"

2. **Add Repository Secrets:**
   - Click "New repository secret"
   - Add the following secrets:

   **Secret 1:**
   - Name: `GOOGLE_SHEETS_ID`
   - Value: Your Google Sheet ID (the long string from the URL)

   **Secret 2:**
   - Name: `GOOGLE_API_KEY`
   - Value: Your Google API key

3. **Verify Secrets are Set:**
   - You should see both secrets listed (values will be hidden)
   - GitHub Actions can now access these during automated builds

4. **Set up GitHub Pages:**
   - In repository Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: `main` (or your default branch)
   - Folder: `/ (root)`

</details>

The script will automatically detect and use environment variables from either source (local `.env` file or GitHub secrets).

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

## Troubleshooting

<details>
<summary><strong>🐛 Common Issues and Solutions (Click to expand)</strong></summary>

### API Key Issues

**Problem**: Getting 403 or 400 errors when running sync script
**Solutions**:
- Verify your Google Sheet is publicly readable (Share → Anyone with link → Viewer)
- Check that Google Sheets API is enabled in Google Cloud Console
- Ensure API key is correctly set in environment variables
- Try creating a new API key if the current one isn't working

### Sheet ID Issues

**Problem**: "Spreadsheet not found" error
**Solutions**:
- Double-check the Sheet ID is correctly extracted from the URL
- Ensure the Sheet ID in your `.env` file doesn't have extra spaces or characters
- Verify the sheet exists and is accessible

### Environment Variable Issues

**Problem**: Script can't find API key or Sheet ID
**Solutions**:
- Verify `.env` file exists and has correct variable names
- Check that you're running the script from the correct directory
- For GitHub Actions, ensure repository secrets are named exactly `GOOGLE_SHEETS_ID` and `GOOGLE_API_KEY`

### Jekyll Build Issues

**Problem**: Site not updating after running sync script
**Solutions**:
- Check if Jekyll collections are properly configured in `_config.yml`
- Restart Jekyll server: `bundle exec jekyll serve`
- Verify generated files exist in `_businesses/` directory

### Data Not Updating

**Problem**: Website shows old data even after sync
**Solutions**:
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
- Check if API endpoint `http://localhost:4000/api/businesses.json` shows updated data
- Restart Jekyll development server
- For GitHub Pages, wait a few minutes for deployment to complete

</details>

## License

MIT License - feel free to use this for your community!
