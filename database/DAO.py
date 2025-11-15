from database.DB_connect import DBConnect

class DAO:
    def __init__(self):
        # carico tutte le parole al momento dell'inizializzazione
        self.parole = self._load_all_words()

    def _load_all_words(self):
        """
        Legge il database una sola volta e salva le parole in un set
        per ricerche O(1).
        """
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        query = "SELECT parola FROM parola"  # <-- modifica se la tabella ha nome diverso

        cursor.execute(query)
        results = cursor.fetchall()

        # creo un set per ricerche velocissime
        parole_set = {row[0] for row in results}

        cursor.close()
        conn.close()

        return parole_set

    def parola_valida(self, p):
        """
        Restituisce True se la parola è presente nel database,
        False altrimenti.
        """
        return p in self.parole

    def get_all_words(self):
        """
        Restituisce tutte le parole caricate (per debug o usi vari)
        """
        return self.parole
