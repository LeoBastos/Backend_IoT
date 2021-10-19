from abc import ABC, abstractclassmethod

class database(ABC):
    """ Interface configuration Methods of all databases used in the project  """

    @abstractclassmethod
    def select():
        raise Exception('Você deve implementar o metodo: select')    

    @abstractclassmethod
    def insert():
        raise Exception('Você deve implementar o metodo: insert')

    @abstractclassmethod
    def update():
        raise Exception('Você deve implementar o metodo: update')

    @abstractclassmethod
    def delete():
        raise Exception('Você deve implementar o metodo: delete')

