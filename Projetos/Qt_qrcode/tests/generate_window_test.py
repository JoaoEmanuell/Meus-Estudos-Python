from re import A
from sys import path
path.append('../')

from qrcode.image.pil import PilImage
from qrcode.image.base import BaseImage

from source.windows.generate_window import GenerateWindow
from source.windows.interfaces import GenerateWindowInterface

def test_answer():
    url = 'https://www.google.com'
    assert type(url) == str

    window = GenerateWindow(url)

    assert issubclass(window.__class__, GenerateWindowInterface)

    image = window.generate_qrcode()

    assert type(image) == PilImage or type(image) == BaseImage

    window.save_image(image, 'test.png')