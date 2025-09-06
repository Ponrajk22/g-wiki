---
layout: default
title: Categories
---

# Business Categories

<div id="categories-container">
  <div class="loading">Loading categories...</div>
</div>

<script src="{{ site.baseurl }}/assets/js/categories.js"></script>

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
