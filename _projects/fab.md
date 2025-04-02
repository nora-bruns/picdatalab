---
layout: page
title: FAB.NRW
# image: /assets/img/projects/fab.png
description: Find a Bed in NRW
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
  <img src="{{ '/assets/img/projects/fab.png' | relative_url }}" alt="FAB" class="corner-image">
</div>




## Background
After a decline in pediatric respiratory infections during the pandemic, a rebound wave of infections in fall/winter 2022/2023 overwhelmed all areas of the pediatric healthcare system. Even urgently needed inpatient or intensive care treatments sometimes had to be provided far away from the patient's residence and finding treatment placement was very time consuming.
## Goal
FAB.NRW focuses on the quick and targeted location of treatment places  for children requiring inpatient admission. The software was designed to display the availabe hospital beds for the required level care, facilitating patient transfer between hospitals and helping to allocate patients efficiently. 
## Target Group and Role of University Hospital Essen (UME)
All children‘s hospitals in North Rhine-Westphalia have the opportunity to participate as reporting facilities (voluntary participation, no fees). The Children‘s hospital of the UME acts as the coordination center of the network.

## State of the project
The software has been developed and online since November 2023, with more than 50 hospitals participating. A steering committee that consists of representatives from participating hospitals oversees the project's implementation. 
Regular user surveys are conducted to evaluate improvements of the network. Evaluation of usage with respect to infectious waves is planned for the end of 2025. Additionally, evaluation of integrating FAB.NRW into existing systems without losing key features is ongoing.

## Funding
-	Stiftung Universitätsmedizin Essen
-	Stiftung Kinderschutz NRW
-	Landeszentrum Gesundheit NRW

