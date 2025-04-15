import os
import glob
import io
import csv
import pandas as pd

# Directory contenente i file CSV
directory = '/Users/alessioivoycazzaniga/CSVer/split_databases'
pattern = os.path.join(directory, '*.csv')
csv_files = glob.glob(pattern)

for file_path in csv_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Rimuove le righe che iniziano con "//"
        filtered_lines = [line for line in lines if not line.lstrip().startswith('//')]
        csv_data = ''.join(filtered_lines)
        
        # Usa csv.reader per leggere tutte le righe
        reader = csv.reader(io.StringIO(csv_data))
        rows = list(reader)
        if not rows:
            print(f"Nessun dato in {file_path}")
            continue
        header = rows[0]
        
        # Se la prima riga dati (se presente) ha un numero diverso di colonne,
        # assumiamo che ci siano colonne extra e le aggiungiamo all'header.
        if len(rows) > 1 and len(rows[1]) != len(header):
            num_extra = len(rows[1]) - len(header)
            header = header + [f'Extra{i+1}' for i in range(num_extra)]
            df = pd.DataFrame(rows[1:], columns=header)
        else:
            df = pd.DataFrame(rows[1:], columns=header)
    except Exception as e:
        print(f"Errore nella lettura di {file_path}: {e}")
        continue

    if 'Id' in df.columns:
        df = df.drop(columns=['Id'])
        # Salva il file CSV aggiornato mantenendo lo stesso nome (usa quoting minimo per preservare le virgole nei campi)
        df.to_csv(file_path, index=False, quoting=1)
        print(f"Colonna 'Id' rimossa da {file_path}")
    else:
        print(f"Colonna 'Id' non presente in {file_path}")