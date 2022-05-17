from typing import Union
from PIL.Image import Image
from qrcode.image.base import BaseImage


from ..interfaces import GenerateWindowInterface

class GenerateWindow(GenerateWindowInterface) :

    def __init__(self, url: str) -> None:
        self.__url = url

    def generate_qrcode(self) -> Union(Image, BaseImage):
        from qrcode import make
        return make(self.__url)

    def save_image(self, image: Union(Image, BaseImage), path: str) -> None:
        image.save(path)