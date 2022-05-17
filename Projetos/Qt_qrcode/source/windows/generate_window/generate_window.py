from typing import Type
from PIL.Image import Image

from ..interfaces import GenerateWindowInterface

class GenerateWindow(GenerateWindowInterface) :

    def __init__(self, url: str) -> None:
        self.__url = url

    def generate_qrcode(self) -> Type[Image]:
        from qrcode import make
        return make(self.__url)

    def save_image(self, image: Type[Image], path: str) -> None:
        image.save(path)