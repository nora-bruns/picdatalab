---
layout: page
title: Projects
permalink: /projects/
no_date_top: true
---
<div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: center; margin-bottom: 30px;">
  
  <!-- qEEG -->
  {% assign qeeg = site.projects | where: "slug", "qeeg" | first %}
  {% if qeeg %}
  <a href="{{ qeeg.url | relative_url }}" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="{{ qeeg.image | default: '/assets/img/projects/qeeg.jpg' | relative_url }}" alt="{{ qeeg.title }}" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">{{ qeeg.title }}</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">{{ qeeg.description }}</p>
    </div>
  </a>
  {% endif %}
  
  <!-- SaVeBRAIN -->
  {% assign savebrain = site.projects | where: "slug", "savebrain" | first %}
  {% if savebrain %}
  <a href="{{ savebrain.url | relative_url }}" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="{{ savebrain.image | default: '/assets/img/projects/savebrain.jpg' | relative_url }}" alt="{{ savebrain.title }}" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">{{ savebrain.title }}</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">{{ savebrain.description }}</p>
    </div>
  </a>
  {% endif %}
  
  <!-- FAB -->
  {% assign fab = site.projects | where: "slug", "fab" | first %}
  {% if fab %}
  <a href="{{ fab.url | relative_url }}" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="{{ fab.image | default: '/assets/img/projects/fab.jpg' | relative_url }}" alt="{{ fab.title }}" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">{{ fab.title }}</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">{{ fab.description }}</p>
    </div>
  </a>
  {% endif %}
  
  <!-- Project Four (Reserve) -->
  {% assign project_four = site.projects | where: "slug", "project-four" | first %}
  {% if project_four %}
  <a href="{{ project_four.url | relative_url }}" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="{{ project_four.image | default: '/assets/img/projects/project-four.jpg' | relative_url }}" alt="{{ project_four.title }}" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">{{ project_four.title }}</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">{{ project_four.description }}</p>
    </div>
  </a>
  {% endif %}
  
</div>
