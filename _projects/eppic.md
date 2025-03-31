---
layout: page
title: EPPIC
image: /assets/img/projects/postpicu.png
description: Essen Post Pediatric Intensive Care Follow-up
hide_description: true
---
<style>
/* Container for header and image */
.header-container {
display: flex;
justify-content: space-between;
align-items: center;
margin-bottom: 20px;
}
/* Style for the corner image */
.corner-image {
max-width: 200px;
max-height: 150px;
object-fit: contain;
}
/* Override default header margins */
.header-container h1 {
margin: 0;
}
/* Style for the title container */
.title-container {
display: flex;
flex-direction: column;
align-items: flex-start;
}
/* Style for the description subtitle */
.description-subtitle {
color: #555;
font-weight: 400;
margin-top: 5px;
margin-bottom: 0;
font-size: 1.1em;
}
/* Hide the default page title - we'll add our own in the flex container */
.page-title {
display: none;
}
</style>
<!-- Custom header with image aligned to title -->
<div class="header-container">
  <div class="title-container">
    <h1>{{ page.title }}</h1>
    <h3 class="description-subtitle">{{ page.description }}</h3>
  </div>
  <img src="{{ '/assets/img/projects/postpicu.png' | relative_url }}" alt="PICS" class="corner-image">
</div>


## Project Goals

- Develop advanced algorithms for detecting subtle EEG changes
- Create prediction models for neurological outcomes after critical illness
- Establish best practices for EEG monitoring in pediatric intensive care
- Translate research findings into clinical applications

## Key Accomplishments

- Implemented continuous EEG monitoring protocols
- Published findings on correlation between EEG patterns and outcomes
- Developed a database of pediatric EEG recordings for research
- Collaborated with multiple centers to validate findings
