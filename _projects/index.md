---
layout: page
title: Projects
permalink: /projects/
no_date_top: true
---
<style>
  .projects-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: center;
    margin-bottom: 30px;
  }

  .project-card {
    flex: 1 1 400px;
    max-width: 45%;
    min-width: 300px;
    display: block;
    border: none;
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    margin-bottom: 20px;
    background-color: #e5eaf3;
  }

  .project-image {
    height: 180px; /* Reduced height */
    overflow: hidden;
  }

  .project-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .project-content {
    padding: 16px;
    text-align: center;
    background-color: transparent;
  }

  .project-title {
    margin: 0;
    font-size: 1.4em;
    color: #00338d; /* UKE blue color */
    font-weight: 700; /* Explicitly set bold font weight */
  }

  .project-footer {
    padding: 16px;
    text-align: center;
  }

  .button-with-chevron {
    display: inline-block;
    background-color: #00338d; /* UKE blue color */
    color: #ffffff;
    font-weight: bold;
    padding: 8px 16px;
    border-radius: 0;
    text-decoration: none;
    position: relative;
    padding-right: 30px;
    cursor: pointer;
  }

  .button-with-chevron:after {
    content: "›";
    position: absolute;
    right: 15px;
    font-size: 20px;
    top: 50%;
    transform: translateY(-50%);
  }
</style>

<div class="projects-container">
  
  <!-- qEEG -->
  {% assign qeeg = site.projects | where: "slug", "qeeg" | first %}
  {% if qeeg %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ qeeg.image | default: '/assets/img/projects/qeeg.jpg' | relative_url }}" alt="{{ qeeg.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ qeeg.title }}</strong></h3>
    </div>
    <div class="project-footer">
      <a href="{{ qeeg.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
  <!-- SaVeBRAIN -->
  {% assign savebrain = site.projects | where: "slug", "savebrain" | first %}
  {% if savebrain %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ savebrain.image | default: '/assets/img/projects/savebrain.jpg' | relative_url }}" alt="{{ savebrain.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ savebrain.title }}</strong></h3>
    </div>
    <div class="project-footer">
      <a href="{{ savebrain.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
  <!-- FAB -->
  {% assign fab = site.projects | where: "slug", "fab" | first %}
  {% if fab %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ fab.image | default: '/assets/img/projects/fab.jpg' | relative_url }}" alt="{{ fab.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ fab.title }}</strong></h3>
    </div>
    <div class="project-footer">
      <a href="{{ fab.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
  <!-- Project Four (Reserve) -->
  {% assign project_four = site.projects | where: "slug", "project-four" | first %}
  {% if project_four %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ project_four.image | default: '/assets/img/projects/project-four.jpg' | relative_url }}" alt="{{ project_four.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ project_four.title }}</strong></h3>
    </div>
    <div class="project-footer">
      <a href="{{ project_four.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
</div>