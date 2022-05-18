from abc import ABC, abstractclassmethod
from typing import Union

class ScanWindowInterface(ABC) :
    @abstractclassmethod
    def extract_qr(cls, path_to_image : str) -> Union[str, bytes] :
        raise NotImplementedError()