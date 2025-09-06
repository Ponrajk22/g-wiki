---
layout: home
---

A community business directory powered by Google Sheets and GitHub Pages. Our data is sourced from a collaborative Google Sheet, making it easy for community members to contribute and maintain up-to-date business information.

## Features

- **Easy Data Management**: All business data is stored in Google Sheets for easy editing and collaboration
- **Automatic Updates**: The site automatically fetches the latest data from Google Sheets
- **Search & Filter**: Find businesses by category, name, or services
- **Community Driven**: Anyone can contribute by editing the Google Sheet

<div id="businesses-container">
  <div class="loading">Loading businesses...</div>
</div>

<script src="{{ site.baseurl }}/assets/js/businesses.js"></script>

<style>
.business-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem 0;
  background: #f9f9f9;
}

.business-card h3 {
  margin-top: 0;
  color: #2c3e50;
}

.business-card .category {
  color: #7f8c8d;
  font-size: 0.9rem;
  margin: 0.5rem 0;
}

.contact-info {
  margin-top: 1rem;
}

.contact-info span, .contact-info a {
  margin-right: 1rem;
  font-size: 0.9rem;
}

.loading {
  text-align: center;
  padding: 2rem;
  color: #7f8c8d;
}
</style>
