"""
    File to start a new Thread, wiich will serve to convert the images.
"""
from PyQt5.QtCore import QThread, pyqtSignal
from .image_convert import ImageConvert

class ImageConvertThread(QThread):
    item_status = pyqtSignal(int)
    
    def run(self):
        """Run the thread
        """        
        for image in self.images:
            im = ImageConvert(image, self.new_type_images).convert_image()
            self.item_status.emit(im)
            
    def set_images(self, images : list):
        """Set the images to be converted

        Args:
            images (list): a list of images to be converted
        """        
        self.images = images

    def set_new_type_images(self, new_type_images : str):
        """Set the new type of images

        Args:
            new_type_images (str): the new type of images
        """        
        self.new_type_images = new_type_images