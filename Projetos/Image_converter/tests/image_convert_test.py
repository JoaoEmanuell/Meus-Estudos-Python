import sys
sys.path.append('../')
from source.image_convert import ImageConvert


def test_answer():
    # Test the class
    Image = ImageConvert('/home/emanuel/Imagens/Captura de tela de 2022-01-30 16-24-40.png', 'jpg')
    assert Image.verfiy_if_converted_image_directory_exists() == None
    assert Image.verify_extension_file() == 'png'
    assert Image.convert_image() == 0