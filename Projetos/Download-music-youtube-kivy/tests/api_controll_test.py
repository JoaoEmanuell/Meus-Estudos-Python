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

    hash : str = response['hash']

    # Status

    sleep(3)

    response = api_controll.get_status(hash)

    assert type(response) == dict
    assert type(response['status']) == bool
    assert response['status'] == False

    # Get file

    response = api_controll.get_file(hash)

    assert type(response) == dict
    assert type(response['filename']) == str
    assert response['filename'] == 'Rap_do_The_Last_of_Us_2_-_SE_EU_TE_PERDER_Ft_Amanda_Areia.mp3'

    # Hash verification 
    
    audio = str(response['audio']).rsplit('/')[-1]
    assert audio[0:8] == hash[0:8]
