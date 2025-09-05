---
layout: default
title: Categories
---

# Business Categories

<div id="categories-container">
  <div class="loading">Loading categories...</div>
</div>

<script>
async function loadCategories() {
  try {
    const response = await fetch('/api/businesses.json');
    const data = await response.json();
    displayCategories(data.businesses);
  } catch (error) {
    document.getElementById('categories-container').innerHTML = 
      '<p>Error loading categories. Please try again later.</p>';
  }
}

function displayCategories(businesses) {
  const container = document.getElementById('categories-container');
  
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
  
  const html = sortedCategories.map(category => `
    <div class="category-section">
      <h2>${category}</h2>
      <div class="businesses-grid">
        ${categories[category].map(business => `
          <div class="business-card">
            <h3><a href="/business/${business.slug}/">${business.name}</a></h3>
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
}

// Load categories when page loads
document.addEventListener('DOMContentLoaded', loadCategories);
</script>

<style>
.category-section {
  margin: 2rem 0;
}

.category-section h2 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}

.businesses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.business-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  background: #f9f9f9;
  transition: transform 0.2s;
}

.business-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.business-card h3 {
  margin-top: 0;
  color: #2c3e50;
}

.business-card .description {
  color: #555;
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
