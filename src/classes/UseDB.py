from typing import Type
from src.Interfaces import database

class UseDatabase:
    """ Injection Dependency with Database: Type[database]"""

    def __init__(self, database: Type[database]):
        self.database = database

        def select_db(self):
            self.database.select()

        def insert_db(self):
            self.database.insert()
        
        def update_db(self):
            self.database.update()
        
        def delete_db(self):
            self.database.delete()