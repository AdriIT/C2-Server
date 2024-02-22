import sqlite3

def inserisci_dati(database_path, tabella, dati):
    """
    Inserisce dati in una tabella SQLite.

    :param database_path: Percorso del file del database SQLite.
    :param tabella: Nome della tabella in cui inserire i dati.
    :param dati: Dati da inserire, deve essere una tupla.
    """
    # Connessione al database
    conn = sqlite3.connect(database_path)

    # Creazione di un cursore
    cursor = conn.cursor()

    # Esecuzione della query di inserimento
    query = f"INSERT or ignore INTO {tabella} VALUES (NULL, ?, ?, ?, ?, ?, ?)"  # Modifica la query in base al tuo schema di tabella
    cursor.execute(query, dati)
    # Commit delle modifiche
    conn.commit()

    print("CHANGES:")
    for row in cursor.execute(f"select * from {tabella}"):
        print(row)

    # Chiusura della connessione
    conn.close()

#Esempio di utilizzo
database_path = 'db.sqlite3'
tabella = 'library_device'

for i in range(0, 3):
    dati_da_inserire = ('test'+str(i), '11'+str(i)+'.123.123.123', 8888, 'kali', "10-50-12-A0-17-"+str(i)+"C", "RM")
    #Username-IP-MAC must be UNIQUE or else it will only increase the id counter

    #Chiamata alla funzione per inserire dati
    inserisci_dati(database_path, tabella, dati_da_inserire)



