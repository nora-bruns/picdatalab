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
    gap: 60px 60px; /* First value controls row gap (vertical), second controls column gap (horizontal) */
    justify-content: space-between;
    margin-bottom: 40px; /* Increased from 30px */
    width: 100%;
  }

  .project-card {
    flex: 0 1 calc(45% - 30px); /* Reduced from 50% to make cards smaller */
    max-width: calc(45% - 30px); /* Reduced from 50% to make cards smaller */
    min-width: 280px; /* Slightly reduced from 300px */
    display: block;
    border: none;
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    margin-bottom: 40px; /* Increased from 20px to add more vertical spacing */
    background-color: #e5eaf3;
  }

  /* This ensures we maintain left alignment when there's an odd number of items */
  .projects-container::after {
    content: "";
    flex: 0 1 calc(45% - 30px); /* Match the new card size */
    max-width: calc(45% - 30px); /* Match the new card size */
  }

  .project-image {
    height: 160px; /* Reduced from 180px */
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white; /* Add white background */
  }

  .project-image img {
    max-width: 100%;     /* Image won't exceed container width */
    max-height: 100%;    /* Image won't exceed container height */
    object-fit: contain; /* Ensures the image is scaled to fit within box while maintaining aspect ratio */
    display: block;      /* Removes any extra space below image */
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
    font-weight: 700;
  }
  
  .project-description {
    margin-top: 10px;
    font-size: 0.9em;
    color: #333;
    line-height: 1.4;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* Limit to 3 lines */
    -webkit-box-orient: vertical;
    text-overflow: ellipsis;
    max-height: 3.9em; /* Approximately 3 lines */
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
    border-radius: 4px;
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
  
  /* Media query to ensure proper sizing on smaller screens */
  @media (max-width: 768px) {
    .project-card {
      flex: 0 1 100%;
      max-width: 100%;
    }
    
    .projects-container {
      gap: 40px; /* Slightly reduce gap on mobile */
    }
  }
</style>

<div class="projects-container">
  
  <!-- NICE -->
  {% assign nice = site.projects | where: "slug", "nice" | first %}
  {% if nice %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ nice.image | default: '/assets/img/projects/qeeg.png' | relative_url }}" alt="{{ nice.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ nice.title }}</strong></h3>
      {% if nice.description %}
      <p class="project-description">{{ nice.description }}</p>
      {% endif %}
    </div>
    <div class="project-footer">
      <a href="{{ nice.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
  <!-- HOPE -->
  {% assign hope = site.projects | where: "slug", "hope" | first %}
  {% if hope %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ hope.image | default: '/assets/img/projects/hope.png' | relative_url }}" alt="{{ hope.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ hope.title }}</strong></h3>
      {% if hope.description %}
      <p class="project-description">{{ hope.description }}</p>
      {% endif %}
    </div>
    <div class="project-footer">
      <a href="{{ hope.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}

  <!-- SaVeBRAIN -->
  {% assign savebrain = site.projects | where: "slug", "savebrain" | first %}
  {% if savebrain %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ savebrain.image | default: '/assets/img/projects/savebrain.png' | relative_url }}" alt="{{ savebrain.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ savebrain.title }}</strong></h3>
      {% if savebrain.description %}
      <p class="project-description">{{ savebrain.description }}</p>
      {% endif %}
    </div>
    <div class="project-footer">
      <a href="{{ savebrain.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
  <!-- EPPIC -->
 {% assign eppic = site.projects | where: "slug", "eppic" | first %}
 {% if eppic %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ postpicu.image | default: '/assets/img/projects/postpicu.png' | relative_url }}" alt="{{ postpicu.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ eppic.title }}</strong></h3>
      {% if postpicu.description %}
      <p class="project-description">{{ eppic.description }}</p>
      {% endif %}
    </div>
    <div class="project-footer">
      <a href="{{ eppic.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}

  <!-- FAB -->
  {% assign fab = site.projects | where: "slug", "fab" | first %}
  {% if fab %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ fab.image | default: '/assets/img/projects/fab.png' | relative_url }}" alt="{{ fab.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ fab.title }}</strong></h3>
      {% if fab.description %}
      <p class="project-description">{{ fab.description }}</p>
      {% endif %}
    </div>
    <div class="project-footer">
      <a href="{{ fab.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
    <!-- PIA -->
  {% assign pia = site.projects | where: "slug", "pia" | first %}
  {% if pia %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ pia.image | default: '/assets/img/projects/pia.png' | relative_url }}" alt="{{ pia.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ pia.title }}</strong></h3>
      {% if pia.description %}
      <p class="project-description">{{ pia.description }}</p>
      {% endif %}
    </div>
    <div class="project-footer">
      <a href="{{ pia.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}

</div>