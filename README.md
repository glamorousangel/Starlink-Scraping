# Starlink Daily Usage Scraper

A simple Python utility that processes exported Starlink billing cycle data (JSON format) and converts it into a clean, structured CSV file containing daily internet usage per date.

---

## Features

- Reads Starlink usage data from a saved JSON file
- Extracts billing cycle and daily usage entries
- Converts indexed daily usage into real calendar dates
- Outputs a clean CSV file for analysis or reporting
- Handles missing or malformed data safely

---

## Project Structure
starlink-webscraping/
│
├── starlink_data.json # Input file (exported Starlink data)
├── script.py # Main Python script (your code)
└── starlink_daily_usage.csv # Output CSV file (generated)

---

## Requirements

Make sure you have the following installed:

- Python 3.7 or higher

### Standard Libraries Used (no external installs needed)

- `json`
- `csv`
- `datetime`

---

## How to Use

### 1. Download json Data

Setup for JSON File

- Navigate to the subscription section of your Starlink account portal.

- Right-click anywhere on the page and select Inspect.

- Click on the Network tab at the top of the Developer Tools panel and select the Fetch/XHR filter.

- Refresh the page, locate the network request containing the annotated data structure, and copy the entire text from the Response tab.

- Open your project folder in VS Code, create a new file named

starlink_data.json, and paste the copied response data directly into it.


### 2. Run the Script

Open a terminal or command prompt and run:

python script.py

## 3. Output

After running successfully, the script generates:

starlink_daily_usage.csv

---

## CSV Format:
Date	Data Usage
2025-01-01	2.34 GB
2025-01-02	3.10 GB

---

## How It Works
Loads the Starlink JSON structure
Extracts billingCyclesAnnotated
Reads startDate of each billing cycle
Iterates through dailyData entries
Converts index-based entries into real calendar dates
Writes results into a structured CSV file

---

## Notes
The script assumes dailyData is ordered sequentially per billing cycle
Missing or invalid values are converted to 0.0 GB
Ensure the JSON structure matches Starlink’s exported format

---

## Example Use Case
Internet usage tracking
Data consumption analysis
Monthly reporting
Visualization in Excel or Power BI

