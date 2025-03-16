---
layout: page
title: Welcome to the Pediatric Intensive Care Data Lab
last_modified_at: 2025-02-25
no_link_title: false
no_excerpt: false
hide_image: false
cover: true
---
<style>
/* Container for header and image */
.header-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-bottom: 20px;
}
/* Style for the image */
.header-image {
  max-width: 100%;
  height: 300px;
  object-fit: contain;
  margin: 20px 0;
}
/* Override default header margins */
.header-container h1 {
  margin: 0;
  line-height: 1.3;
}
/* Split the title into two lines */
.header-title-top {
  display: block;
}
/* Hide the default page title - we'll add our own in the flex container */
.page-title {
  display: none;
}
/* Button with chevron style */
.explore-link-container {
  text-align: center;
  margin: 30px 0;
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
</style>
<!-- Vertically stacked header layout -->
<div class="header-container">
  <h1>
    <span class="header-title-top">Welcome to the</span>
    Pediatric Intensive Care Data Lab
  </h1>
  <img src="{{ '/assets/img/projects/qeeg2.png' | relative_url }}" alt="Quantitative EEG" class="header-image">
</div>

<div class="explore-link-container">
  <a href="home/index.md" class="button-with-chevron">Start exploring</a>
</div>