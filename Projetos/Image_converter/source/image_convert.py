from PIL import Image
from pathlib import Path
from os.path import join, getmtime
from os import utime
from datetime import datetime
from time import mktime

class ImageConvert():
    def __init__(self, IMAGENAME : str, NEWIMAGEFORMAT : str) -> None:
        """[Convert the desired image to the desired format.]

        Args:
            IMAGENAME ([str]): [Name of the image to be converted]
            NEWIMAGEFORMAT ([str]): [Format the image will be saved]
        """        
        #self.PATH = Path().absolute()
        self.verfiy_if_converted_image_directory_exists()
        self.IMAGE_SAVE_DIRECTORY = join(Path().absolute(), 'converted_images')
        self.name = IMAGENAME
        self.NEW_IMAGE_FORMAT = NEWIMAGEFORMAT
        self.IMAGE_FORMAT = self.verify_extension_file()

    def convert_image(self) -> int:
        """[Convert the desired image.]

        Returns:
            [Int]: [Returns 0 if the conversion is successful, otherwise returns 1.]
        """
        try :
            with Image.open(self.name) as im:
                self.mod_time = self.get_image_modify_date()
                self.name = self.name.replace(self.IMAGE_FORMAT, self.NEW_IMAGE_FORMAT).split('/')[-1]
                im.convert('RGB').save(f'{self.IMAGE_SAVE_DIRECTORY}/{self.name}') # Convert to RGB and save image
                self.set_image_modify_date()
                return 0
        except :
            return 1

    def verify_extension_file(self) -> str:
        """[Check the image extension and return it.]

        Args:
            imageName ([str]): [image name]

        Returns:
            [str]: [Image extension]
        """
        return self.name.lower().split('.')[-1]

    def verfiy_if_converted_image_directory_exists(self) -> None:
        """[Checks if the folder where the converted images will be saved exists, if not, this function will create the folder.]
        """        
        if not (Path('converted_images').exists()): Path('converted_images').mkdir()

    def get_image_modify_date(self) -> float:
        """[Get the image modify date]

        Returns:
            float: [mktime date of the image]
        """        
        date = getmtime(self.name)
        date = datetime.fromtimestamp(date)
        return mktime(date.timetuple())

    def set_image_modify_date(self) -> None:
        """[Set the image modify date]
        """        
        utime(f'{self.IMAGE_SAVE_DIRECTORY}/{self.name}', (self.mod_time, self.mod_time))