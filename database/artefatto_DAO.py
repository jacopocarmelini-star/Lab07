from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto


"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def estrai_epoche(self):
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """SELECT DISTINCT epoca
                    FROM artefatto"""

        cursor.execute(query)
        risultati = cursor.fetchall()
        lista_epoche = []
        for riga in risultati:
            epoca = riga[0]
            lista_epoche.append(epoca)
        cursor.close()
        cnx.close()
        return lista_epoche

    def estrai_artefatti(self, id_museo, epoca):
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM artefatto WHERE (%s IS NULL OR id_museo=%s)  
                        AND (%s IS NULL OR epoca=%s)"""
        cursor.execute(query, (id_museo,id_museo, epoca, epoca))

        risultati = cursor.fetchall()
        lista_artefatti = []

        for (id, nome, tipologia, epoca, id_museo) in risultati:
            artefatto = Artefatto(id, nome, tipologia, epoca, id_museo)
            lista_artefatti.append(artefatto)
        cursor.close()
        cnx.close()
        return lista_artefatti


