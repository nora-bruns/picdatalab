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
    gap: 40px;
    justify-content: space-between; /* Changed to space-between to use full width */
    margin-bottom: 30px;
    width: 100%; /* Ensure container uses full width */
  }

  .project-card {
    flex: 0 1 calc(50% - 20px); /* Adjusted calculation to account for space-between */
    max-width: calc(50% - 20px); /* Adjusted max-width calculation */
    min-width: 300px;
    display: block;
    border: none;
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    margin-bottom: 20px;
    background-color: #e5eaf3;
  }

  /* This ensures we maintain left alignment when there's an odd number of items */
  .projects-container::after {
    content: "";
    flex: 0 1 calc(50% - 20px);
    max-width: calc(50% - 20px);
  }

  .project-image {
    height: 180px;
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
  }
</style>

<div class="projects-container">
  
  <!-- qEEG -->
  {% assign qeeg = site.projects | where: "slug", "qeeg" | first %}
  {% if qeeg %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ qeeg.image | default: '/assets/img/projects/qeeg.png' | relative_url }}" alt="{{ qeeg.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ qeeg.title }}</strong></h3>
    </div>
    <div class="project-footer">
      <a href="{{ qeeg.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
  <!-- DRG -->
  {% assign drg = site.projects | where: "slug", "drg" | first %}
  {% if drg %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ drg.image | default: '/assets/img/projects/drg.png' | relative_url }}" alt="{{ drg.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ drg.title }}</strong></h3>
    </div>
    <div class="project-footer">
      <a href="{{ drg.url | relative_url }}" class="button-with-chevron">Learn more</a>
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
    </div>
    <div class="project-footer">
      <a href="{{ savebrain.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}
  
  <!-- Post-PICU -->
  {% assign postpicu = site.projects | where: "slug", "postpicu" | first %}
  {% if postpicu %}
  <div class="project-card">
    <div class="project-image">
      <img src="{{ postpicu.image | default: '/assets/img/projects/postpicu.png' | relative_url }}" alt="{{ savebrain.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title"><strong>{{ postpicu.title }}</strong></h3>
    </div>
    <div class="project-footer">
      <a href="{{ postpicu.url | relative_url }}" class="button-with-chevron">Learn more</a>
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
    </div>
    <div class="project-footer">
      <a href="{{ pia.url | relative_url }}" class="button-with-chevron">Learn more</a>
    </div>
  </div>
  {% endif %}

</div>