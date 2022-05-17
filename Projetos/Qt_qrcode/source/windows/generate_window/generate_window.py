from typing import Union
from qrcode.image.base import BaseImage
from qrcode.image.pil import PilImage

from ..interfaces import GenerateWindowInterface

class GenerateWindow(GenerateWindowInterface) :

    def __init__(self, url: str) -> None:
        self.__url = url

    def generate_qrcode(self) -> Union[PilImage, BaseImage]:
        from qrcode import make
        return make(self.__url)

    def save_image(self, image: Union[PilImage, BaseImage], path: str) -> None:
        image.save(path)