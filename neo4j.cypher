LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Alemusica/CSVer/main/JMP%202023%20csv%20struturato%20parziale%209%20JOHN%20DEER%20MAN%20MITSUBISHI.csv" AS row
FIELDTERMINATOR ','

// 1) Girante JMP
MERGE (jmpImp:Impeller {code: row.JMP})
  ON CREATE SET
    jmpImp.id = randomUUID(),
    jmpImp.createdAt = datetime(),
    jmpImp.name = row.JMP

// Azienda JMP
MERGE (jmpCompany:Company {name:"JMP"})
  ON CREATE SET
    jmpCompany.id = randomUUID(),
    jmpCompany.createdAt = datetime()

MERGE (jmpImp)-[impManu:MANUFACTURED_BY]->(jmpCompany)
  ON CREATE SET
    impManu.id = randomUUID(),
    impManu.createdAt = datetime()

// 2) Pompa JMP
MERGE (jmpPump:Pump {code: row.`JMP Pump Name`})
  ON CREATE SET
    jmpPump.id = randomUUID(),
    jmpPump.createdAt = datetime(),
    jmpPump.name = row.`JMP Pump Name`

MERGE (jmpPump)-[pumpManu:MANUFACTURED_BY]->(jmpCompany)
  ON CREATE SET
    pumpManu.id = randomUUID(),
    pumpManu.createdAt = datetime()

// Relazione: girante “JMP” -> FITS_IN -> pompa “JMP Pump Name”
MERGE (jmpImp)-[fits:FITS_IN]->(jmpPump)
  ON CREATE SET
    fits.id = randomUUID(),
    fits.createdAt = datetime()

////////////////////////////////////////////////////////////////////////
// 3) Motore (Engine)
////////////////////////////////////////////////////////////////////////
MERGE (engine:Engine {model: row.`Engine Model`})
  ON CREATE SET
    engine.id = randomUUID(),
    engine.createdAt = datetime(),
    engine.name = row.`Engine Model`

// Azienda “COMPANY” (es. "JOHN DEERE", "MAN", "MITSUBISHI", ecc.)
MERGE (comp:Company {name: toUpper(row.COMPANY)})
  ON CREATE SET
    comp.id = randomUUID(),
    comp.createdAt = datetime()

MERGE (engine)-[engManu:MANUFACTURED_BY]->(comp)
  ON CREATE SET
    engManu.id = randomUUID(),
    engManu.createdAt = datetime()

// Relazione: pompa JMP -> COMPATIBLE_WITH -> motore
MERGE (jmpPump)-[rcompat:COMPATIBLE_WITH]->(engine)
  ON CREATE SET
    rcompat.id = randomUUID(),
    rcompat.createdAt = datetime()

////////////////////////////////////////////////////////////////////////
// 4) Pompa “Pump P/N” (brand = row.COMPANY) + EQUIVALENCE
////////////////////////////////////////////////////////////////////////

// Se Pump P/N e` vuoto o "N/A", lo saltiamo
WITH row, jmpPump, engine, comp
WHERE NOT (row.`Pump P/N` IS NULL OR row.`Pump P/N` = "" OR toUpper(row.`Pump P/N`) = "N/A")

MERGE (compPump:Pump {code: row.`Pump P/N`})
  ON CREATE SET
    compPump.id = randomUUID(),
    compPump.createdAt = datetime(),
    compPump.name = row.`Pump P/N`

MERGE (compPump)-[pumpManu2:MANUFACTURED_BY]->(comp)
  ON CREATE SET
    pumpManu2.id = randomUUID(),
    pumpManu2.createdAt = datetime()

// compatibile con lo stesso motore
MERGE (compPump)-[compCw:COMPATIBLE_WITH]->(engine)
  ON CREATE SET
    compCw.id = randomUUID(),
    compCw.createdAt = datetime()

// EQUIVALENT_TO con la pompa JMP
MERGE (jmpPump)-[equiv:EQUIVALENT_TO]-(compPump)
  ON CREATE SET
    equiv.id = randomUUID(),
    equiv.createdAt = datetime();