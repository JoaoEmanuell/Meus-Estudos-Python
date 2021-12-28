from PIL import Image
from pathlib import Path

class ImageConvert():
    def __init__(self, IMAGENAME, NEWIMAGEFORMAT) -> None:
        self.PATH = Path().absolute()
        self.verfiy_if_converted_image_exists()
        self.IMS = f'{self.PATH}/converted_images/'
        self.name = str(IMAGENAME)
        self.NEW_IMAGE_FORMAT = str(NEWIMAGEFORMAT)
        self.IMAGE_FORMAT = self.VerifyExtensionFile(self.name.lower())

    def convertImage(self):
        with Image.open(self.name) as im:
            self.name = self.name.replace(self.IMAGE_FORMAT, self.NEW_IMAGE_FORMAT).split('/')[-1]
            im.convert('RGB').save(f'{self.IMS}{self.name}')

    def VerifyExtensionFile(self, imageName):
        VALIDEXTENSIONS = ['png' ,'webp','jpeg','gif','bmp','tiff','pdf','eps', 'jpg']
        for ex in VALIDEXTENSIONS:
            if imageName.find(f'.{ex}') != -1:
                return ex

    def verfiy_if_converted_image_exists(self):
        if not (Path('converted_images').exists()): Path('converted_images').mkdir()