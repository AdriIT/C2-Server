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
    query = f"Delete from {tabella}"  # Modifica la query in base al tuo schema di tabella
    cursor.execute(query)

    # Commit delle modifiche
    conn.commit()

  

    # Chiusura della connessione
    conn.close()

#Esempio di utilizzo
database_path = 'db.sqlite3'
tabella = 'library_device'
dati_da_inserire = ('kali', '123.123.123.123', "00-50-FC-A0-67-2C", "RM")

#Chiamata alla funzione per inserire dati
inserisci_dati(database_path, tabella, dati_da_inserire)
print("cleared")
