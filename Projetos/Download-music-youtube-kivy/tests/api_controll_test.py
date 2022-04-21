from sys import path
path.append('../')

from source_api import ApiControll
from source_api.interfaces import ApiControllInterface

def test_answer() :

    api_controll = ApiControll()

    # Instance 

    assert isinstance(api_controll, ApiControllInterface)