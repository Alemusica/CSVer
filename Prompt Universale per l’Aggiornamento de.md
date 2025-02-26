Prompt Completo con Algoritmo di Ricerca e Propagazione
Obiettivo Principale
Aggiornare il catalogo CEF Marine (attualmente fermo al 2018) con le nuove applicazioni di giranti-soffietti (impellers) per motori [BRAND] (sostituire con il marchio desiderato) dal 2018 in avanti, considerando un periodo di 2 anni dopo la scadenza della garanzia OEM e focalizzandosi quindi sull’aftermarket.

Algoritmo di Ricerca Dettagliato
Ricerca dei Motori di Nuova Uscita

Individuare i motori [BRAND] lanciati dal [anno di inizio] fino a [anno attuale].
Per ciascun motore individuato, raccogliere le specifiche di base (potenza, modello, eventuali aggiornamenti di serie, ecc.).
Identificazione del Service Kit OEM

Per ogni nuovo motore trovato, identificare il relativo service kit OEM (se disponibile).
Dal service kit OEM, ricavare il part number OEM dell’Impeller (girante).
Se la girante non è inclusa o non identificabile, saltare al motore successivo.
Memorizzazione delle Caratteristiche Tecniche

Quando si individua il part number OEM dell’Impeller, raccogliere e salvare in variabili le sue dimensioni (diametro, altezza, foro centrale, ecc.) e il numero di pale (alette).
Questi dati serviranno in seguito per irrobustire le corrispondenze (cross references) e aiutare a scartare possibili errori.
Ricerca Parallela delle Alternative Aftermarket

A partire dai codici OEM (service kit e/o girante), eseguire ricerche parallele su vari siti e database aftermarket (eBay, Osculati, Recmar/Recambios, Sierra, Jabsco, Sherwood, JMP, ecc.).
Ogni sito fornirà cross references potenzialmente incomplete, che costituiranno la base per la propagazione.
Propagazione dei Codici (3-4 Iterazioni)

Per ciascun codice aftermarket o OEM emerso nei passaggi precedenti, avviare 3-4 iterazioni di sottoricerche:
Utilizzare i codici (o le denominazioni) trovati per cercare nuovi riferimenti su altri siti o nelle sezioni “cross reference” di ogni portale.
Anche se durante una di queste ricerche si individua subito il codice CEF, continuare le iterazioni per raccogliere ulteriori dati.
Lo scopo è creare un quadro completo di tutti i possibili equivalenti (kit, giranti, pompe, ecc.).
Aggregazione e Condensa dei Risultati

Al termine delle ricerche, accorpare tutti i risultati ottenuti dalle fasi di propagazione.
Confrontare le caratteristiche tecniche (dimensioni, numero di pale) per escludere eventuali false corrispondenze.
Stendere una tabella di equivalenza finale che includa:
Il motore (o i motori) di riferimento
I codici OEM (service kit/girante)
I codici aftermarket equivalenti (Osculati, Recmar, Sierra, ecc.)
Eventuale codice CEF se esistente
Segnalare con la dicitura “DA SVILUPPARE” i casi in cui non esiste ancora un codice CEF corrispondente.
Struttura della Tabella di Output (Esempio)
Id,Applications,Cef,NBR Version,Kit,Remarks,Company,Tipologia Appplicazione

ID: Numero progressivo o codice interno nuovo.
Applications: Modello motore (es. BF100, BF150) e specifiche principali.
CEF: Codice CEF (se presente), altrimenti “DA SVILUPPARE”.
NBR Version: Indicare se esiste versione in gomma nitrilica.
Kit: Codice kit di riferimento (se esiste).
Remarks: Note su compatibilità, differenze, anno di rilascio, eventuali richiami, ecc.
Company: Il marchio ricercato (es. Honda).
Tipologia: Es. Outboard_Engines, Inboard, Diesel, ecc.
Note Esplicative: Sezione per link alle fonti, cross reference aggiuntive, dimensioni salvate, ecc.
Istruzioni per l’Uso del Prompt
Sostituisci [BRAND] con il marchio da analizzare (es. Honda, Yamaha, ecc.).
Definisci il periodo temporale (es. dal 2018 a oggi).
Segui l’algoritmo passo dopo passo (dalla ricerca motori nuovi, all’estrazione di part number OEM, sino alle ricerche parallele e propagazioni multiple).
Concludi con la fase di aggregazione e condensa, generando la tabella riassuntiva e un breve report sulle differenze rispetto al catalogo CEF fermo al 2018, indicando:
Nuove applicazioni trovate
Cross references con altri marchi e codici
Voci “DA SVILUPPARE” ove manca il codice CEF
Eventuali necessità di ulteriori verifiche
Questa formulazione segue esattamente le fasi indicate (ricerca, identificazione service kit, part number girante, ricerca parallela, propagazione, aggregazione) e fornisce una struttura chiara per la presentazione dei risultati in tabella.






You said:
questa la struttura:
Id,Applications,Cef,NBR Version,Kit,Remarks,Company,Tipologia Appplicazione
ChatGPT said:
Ecco il prompt riformulato in modo chiaro e strutturato, con la struttura tabellare definita e il processo di ricerca dettagliato.

