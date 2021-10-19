from src.Api.api_consumer import ApiConsumer
from src.classes.IoT import Modules
from src.actions.Atualizar import AtualizarModulo
from src.actions.Parar import PararModulo
import time

class VersionModule:
    def action(self):
        get_version = ApiConsumer()
        response = get_version.get_modulos_id('1')

        if response['Modulos'][0]['version'] == 3:
            print(f'Você já Possui a ultima Versão!')
            time.sleep(2)
        else:
            modulo = Modules(PararModulo())
            modulo.make_action()
            print('Parando o Modulo Para Atualização')
            time.sleep(2)
            print('Iniciando Atualização')
            modulo1 = Modules(AtualizarModulo())
            modulo1.make_action()