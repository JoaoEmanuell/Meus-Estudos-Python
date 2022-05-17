from abc import ABC, abstractmethod
from typing import Union
from qrcode.image.base import BaseImage
from qrcode.image.pil import PilImage

class GenerateWindowInterface(ABC) : 
    """GenerateWindowInterface

    Args:
        ABC (_type_): _description_
    """    
    @abstractmethod
    def __init__(self, url : str) -> None:
        """Init

        Args:
            url (str): Url to generate QR code
        """        
        raise NotImplementedError()

    @abstractmethod
    def generate_qrcode(self) -> Union[PilImage, BaseImage]:
        """Generate QR code

        Returns:
            Union[PilImage, BaseImage]: QR code image
        """        
        raise NotImplementedError()

    @abstractmethod
    def save_image(self, image : Union[PilImage, BaseImage], path : str) -> None:
        """Save QR code image

        Args:
            image (Union[PilImage, BaseImage]): QR code image
            path (str): Path to save image

        Raises:
            ValueError: If file extension is invalid (not .png)
        """        
        raise NotImplementedError()
        raise ValueError