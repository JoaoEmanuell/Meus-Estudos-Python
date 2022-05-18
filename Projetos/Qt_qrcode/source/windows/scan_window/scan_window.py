from ..interfaces import ScanWindowInterface
from typing import Union, Tuple

class ScanWindow(ScanWindowInterface) :
    @classmethod
    def extract_qr(cls, path_to_image : str) -> Union[Tuple[str], Tuple[bytes]] :

        from PIL import Image
        from pyzbar.pyzbar import decode

        with Image.open(path_to_image) as image :
            images_decode = (* decode(image), )

        if len(images_decode) == 0 :
            raise Exception("No QR code found")

        images = (
            * [image for image.data in images_decode], 
        )

        return images