import csv

file_path = 'QB_Projections.csv'

with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
    header = csv.DictReader(csvfile)
    rows = list(header)

columns = {x: [row[x] for row in rows] for x in header.fieldnames}

# How to access a specific column
print(columns['YDS'])

