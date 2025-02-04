import csv
from collections import defaultdict

def expand_slash(token):
    """
    Se il token contiene un trattino e una barra (es. "250A/SP-A/MT"),
    suddivide la parte dopo il trattino sui caratteri "/" e restituisce
    una lista di valori in cui lo slash è sostituito dal trattino.
    Ad esempio, "250A/SP-A/MT" -> ["250A-SP-A", "250A-SP-MT"].
    Se non c'è la barra, restituisce [token].
    """
    if '-' in token and '/' in token:
        prefix, suffix_group = token.split('-', 1)
        suffixes = [s.strip() for s in suffix_group.split('/') if s.strip() != ""]
        return [f"{prefix}-{s}" for s in suffixes]
    else:
        return [token]

def merge_tokens(tokens):
    """
    Effettua il merging dei token per unire eventuali token “di suffisso”
    che sono separati da virgola.
    Regola: se un token (non il primo) è lungo al massimo 2 caratteri e
    composto solo da lettere, viene unito al token precedente tramite un trattino.
    Ad esempio, ["AQ231A", "B"] -> ["AQ231A-B"].
    """
    merged = []
    current = None
    for token in tokens:
        # Se il token è vuoto, lo aggiungiamo così com'è
        if token == "":
            merged.append(token)
            continue
        if current is None:
            current = token
        else:
            if len(token) <= 2 and token.isalpha():
                current = f"{current}-{token}"
            else:
                merged.append(current)
                current = token
    if current is not None:
        merged.append(current)
    return merged

def clean_and_expand_applications(app_str):
    """
    Processa il campo Applications applicando le seguenti operazioni:
      1. Split sulla virgola e stripping degli spazi.
      2. Se il primo token contiene una virgola (es. "5,7L"), viene trattato
         come un caso speciale: viene convertito in "5.7L" e per ogni token
         successivo (non vuoto) viene prodotto il valore ottenuto concatenando
         il prefisso numerico (ossia il primo token con la virgola sostituita e senza l'ultima lettera)
         con il token.
         Ad esempio: ["5,7L", "GI", "GIL", ...] → ["5.7L", "5.7GI", "5.7GIL", ...].
      3. Altrimenti, applica la funzione merge_tokens.
      4. Infine, per ogni token, se contiene "/" lo espande tramite expand_slash.
    Restituisce la lista finale dei valori.
    """
    # 1. Split sulla virgola e stripping
    raw_tokens = [token.strip() for token in app_str.split(',')]
    
    # Caso speciale: se il primo token contiene una virgola, ad es. "5,7L"
    if raw_tokens and (',' in raw_tokens[0]):
        # Sostituisci la virgola con il punto nel primo token
        prefix_full = raw_tokens[0].replace(',', '.')
        # Se il primo token termina con una lettera, definiamo il prefisso numerico rimuovendo l'ultima lettera
        if prefix_full and prefix_full[-1].isalpha():
            prefix_number = prefix_full[:-1]
        else:
            prefix_number = prefix_full
        # Costruiamo la lista speciale:
        # Il primo output è il prefisso completo, poi per ogni token successivo (non vuoto)
        # creiamo "prefix_number" + token.
        special_tokens = [prefix_full] + [prefix_number + token for token in raw_tokens[1:] if token != ""]
        tokens = special_tokens
    else:
        tokens = raw_tokens
    
    # Applica il merging euristico
    merged_tokens = merge_tokens(tokens)
    
    # Espansione dei token che contengono "/"
    final_tokens = []
    for token in merged_tokens:
        if '/' in token:
            final_tokens.extend(expand_slash(token))
        else:
            final_tokens.append(token)
    return final_tokens

def group_rows_by_id(rows):
    """
    Raggruppa le righe in base al campo 'Id'.
    Restituisce un dizionario con chiave = Id e valore = lista di righe.
    """
    groups = defaultdict(list)
    for row in rows:
        groups[row['Id']].append(row)
    return groups

def main():
    input_file = 'Unified_Marine_Components_Database_VOLVO_PENTA.csv'
    output_file = 'Unified_Marine_Components_Database_VOLVO_PENTA_output.csv'
    
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
    
    groups = group_rows_by_id(rows)
    
    out_rows = []
    for id_val, group in groups.items():
        # Raccogli tutti i valori del campo Applications del gruppo
        all_apps = [row['Applications'].strip() for row in group]
        # Esegui la pulizia ed espansione sul gruppo (considerando l'ordine)
        merged = merge_tokens(all_apps)
        final_apps = []
        for token in merged:
            if '/' in token:
                final_apps.extend(expand_slash(token))
            else:
                final_apps.append(token)
        
        # Usa la prima riga del gruppo per le altre colonne
        base_row = group[0].copy()
        for app in final_apps:
            new_row = base_row.copy()
            new_row['Applications'] = app
            out_rows.append(new_row)
    
    fieldnames = rows[0].keys()
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)
    
    print(f"Elaborazione completata. Output salvato in {output_file}")

if __name__ == "__main__":
    main()