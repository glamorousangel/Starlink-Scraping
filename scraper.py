import json
import csv
from datetime import datetime, timedelta

# Open and load the saved Starlink JSON payload
with open("starlink_data.json", "r") as f:
    data = json.load(f)

rows = []

# Access the billing cycle data structure from the response
cycles = data.get("content", {}).get("billingCyclesAnnotated", [])

for billing_cycle in cycles:
    # Parse the start date of the cycle (ISO format → date only)
    raw_start = billing_cycle.get("startDate", "").split("T")[0]
    cycle_start = datetime.strptime(raw_start, "%Y-%m-%d")

    # Retrieve the list of daily usage entries
    daily_entries = billing_cycle.get("dailyData", [])

    for i, entry in enumerate(daily_entries):
        # Compute actual calendar date for each usage entry
        date_label = cycle_start + timedelta(days=i)
        date_str = date_label.strftime("%Y-%m-%d")

        # Extract numeric GB value from nested structure safely
        if entry and isinstance(entry, list) and len(entry) > 0:
            usage_gb = round(float(entry[0]), 2)
        else:
            usage_gb = 0.0

        rows.append([date_str, f"{usage_gb} GB"])

# Write processed results into a CSV file
output_file = "starlink_daily_usage.csv"

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Column headers for readability
    writer.writerow(["Date", "Data Usage"])
    writer.writerows(rows)

print(f"CSV export complete: '{output_file}' ({len(rows)} records written).")
