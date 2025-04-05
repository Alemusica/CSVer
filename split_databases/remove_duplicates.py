import pandas as pd
import csv

# Percorsi dei file
input_file = "/Users/alessioivoycazzaniga/CSVer/split_databases/output.csv"
output_file = "/Users/alessioivoycazzaniga/CSVer/split_databases/output_deduplicated.csv"

try:
    # Carica il CSV usando il delimitatore tab
    df = pd.read_csv(input_file, delimiter='\t', on_bad_lines='skip',
                     engine='python', quoting=csv.QUOTE_NONE, escapechar='\\')
except pd.errors.ParserError as e:
    print(f"Errore durante la lettura del file CSV: {e}")
    exit(1)

# Rimuovi i duplicati basati sul campo 'Applications', mantenendo il primo record
df_cleaned = df.drop_duplicates(subset='Applications', keep='first')

# Salva il risultato in un nuovo file CSV mantenendo il delimitatore tab
df_cleaned.to_csv(output_file, index=False, sep='\t')

print(f"File senza duplicati salvato come {output_file}")
