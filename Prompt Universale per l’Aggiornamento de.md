Prompt Universale per l’Aggiornamento del Catalogo CEF Marine
Contesto e Obiettivo:
* Scopo: Aggiornare il catalogo CEF Marine (attualmente fermo al 2018) con le nuove applicazioni di giranti-soffietti (impellers) per motori [BRAND] (da sostituire con il marchio desiderato) dal 2018 in avanti.
* Focus: Considerare il periodo di 2 anni per la scadenza della garanzia OEM (quindi a fino al  2023 circa).
* Obiettivo specifico:
    * Identificare possibili nuovi kit service, giranti e pompe non presenti a catalogo.
    * Verificare se tali elementi siano riconducibili a codici CEF esistenti oppure, in assenza, etichettarli come “DA SVILUPPARE”.
Fonti e Metodologia:
* Raccolta Dati:
    * Estrarre informazioni da fonti affidabili online, tra cui eBay, siti di produttori (Osculati, Recmar/Recambios, Sierra, Jabsco, Sherwood, JMP e altri se ritenuto utile) e altre risorse affidabili.
    * Utilizzare tecniche di web scraping per recuperare dati, assicurando un’analisi accurata per il recupero, l’ordinamento e l’analisi delle informazioni.
* Algoritmo di Propagazione:
    * Impiegare un algoritmo di propagazione per eseguire "salti" tra le liste, collegando i riferimenti ai codici sulla base dei dati estrapolati dal web.
    * Tale algoritmo è cruciale per verificare cross references tra kit, pompe, giranti e motori, facilitando il recupero e l’aggiornamento dei codici CEF.
Struttura della Tabella Finale (proposta):
ID	Applications (motore / potenza / specifiche)	CEF (codice CEF, se esistente)	NBR Version (se applicabile)	Kit (codice kit, se esistente)	Remarks (note su compatibilità, differenze, anno, eventuali richiami)	Company (es. [BRAND])	Tipologia Applicazione (es. Outboard_Engines)	Note Esplicative (approfondimenti, fonti, link, scoperte particolari)
Istruzioni Dettagliate:
1. Identificazione dei Nuovi Motori:
    * Individuare i motori [BRAND] dal 2018 a oggi (es. BF100, BF150, BF200, BF250, BF serie successive, ecc.) verificando l’eventuale disponibilità di kit/giranti aftermarket.
2. Confronto con il Catalogo Esistente:
    * Confrontare i nuovi dati con i codici CEF già presenti (ad es. 500327, 500328, 500339, 500337, 500338, 500347, 500348, 500343, 500391, 500301N, ecc.) e con i kit/impeller OEM.
3. Cross References e Propagazione:
    * Per ogni applicazione o motore trovato, associare eventuali codici provenienti da fonti come Osculati, Recmar, Sierra, Jabsco, Sherwood, JMP e altre.
    * Utilizzare l'algoritmo di propagazione per eseguire salti tra le liste: collegare i codici incrociati basandosi sui dati "scrapati" dal web, ordinandoli e analizzandoli per facilitare l'identificazione dei riferimenti mancanti.
4. Verifica e Aggiornamento:
    * Se esiste una corrispondenza con un codice CEF esistente, riportare tale corrispondenza nella tabella.
    * Se non esiste, etichettare la voce come “DA SVILUPPARE”.
5. Note Esplicative:
    * Aggiungere una colonna o una sezione finale in cui indicare:
        * La fonte della cross reference (link, nome del sito, ecc.)
        * L’anno di introduzione del motore o del kit
        * Eventuali osservazioni relative a dati contraddittori o incompleti (es. “Necessaria verifica ulteriore”).
6. Report Finale:
    * Oltre alla tabella, fornire un breve report descrittivo che evidenzi:
        * Le nuove applicazioni individuate
        * Le differenze riscontrate rispetto al catalogo CEF fermo al 2018
        * Le voci che necessitano di approfondimento o verifica ulteriore

Istruzioni per l’Utilizzo:
* Sostituire il placeholder [BRAND] con il nome del marchio da ricercare (es. Honda, JMC, ecc.).
* Assicurarsi che l’algoritmo di propagazione venga applicato in maniera coerente per gestire i salti tra le diverse liste di dati e per verificare la completezza dei codici incrociati.
* Verificare e integrare i dati provenienti da più fonti per garantire un aggiornamento accurato e affidabile del catalogo.

Questa struttura consente di avere un prompt universale e flessibile, che potrà essere facilmente adattato per diversi marchi e applicazioni, garantendo un aggiornamento sistematico e accurato del catalogo basato su dati web e cross references.
