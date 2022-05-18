from abc import ABC, abstractclassmethod
from typing import Union, Tuple

class ScanWindowInterface(ABC) :
    @abstractclassmethod
    def extract_qr(cls, path_to_image : str) -> Union[Tuple[str], Tuple[bytes]] :
        raise NotImplementedError()
        raise Exception("No QR code found")