# Apple Scholars in AI/ML Web Scraper

## Description

This project is a web scraper that targets the [Apple Scholars in AI/ML webpage](https://machinelearning.apple.com/work-with-us#scholars). The goal is to extract the information for each scholar into an Excel spreadsheet.

## Features

- **Yearly Data Extraction**: The scraper retrieves data for scholars from specified years (currently set to extract data from 2020-2023).
- **Detailed Scholar Profiles**: For each scholar, the scraper extracts:
   * Year of recognition
   * Name
   * Institution
   * Research area
   * Detailed bio (from a modal popup)
- **Excel Export**: After scraping, the data is exported to an Excel spreadsheet (`apple_scholars_data.xlsx`). This spreadsheet organizes the data with each scholar on a new row and separate columns for the year, name, institution, research area, and bio.

## Technologies Used

- **Python**: The primary language for the scraper.
- **Selenium**: A browser automation tool used to navigate the website and extract data.
- **pandas**: A data manipulation library in Python that aids in organizing the scraped data and exporting it to Excel format.

## Usage

Simply run the script, and it will navigate to the "Apple Scholars in AI/ML" webpage, scrape the data, and export the details to an Excel file in the root directory.
