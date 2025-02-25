---
layout: page
title: Projects
permalink: /projects/
no_date_top: true
---
<div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: center; margin-bottom: 30px;">
  {% for project in site.pages %}
    {% if project.categories contains 'project' %}
      <a href="{{ project.url | relative_url }}" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
        <div style="height: 240px; overflow: hidden;">
          <img src="{{ project.image | relative_url }}" alt="{{ project.title }}" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
          <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">{{ project.title }}</h3>
          <p style="margin: 0; color: #666; font-size: 0.9em;">{{ project.description }}</p>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>


<div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: center; margin-bottom: 30px;">
  
  <!-- qEEG -->
  <a href="qeeg.md" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="/assets/img/projects/qeeg.jpg" alt="qEEG" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">Quantitative EEG</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">Detecting abnormalieties and predicting outcomes with EEG-based neuromonitoring</p>
    </div>
  </a>
  
  <!-- SaVeBRAIN -->
  <a href="savebrain.md" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="/assets/img/projects/savebrain.jpg" alt="SaVeBRAIN.Kids" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">SaVeBRAIN.Kids</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">Advancing outpatient care for children with mild traumatic brain injury</p>
    </div>
  </a>
  
  <!-- FAB -->
  <a href="fab.md" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="/assets/img/projects/fab.jpg" alt="FAB.NRW" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">FAB.NRW</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">Finding available pediatric hospital beds in North Rhine-Westphalia</p>
    </div>
  </a>
  
  <!-- Project Four -->
  <a href="project-four.md" style="flex: 1 1 400px; max-width: 45%; min-width: 300px; display: block; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <div style="height: 240px; overflow: hidden;">
      <img src="/assets/img/projects/project-four.jpg" alt="Project Four" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div style="padding: 16px; text-align: center; background-color: #f8f8f8;">
      <h3 style="margin: 0 0 8px 0; font-size: 1.4em;">Project Four</h3>
      <p style="margin: 0; color: #666; font-size: 0.9em;">Key highlights and purpose of Project Four in a single line</p>
    </div>
  </a>
  
</div>
