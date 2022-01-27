from PyQt5.QtCore import QThread, pyqtSignal
from .image_convert import ImageConvert

class ImageConvertThread(QThread):
    item_status = pyqtSignal(int)
    
    def run(self):
        for image in self.images:
            im = ImageConvert(image, self.new_type_images).convert_image()
            self.item_status.emit(im)
            
    def set_images(self, images : list):
        self.images = images

    def set_new_type_images(self, new_type_images : str):
        self.new_type_images = new_type_images