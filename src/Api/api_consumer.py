import requests
from requests import Request
from typing import Type
# from collections import namedtuple



class ApiConsumer:    
    """ Config Class Api  """
    # def __init__(self) -> None:
    #     self.get_modulos_id_response = namedtuple('Get_Data_Api', 'response')
    
    def get_modulos_id(self, id: str) -> any:        
        """ Get data by Id from Api"""

        req = requests.Request(
            method='GET',
            url='http://127.0.0.1:8000/' + id,            
        )

        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)

        return response.json()

        # return self.get_modulos_id_response(response=response.json())


    def get_modulos(self) -> any:
        """ Get all data from Api  """
       
        req = requests.Request(
            method='GET',
            url='http://127.0.0.1:8000/',            
        )

        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)

        return response.json()
        # return self.get_modulos_id_response(response=response.json())
        

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        """ 
            Prepare Session and send Http Request      
            :param - req_prepared: Request Object with all params
            :response - Http response raw
        """
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response