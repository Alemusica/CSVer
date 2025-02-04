import csv
import re

def clean_application(app_str):
    """
    Rimuove spazi e virgolette esterne, e converte eventuali virgole usate come separatore decimale in punto.
    Ad esempio: "4,3L" -> "4.3L"
    """
    # Rimuove spazi iniziali/finali e virgolette
    app_str = app_str.strip().strip('"')
    # Sostituisce il separatore decimale (virgola) con il punto, ad esempio "4,3L" -> "4.3L"
    app_str = re.sub(r'(\d),(\d)', r'\1.\2', app_str)
    return app_str

def split_applications(app_str):
    """
    Divide la stringa in token (usando la virgola come separatore) e, se il primo token contiene un prefisso numerico,
    lo utilizza per "integrare" i token successivi che sono solo suffissi (cioè non iniziano con un numero).
    """
    app_str = clean_application(app_str)
    # Dividi per virgola e rimuovi spazi in eccesso
    tokens = [t.strip() for t in app_str.split(',') if t.strip()]
    if not tokens:
        return []
    
    # Proviamo a estrarre un prefisso numerico dal primo token
    # Si assume che il primo token sia completo (ad es. "4.3L") e che contenga la parte numerica all'inizio.
    m = re.match(r'(\d+\.\d+)', tokens[0])
    prefix = m.group(1) if m else ""
    
    result = []
    for token in tokens:
        # Se il token non inizia con una cifra e abbiamo un prefisso, lo completiamo aggiungendo il prefisso.
        if prefix and not re.match(r'\d', token):
            result.append(prefix + token)
        else:
            result.append(token)
    return result

def process_csv(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as csv_in, \
         open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
        
        reader = csv.DictReader(csv_in)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Estrae il campo Applications e lo suddivide
            apps = split_applications(row['Applications'])
            # Per ogni token ottenuto, scrive una riga nuova con lo stesso Id (e gli altri campi invariati)
            for app in apps:
                new_row = row.copy()
                new_row['Applications'] = app
                writer.writerow(new_row)

if __name__ == '__main__':
    # Imposta il percorso dei file (modifica se necessario)
    input_csv = 'Unified_Marine_Components_Database_VOLVO_PENTA_output.csv'
    output_csv = 'Unified_Marine_Components_Database_VOLVO_PENTA_expanded.csv'
    process_csv(input_csv, output_csv)