from PIL import Image
from pathlib import Path

class ImageConvert():
    def __init__(self, IMAGENAME, NEWIMAGEFORMAT) -> None:
        """[Convert the desired image to the desired format.]

        Args:
            IMAGENAME ([str]): [Name of the image to be converted]
            NEWIMAGEFORMAT ([str]): [Format the image will be saved]
        """        
        self.PATH = Path().absolute()
        self.verfiy_if_converted_image_exists()
        self.IMS = f'{self.PATH}/converted_images/'
        self.name = str(IMAGENAME)
        self.NEW_IMAGE_FORMAT = str(NEWIMAGEFORMAT)
        self.IMAGE_FORMAT = self.VerifyExtensionFile(self.name.lower())

    def convertImage(self):
        """[Convert the desired image.]

        Returns:
            [Int]: [Returns 0 if the conversion is successful, otherwise returns 1.]
        """
        try :
            with Image.open(self.name) as im:
                self.name = self.name.replace(self.IMAGE_FORMAT, self.NEW_IMAGE_FORMAT).split('/')[-1]
                im.convert('RGB').save(f'{self.IMS}{self.name}') # Convert to RGB and save image
                return 0
        except :
            return 1

    def VerifyExtensionFile(self, imageName):
        """[Check the image extension and return it.]

        Args:
            imageName ([str]): [image name]

        Returns:
            [str]: [Image extension]
        """
        VALIDEXTENSIONS = ['png' ,'webp','jpeg','gif','bmp','tiff','pdf','eps', 'jpg']
        for ex in VALIDEXTENSIONS:
            if imageName.find(f'.{ex}') != -1:
                return ex

    def verfiy_if_converted_image_exists(self):
        """[Checks if the folder where the converted images will be saved exists, if not, this function will create the folder.]
        """        
        if not (Path('converted_images').exists()): Path('converted_images').mkdir()