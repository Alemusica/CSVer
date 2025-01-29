import csv

input_file = '/Users/alessioivoycazzaniga/CSVer/Cef unified.csv'
output_file = '/Users/alessioivoycazzaniga/CSVer/VolvoPentaRecords.csv'
manufacturer = 'VOLVO-PENTA'

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write header to the output file
    header = next(reader)
    writer.writerow(header)
    
    # Filter and write rows
    for row in reader:
        if manufacturer in row:
            writer.writerow(row)