from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    def estrai_musei(self):
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """SELECT id, nome, tipologia
                    FROM museo"""
        cursor.execute(query)
        risultati = cursor.fetchall()
        lista_musei = []
        for riga in risultati:
            id_museo, nome, tipologia = riga
            museo = Museo(id_museo, nome, None)
            lista_musei.append(museo)

        cursor.close()
        cnx.close()
        return lista_musei
