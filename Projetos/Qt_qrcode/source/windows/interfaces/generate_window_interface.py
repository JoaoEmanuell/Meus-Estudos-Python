from abc import ABC, abstractmethod
from typing import Type
from PIL.Image import Image

class GenerateWindowInterface(ABC) : 
    @abstractmethod
    def __init__(self, url : str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def generate_qrcode(self) -> Type[Image]:
        raise NotImplementedError()

    @abstractmethod
    def save_image(self, image : Type[Image], path : str) -> None:
        raise NotImplementedError()