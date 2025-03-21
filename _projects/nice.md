---
layout: page
title: NICE
# image: /assets/img/projects/qeeg.png
description: Neurological Intensive Care Assessment by EEG
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
  <img src="{{ '/assets/img/projects/qeeg.png' | relative_url }}" alt="NICE" class="corner-image">
</div>


## History
Our group‘s research journey began with amplitude-integrated EEG (aEEG) in preterm infants, initially using mere visual assessment of the tracings. Since establishing the PIC Data Lab in 2020, our focus has shifted towards pediatric intensive care patients and the approach evolved using partially automated assessments. 
Today, we focus on fully automated analysis of aEEG and explore advanced quantitative EEG processing, including Fast Fourier Transformation, burst suppression ratio, asymmetry detection, and more.

## Motivation
Preliminary evidence from small case series and adult intensive care suggests that certain quantitative EEG parameters may change before clinical neurological deterioration becomes apparent, potentially serving as early warning indicators. Additionally, our research is driven by the need for outcome prediction tools to inform clinical decision-making and provide accurate information for parent counseling.

## Current Work
We are currently conducting comprehensive analyses of quantitative parameters from approximately 1,000 EEGs collected at our center. These recordings derive from diverse patient populations, including neurologically healthy children (awake and during sedation) and critically ill children. Examining these different cohorts will provide important insights into baseline changes induced by sedation and neurological/critical illness. 
Once established we plan to apply our technical expertise and content knowledge to expand these analyses to newborn and preterm infant populations with various neurological conditions.

## Funding
-	Stiftung Universitätsmedizin
-	Medical Faculty of the University of Duisburg-Essen
-	UMEA Clinican Scientist programme