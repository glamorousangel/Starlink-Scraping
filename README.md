# Starlink Usage Scraper

A lightweight Python tool that extracts daily data usage from a saved Starlink dashboard HTML file and converts the bar chart into structured CSV data for your billing cycle.

---

## What it does
- Reads total data usage from the Starlink dashboard (GB)
- Converts bar chart pixel heights into real usage values
- Maps each bar to the correct date based on the billing cycle
- Anchors the cycle to the **17th of each month**
- Exports results into a clean CSV file

---

## Requirements
- Python 3.x
- beautifulsoup4

Install dependency:
```bash
pip install beautifulsoup4
