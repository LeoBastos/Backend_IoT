import subprocess
import psutil as ps


class IniciarModulo:
    """ Setup for Starting Module """

    program = None
    path_modulo = "/home/leonardo/Área de Trabalho/exec/dist/filho/filho"

    def action(self):              
        if not 'filho' in (p.name() for p in ps.process_iter()):
            try:                 
                self.program = subprocess.Popen(self.path_modulo)
                for proc in ps.process_iter():
                    if 'filho' == proc.name():
                        print('PID: [{}] (name: {})'.format(proc.pid, proc.name()))
                        print('PID: [{}] (parent: {})'.format(proc.pid, proc.parent()))
            except:                
                print('Ocorreu um erro ao iniciar o processo do modulo')
        else:
            print('já existe um processo ativo')

