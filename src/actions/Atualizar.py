import os
import time
import psutil
import wget
from src.config.mypaths import path_modulo, url_update


class AtualizarModulo:  
    """ 
        Setup for Update Module 
        :Check if modulo is active, if True his kill the module
        :else - Proceding updating process
    """

    def action(self):        
        for proc in psutil.process_iter():
            if 'filho' in proc.name():
                proc.kill()
            else:       
                os.rename(path_modulo + 'filho', path_modulo + 'filho_old')
                print('Modulo Antigo Renomeado com _Old...')
                time.sleep(2)
                print()
                print('Baixando atualização..')                
                url = url_update
                wget.download(url, path_modulo)
                print('Aguardando Download....')
                print('Download Finalizado')
                print()
                print('Renomeando novo Modulo para filho')
                os.rename(path_modulo + 'yh7pjwdy', path_modulo + 'filho')
                time.sleep(2)
                print('Colocando permissão para Execução')
                os.system(path_modulo + 'chmod u+x filho')
                