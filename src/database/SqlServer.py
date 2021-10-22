from src.Interfaces import database
from src.config import CONN_STR
import pyodbc
import logging


logger = logging.getLogger(__name__)
conn = pyodbc.connect(CONN_STR)
cursor = conn.cursor()

class Database1(database):
    """ Configuration of SQL Server in project  """
    
    def select(self):
        cursor.execute('SELECT * FROM MODULO')
        for row in cursor:
            print('row = %r' % (row,))

    def insert(self, name, version, url, isActive):
        query = 'INSERT INTO MODULO (name, version, url, isActive) VALUES (?, ?, ?, ?)'
        cursor.execute(query, (name, version, url, isActive))
        conn.commit()
        logger.info("Dados Inseridos no Sql")
        print('Inserido com Sucesso!')

    def update(self, name, version, url, isActive, idModulo):
        query = 'UPDATE MODULO SET name=?, version=?, url=?, isActive=? WHERE idModulo=?'
        cursor.execute(query, (name, version, url, isActive, idModulo))
        conn.commit()
        print('Atualizado com Sucesso!')

    def delete(self, idModulo):
        query = 'DELETE FROM MODULO WHERE idModulo=?'
        cursor.execute(query, (idModulo,))
        conn.commit()
        print('Excluido com Sucesso!')


# insert("PC-Count-6", 1, "http://127.0.0.1:8000/8478F87E-6E34-47C2-B378-07427751D059", True);
