---
---
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
