from time import sleep
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

    # Status

    sleep(3)

    response = api_controll.get_status(response['hash'])

    assert type(response) == dict
    assert type(response['status']) == bool
    assert response['status'] == False
