---
layout: page
title: HOPE-TBI
description: Hospital Data for Pediatric TBI Research
image: /assets/img/projects/hope.png
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
  <img src="{{ '/assets/img/projects/hope.png' | relative_url }}" alt="HOPE" class="corner-image">
</div>


## Background
Traumatic Brain Injury (TBI) represents one of the major public health concerns in pediatric populations across the world. While moderate and severe TBI are luckily rare, this creates challenges in gathering large-scale data for research and evidence synthesis. At the same time, optimizing diagnostic and neuroprotective management during the acute phase is crucial in order to avoid secondary brain injury.

Routine healthcare data provides the opportunity to investigate moderate and severe TBI on a larger scale. The German hospital dataset offers nationwide comprehensive coverage of pediatric hospital discharges, creating an ideal platform for in-depth TBI research.

## Methodological preparatory work
Because stratification or adjustment for injury severity is indispensable in trauma research, we have implemented two distinct methods to measure injury severity in pediatric trauma patients from routine health care data:
-	An adapted mapping-based that allows to calculate the Abbreviated Injury Scale (AIS) and Injury Severity Score (ISS) from the German modification of the International Classification of Diseases (ICD-10)
-	An internal approach that calculates survival probability directly from cases within the database (survival risk ratios)

This foundational work provides the methodological basis for our current research using the German hospital dataset.

## Current work
We are assessing various aspects of TBI in the German hospital dataset to answer – among others – these research questions:
-	How do mortality and outcomes in children with severe traumatic brain injury differ depending on the timing of decompressive craniectomy?
-	How does ICP monitoring in children with severe TBI affect mortality and outcomes?
-	How do mortality and outcomes differ in children with serious TBI when treated in pediatric versus adult intensive care units?
-	How did hospitalization numbers for mild versus moderate-severe TBI change during the pandemic-related reduction in TBI-related hospitalizations?

Because the reliability of routine healthcare data varies considerably depending on the context in which it was collected, we work on cross-verifying clinical data with routine healthcare data on both single and multicenter basis, e.g. For assessing organ dysfunction.  Insights from these analyses will help to further develop approaches to reduce bias in research from routine healthcare datasets.

## Funding
–	Save-my-brain foundation
