import os
from datetime import datetime
import threading
import schedule
import time
from src.classes.IoT import Modules
from src.classes.UseDB import UseDatabase
from src.actions.CheckVersion import VersionModule
from src.actions.CheckStateModule import StateModule
from src.database.SqlServer import Database1
from src.Api.api_consumer import ApiConsumer



start_time = datetime.now().replace(microsecond=0)

def main():
    print('Sistema Iniciado')
    print()
    time.sleep(1)    
    
    #Faz Requisição da Api
    get_data_from_api = ApiConsumer()
    response = get_data_from_api.get_modulos_id('1')
    print(response)    
    print()
    time.sleep(2)

    #Insere no banco o Resultado da Requisição da Api 
    #Database1 = SqlServer / database2 = Sqlite
    mydb = UseDatabase(Database1())
    print('Inserindo dados da Api...')
    mydb.database.insert(response['Modulos'][0]['name'], response['Modulos'][0]['version'], 
                         response['Modulos'][0]['url'], response['Modulos'][0]['isActive'])
    time.sleep(2)
    print()

    #Checando a Versão do Modulo para Updates
    print('Checa a Versão do Modulo para Updates')
    check_version = Modules(VersionModule())        
    check_version.make_action()    
    time.sleep(2)
    print()

    #Verifica o Estado do Modulo: Ativo ou Parado
    #Caso Modulo esteja parado ele irá iniciar automáticamente
    print('Verificando o estado do Modulo')
    state_modulo = Modules(StateModule())
    state_modulo.make_action()
    time.sleep(2)
    print()


    CPU_Pct = str(round(float(
        os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),
        2))
    
    print("Uso de CPU = " + CPU_Pct)

    time_elapsed = datetime.now().replace(microsecond=0) - start_time
    
    print(time_elapsed)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    job_thread.join()


schedule.every(10).seconds.do(main)

while 1:
    schedule.run_pending()
    time.sleep(1)

