import sys
sys.path.append('../')
from source.image_convert import ImageConvert


def test_answer():
    # Test the class
    Image = ImageConvert('/home/emanuel/Imagens/Captura de tela de 2022-02-11 18-18-05.png', 'jpg')
    assert Image.convert_image() == 0