import os
from dotenv import load_dotenv

load_dotenv()

CONN_STR = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=criareDB;UID=sa;PWD=-00388ut32Leo'

database_config = {    
    "driver": os.getenv('DRIVER'),
    "server": os.getenv('SERVER'),
    "database": os.getenv('DATABASE'),    
    "user": os.getenv('UID'),
    "password": os.getenv('PWD')
}

