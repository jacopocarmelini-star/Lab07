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
    def estrai_artefatti(self):
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM artefatto"""
        cursor.execute(query)
        lista_artefatti = cursor.fetchall()
        cursor.close()
        cnx.close()
        return lista_artefatti

    def estrai_epoche(self):
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """SELECT epoche
                    FROM artefatto  """

