---
layout: home
---

# Welcome to G-Wiki

A community business directory powered by Google Sheets and GitHub Pages. Our data is sourced from a collaborative Google Sheet, making it easy for community members to contribute and maintain up-to-date business information.

## Features

- **Easy Data Management**: All business data is stored in Google Sheets for easy editing and collaboration
- **Automatic Updates**: The site automatically fetches the latest data from Google Sheets
- **Search & Filter**: Find businesses by category, name, or services
- **Community Driven**: Anyone can contribute by editing the Google Sheet

<div id="businesses-container">
  <div class="loading">Loading businesses...</div>
</div>

<script>
// Fetch businesses from Google Sheets
async function loadBusinesses() {
  const container = document.getElementById('businesses-container');
  
  try {
    // Use Jekyll baseurl for GitHub Pages compatibility
    const baseUrl = '{{ site.baseurl }}';
    const apiUrl = `${baseUrl}/api/businesses.json`;
    console.log('Fetching businesses from', apiUrl);
    
    const response = await fetch(apiUrl);
    
    console.log('Response status:', response.status);
    console.log('Response ok:', response.ok);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    console.log('Data received:', data);
    
    if (!data.businesses) {
      throw new Error('No businesses property in response');
    }
    
    displayBusinesses(data.businesses);
  } catch (error) {
    console.error('Error loading businesses:', error);
    container.innerHTML = 
      `<p>Error loading businesses: ${error.message}. Please try again later.</p>
       <p><small>Check the browser console for more details.</small></p>`;
  }
}

function displayBusinesses(businesses) {
  const container = document.getElementById('businesses-container');
  
  console.log('Displaying businesses:', businesses);
  
  if (!businesses || businesses.length === 0) {
    container.innerHTML = '<p>No businesses found.</p>';
    return;
  }
  
  // Use Jekyll baseurl for GitHub Pages compatibility
  const baseUrl = '{{ site.baseurl }}';
  
  const html = businesses.map(business => `
    <div class="business-card">
      <h3><a href="${baseUrl}/business/${business.slug}/">${business.name}</a></h3>
      <p class="category">${business.category}</p>
      <p class="description">${business.description}</p>
      <div class="contact-info">
        ${business.phone ? `<span class="phone">📞 ${business.phone}</span>` : ''}
        ${business.website ? `<a href="${business.website}" target="_blank">🌐 Website</a>` : ''}
      </div>
    </div>
  `).join('');
  
  container.innerHTML = html;
  console.log('Businesses displayed successfully');
}

// Load businesses when page loads
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM loaded, loading businesses...');
  loadBusinesses();
});
</script>

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
