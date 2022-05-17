from abc import ABC, abstractmethod
from typing import Union
from qrcode.image.base import BaseImage
from qrcode.image.pil import PilImage

class GenerateWindowInterface(ABC) : 
    @abstractmethod
    def __init__(self, url : str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def generate_qrcode(self) -> Union[PilImage, BaseImage]:
        raise NotImplementedError()

    @abstractmethod
    def save_image(self, image : Union[PilImage, BaseImage], path : str) -> None:
        raise NotImplementedError()