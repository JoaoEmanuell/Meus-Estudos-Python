from abc import ABC, abstractmethod
from typing import Union
from PIL.Image import Image
from qrcode.image.base import BaseImage

class GenerateWindowInterface(ABC) : 
    @abstractmethod
    def __init__(self, url : str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def generate_qrcode(self) -> Union(Image, BaseImage):
        raise NotImplementedError()

    @abstractmethod
    def save_image(self, image : Union(Image, BaseImage), path : str) -> None:
        raise NotImplementedError()