import psutil as ps


class PararModulo:
    """ Setup for Stopping Modules """

    def action(self):         
        if 'filho' in (p.name() for p in ps.process_iter()):
            try:
                for proc in ps.process_iter():
                    if 'filho' in proc.name():
                        proc.kill()
                        print('FINALIZANDO PID: [{}] (name: {})'.format(proc.pid, proc.name()))
                        print('FINALIZANDO PID: [{}] (parent: {})'.format(proc.pid, proc.parent()))
            except:
                print('Ocorreu um erro ao Finalizar o processo do modulo')
        else:
            print('Este Processo não está Ativo')