from requests import post
from sys import path
path.append('../')

from source_api import ApiControll
from source_api.interfaces import ApiControllInterface

def test_answer() :

    api_controll = ApiControll()

    # Instance 

    assert isinstance(api_controll, ApiControllInterface)

    # Upload

    response = api_controll.upload('/home/emanuel/Música/Outros/Rap do The Last of Us 2 - SE EU TE PERDER  Ft Amanda Areia.mp3')

    assert type(response) == dict
    assert response['message'] == 'Audio uploaded successfully'