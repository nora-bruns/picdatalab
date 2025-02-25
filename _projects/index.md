---
layout: page
title: Projects
permalink: /projects/
no_date_top: true
---
<div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: center; margin-bottom: 30px;">
  
  {% for project in site.projects %}
    <a href="{{ project.url | relative_url }}" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
      <div style="height: 240px; overflow: hidden;">
        <img src="{{ project.image | default: '/assets/img/projects/default-project.jpg' | relative_url }}" alt="{{ project.title }}" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
      <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
        <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">{{ project.title }}</h3>
        <p style="margin: 0; color: #666; font-size: 0.9em;">{{ project.description }}</p>
      </div>
    </a>
  {% endfor %}
  
</div>
