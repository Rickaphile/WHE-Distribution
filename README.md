# WHE-Distribution

## What is WHE Distribution?
The analysis of World higher-level education (WHE) distribution.<br/>
To be more specific, it is the analysis of rankings and ranking differences among universities and colleges around the globe.

## What are the problems?
* What datasets is the eligible one to use?
  - CWUR world ranking lists
    - Sources: [CWUR 2022-23 Rankings](https://cwur.org/2022-23.php), [CWUR 2019-20 Rankings](https://cwur.org/2019-20.php)
    - It is one of the largest authority in the area
    - The data provided by CWUR is one of the most geographically well-rounded
* How to effectively visualize the analyzed data? 
  - Using Tableau to map the data geographically
  - Building an interactive websites for dynamic visualization according to viewers' needs

## Preparing the data
* Collect datasets from CWUR websites
  - Building a Python scraping tool to crawl the ranking data from CWUR websites
    - Convert the scrapped results to CSV files
    - Generate spreadsheets based on these files
