import csv
import os

def int_to_superscript(n):
    # Convert integer to a string of superscript digits using Unicode
    superscripts = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'}
    return ''.join(superscripts[d] for d in str(n))

def process_csv(input_path, output_path, notes_output_path):
    rows = []
    remark_col = "Remarks (Compatibility - years - notes)"
    # Lettura del CSV
    with open(input_path, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)
    # Conta le occorrenze dei remark
    remark_freq = {}
    for row in rows:
        remark = row[remark_col].strip()
        if remark:
            remark_freq[remark] = remark_freq.get(remark, 0) + 1
    # Costruisci la mappa remark -> numero di nota solo per remark ripetuti
    remark_mapping = {}
    note_counter = 1
    for remark, freq in remark_freq.items():
        if freq > 1:
            remark_mapping[remark] = note_counter
            note_counter += 1
    # Sostituisci i remark ripetuti con il corrispondente esponente, altrimenti lascia il testo originale
    for row in rows:
        remark = row[remark_col].strip()
        if remark and remark in remark_mapping:
            row[remark_col] = int_to_superscript(remark_mapping[remark])
    # Scrittura del nuovo CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    # Crea il file per le note (solo per i remark ripetuti)
    with open(notes_output_path, 'w', encoding='utf-8') as notes_file:
        for remark, num in remark_mapping.items():
            notes_file.write(f"{int_to_superscript(num)}: {remark}\n")

if __name__ == "__main__":
    input_csv = r"/Users/alessioivoycazzaniga/Documents/CEF NAUTICA/YAMAHA INVIATO A FRANCESCO VILLA 08-04-2025 CSV.csv"
    output_csv = r"/Users/alessioivoycazzaniga/Documents/CEF NAUTICA/YAMAHA INVIATO A FRANCESCO VILLA 08-04-2025 CSV_modified.csv"
    notes_txt = r"/Users/alessioivoycazzaniga/Documents/CEF NAUTICA/YAMAHA_INVIATO_NOTES.txt"
    process_csv(input_csv, output_csv, notes_txt)
    print("CSV processing complete. Modified file and notes generated.")