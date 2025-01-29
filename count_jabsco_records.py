import csv

file_path = '/Users/alessioivoycazzaniga/CSVer/Cef unified.csv'
manufacturer_to_count = 'JABSCO'
count = 0

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Manufacturer'] == manufacturer_to_count:
            count += 1

print(f"Number of records with {manufacturer_to_count} as manufacturer: {count}")
