import csv
import json

csv_filename = "data.csv"
json_filename = "output.json"

# 1. Read data from the CSV file
data = []
with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
    # DictReader automatically uses the first row (headers) as keys
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# 2. Convert and write the data into a JSON output file
with open(json_filename, mode="w", encoding="utf-8") as json_file:
    # indent=4 formats the JSON nicely with indentation
    json.dump(data, json_file, indent=4)

print(f"Successfully converted '{csv_filename}' to '{json_filename}'.")