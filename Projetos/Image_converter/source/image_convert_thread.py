from PyQt5.QtCore import QThread, pyqtSignal
from .image_convert import ImageConvert

class Image_convert_thread(QThread):
    item_status = pyqtSignal(int)
    
    def run(self):
        for image in self.files:
            im = ImageConvert(image, self.new_type_images).convertImage()
            self.item_status.emit(im)
            
    def set_files(self, files):
        self.files = files

    def set_new_type_images(self, new_type_images):
        self.new_type_images = new_type_images