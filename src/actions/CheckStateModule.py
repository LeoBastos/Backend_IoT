import psutil
from src.classes.IoT import Modules
from src.actions.Iniciar import IniciarModulo

class StateModule:
    def action(self):
        if not 'filho' in (p.name() for p in psutil.process_iter()):
            print('O Estado do processo esta PARADO')
            print()
            print('Inicializando Modulo')
            modulo = Modules(IniciarModulo())
            modulo.make_action()
            
        else:
            print('O Estado do Processo esta ATIVO')
        