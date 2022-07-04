from abc import ABC, abstractmethod
from typing import Dict

class ApiControllInterface(ABC) :
    @abstractmethod
    def __init__(self) -> None:
        """
            Init

        Raises:
            NotImplementedError: NotImplementedError
        """

        self.__endpoint : str = 'endpoint'
        self.private__start_api()
        raise NotImplementedError

    @abstractmethod
    def private__start_api(self) -> None :
        """
        Private method, start the api

        Raises:
            NotImplementedError: NotImplementedError
        """

        raise NotImplementedError
    
    @abstractmethod
    def upload(self, file_path : str) -> Dict[str, str] :
        """
        Upload a file

        Args:
            file_path (str): The path to the file

        Raises:
            NotImplementedError: NotImplementedError

        Returns:
            Dict[str, str]: {
                'message': 'Message',
                'hash' : 'Hash'
            }
        """        

        raise NotImplementedError

    @abstractmethod
    def get_status(self, hash : str) -> Dict[str, str] :
        """
        Get a conversion file status

        Args:
            hash (str): Hash provide by upload

        Raises:
            NotImplementedError: NotImplementedError

        Returns:
            Dict[str, str]: {
                'status' : Bool
            }
        """        

        raise NotImplementedError
    
    @abstractmethod
    def get_file(self, hash : str) -> Dict[str, str] :
        """
        Get file

        Args:
            hash (str): Hash provide by upload

        Raises:
            NotImplementedError: NotImplementedError

        Returns:
            Dict[str, str]: {
                'audio' : 'Audio path in the server', 
                'filename' : 'Filename audio'
            }
        """  
      
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, hash : str) -> None:
        """Delete file on server

        Args:
            hash (str): Hash provide by upload

        Raises:
            NotImplementedError: NotImplementedError
        """        
        raise NotImplementedError()