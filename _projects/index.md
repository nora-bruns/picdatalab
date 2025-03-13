Looking at the first pasted HTML code, I can see the card-style boxes used on the Klinik für Kinderheilkunde I website. I'll help you adapt this style to work with your Markdown script from paste-2.txt.

The boxes on the original site use card elements with images, titles, and buttons. In the second pasted file, you already have a card-like layout using HTML and CSS in a Markdown file. Let's modify it to more closely match the style from the first example.

Here's the modified version of your Markdown file with CSS styling that mimics the boxes from the Kinderklinik website:

```markdown
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
    border: 1px solid #e5eaf3;
    border-radius: 8px;
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    background-color: #e5eaf3;
  }

  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  }

  .project-image {
    height: 240px;
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
    margin: 0 0 8px 0;
    font-size: 1.4em;
    color: #00338d; /* UKE blue color */
    font-weight: bold;
  }

  .project-description {
    margin: 0;
    color: #3d3d3c;
    font-size: 0.9em;
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
  }

  .button-with-chevron:after {
    content: "›";
    position: absolute;
    right: 15px;
    font-size: 20px;
    top: 50%;
    transform: translateY(-50%);
  }

  .button-with-chevron:hover {
    background-color: #002266; /* Darker blue */
  }
</style>

<div class="projects-container">
  
  <!-- qEEG -->
  {% assign qeeg = site.projects | where: "slug", "qeeg" | first %}
  {% if qeeg %}
  <a href="{{ qeeg.url | relative_url }}" class="project-card">
    <div class="project-image">
      <img src="{{ qeeg.image | default: '/assets/img/projects/qeeg.jpg' | relative_url }}" alt="{{ qeeg.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title">{{ qeeg.title }}</h3>
      <p class="project-description">{{ qeeg.description }}</p>
    </div>
    <div class="project-footer">
      <span class="button-with-chevron">Mehr</span>
    </div>
  </a>
  {% endif %}
  
  <!-- SaVeBRAIN -->
  {% assign savebrain = site.projects | where: "slug", "savebrain" | first %}
  {% if savebrain %}
  <a href="{{ savebrain.url | relative_url }}" class="project-card">
    <div class="project-image">
      <img src="{{ savebrain.image | default: '/assets/img/projects/savebrain.jpg' | relative_url }}" alt="{{ savebrain.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title">{{ savebrain.title }}</h3>
      <p class="project-description">{{ savebrain.description }}</p>
    </div>
    <div class="project-footer">
      <span class="button-with-chevron">Mehr</span>
    </div>
  </a>
  {% endif %}
  
  <!-- FAB -->
  {% assign fab = site.projects | where: "slug", "fab" | first %}
  {% if fab %}
  <a href="{{ fab.url | relative_url }}" class="project-card">
    <div class="project-image">
      <img src="{{ fab.image | default: '/assets/img/projects/fab.jpg' | relative_url }}" alt="{{ fab.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title">{{ fab.title }}</h3>
      <p class="project-description">{{ fab.description }}</p>
    </div>
    <div class="project-footer">
      <span class="button-with-chevron">Mehr</span>
    </div>
  </a>
  {% endif %}
  
  <!-- Project Four (Reserve) -->
  {% assign project_four = site.projects | where: "slug", "project-four" | first %}
  {% if project_four %}
  <a href="{{ project_four.url | relative_url }}" class="project-card">
    <div class="project-image">
      <img src="{{ project_four.image | default: '/assets/img/projects/project-four.jpg' | relative_url }}" alt="{{ project_four.title }}">
    </div>
    <div class="project-content">
      <h3 class="project-title">{{ project_four.title }}</h3>
      <p class="project-description">{{ project_four.description }}</p>
    </div>
    <div class="project-footer">
      <span class="button-with-chevron">Mehr</span>
    </div>
  </a>
  {% endif %}
  
</div>
```

Key changes I made:
1. Added a style section that creates cards with the light blue background (#e5eaf3) similar to the Kinderklinik site
2. Used the UKE blue color (#00338d) for titles and buttons
3. Created a "Mehr" button with chevron styling similar to the original site
4. Added hover effects to make the cards more interactive
5. Structured the cards with image, content, and footer sections like the original

This should give you a similar look to the boxes on the Kinderklinik website while working within your Jekyll markdown template structure.