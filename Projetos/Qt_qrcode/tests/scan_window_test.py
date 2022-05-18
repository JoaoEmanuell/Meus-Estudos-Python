from sys import path
path.append('../')

from source.windows.scan_window import ScanWindow
from source.windows.interfaces import ScanWindowInterface

def test_answer():
    image = 'test.png'
    assert type(image) == str

    assert issubclass(ScanWindow, ScanWindowInterface)

    images = ScanWindow.extract_qr(image)

    assert type(images) == tuple
    
    assert len(images) == 1

    assert images[0] == 'https://www.google.com'