---
---
async function loadCategories() {
  try {
    const baseUrl = '{{ site.baseurl }}';
    const apiUrl = `${baseUrl}/api/businesses.json`;
    console.log('Fetching categories from', apiUrl);
    
    const response = await fetch(apiUrl);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    console.log('Categories data received:', data);
    
    if (!data.businesses) {
      throw new Error('No businesses property in response');
    }
    
    displayCategories(data.businesses);
  } catch (error) {
    console.error('Error loading categories:', error);
    document.getElementById('categories-container').innerHTML = 
      `<p>Error loading categories: ${error.message}. Please try again later.</p>
       <p><small>Check the browser console for more details.</small></p>`;
  }
}

function displayCategories(businesses) {
  const container = document.getElementById('categories-container');
  
  console.log('Displaying categories for businesses:', businesses);
  
  if (!businesses || businesses.length === 0) {
    container.innerHTML = '<p>No categories found.</p>';
    return;
  }
  
  // Group businesses by category
  const categories = {};
  businesses.forEach(business => {
    const category = business.category || 'Uncategorized';
    if (!categories[category]) {
      categories[category] = [];
    }
    categories[category].push(business);
  });
  
  // Sort categories alphabetically
  const sortedCategories = Object.keys(categories).sort();
  
  // Use Jekyll baseurl for GitHub Pages compatibility
  const baseUrl = '{{ site.baseurl }}';
  
  const html = sortedCategories.map(category => `
    <div class="category-section">
      <h2>${category}</h2>
      <div class="businesses-grid">
        ${categories[category].map(business => `
          <div class="business-card">
            <h3><a href="${baseUrl}/business/${business.slug}/">${business.name}</a></h3>
            <p class="description">${business.description || ''}</p>
            <div class="contact-info">
              ${business.phone ? `<span class="phone">📞 ${business.phone}</span>` : ''}
              ${business.website ? `<a href="${business.website}" target="_blank">🌐 Website</a>` : ''}
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `).join('');
  
  container.innerHTML = html;
  console.log('Categories displayed successfully');
}

// Load categories when page loads
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM loaded, loading categories...');
  loadCategories();
});
