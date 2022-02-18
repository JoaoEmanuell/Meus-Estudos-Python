# Imports

# Global Imports

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from pathlib import Path
from os import listdir

# Local Imports

from source import ImageConvertThread

class Window():
    def __init__(self):
        """[Launches the interface and tells you what each button should do when it's clicked]
        """        
        self.app = QApplication([])

        # Forms

        self.form = self.load_ui('interface.ui')

        # Buttons

        self.form.select_images_button.clicked.connect(self.open_images)
        self.form.convert_images_button.clicked.connect(self.convert_images)

        # Execute
        self.form.show()
        self.app.exec()

    def load_ui(self, ui_file):
        """Loads the desired interface, every interface is a .ui file

        Args:
            ui_file ([ui]): [.ui file name]

        Returns:
            [ui]: [Interface loaded]
        """
        path = Path().absolute()
        return uic.loadUi(f'{path}/{ui_file}')

    def open_images(self):
        """[Opens a dialog for the user to choose the images they prefer, the images are filtered by file format to avoid bugs.]
        """        
        self.form.image_name_list.clear()
        filter = "Images (*.png *.jpg *.jpeg *.bmp *.gif *.webp)"
        self.files = QFileDialog.getOpenFileNames(filter=filter)[0]
        self.set_images_in_list()

    def convert_images(self):
        """[Convert the images and place an icon in the status list, if the image is successfully converted the icon will be "Successful_Image_Conversion" if not converted the icon will be "Unsuccessful_image_conversion"]
        """        
        self.form.status_list.clear()
        self.work = ImageConvertThread()
        self.work.set_images(self.files)
        self.work.set_new_type_images(self.form.comboBox.currentText())
        self.work.start()
        self.work.item_status.connect(self.set_convert_item_status_list)

    def set_convert_item_status_list(self, val):
        """[Set the icon in the status list, if the image is successfully converted the icon will be "Successful_Image_Conversion" if not converted the icon will be "Unsuccessful_image_conversion"]""" 
        icon_path = listdir(f'{Path().absolute()}/icons/')
        icon = QIcon(f'{Path().absolute()}/icons/{icon_path[val]}')               
        item = QListWidgetItem(icon, "")
        item.setSizeHint(QSize(25, 25))
        self.form.status_list.addItem(item)
        self.form.status_list.setCurrentRow(self.form.status_list.count() - 1)
        self.form.image_name_list.setCurrentRow(self.form.status_list.count() - 1) 
        
    def set_images_in_list(self):
        """[Set the image names in the image name list, it removes the image name path, making the interface more pleasant.]
        """        
        for image in self.files:
            # Remove the path from the image and add it to the list and set size of the item
            item = QListWidgetItem(image.split('/')[-1])
            item.setSizeHint(QSize(25, 25))
            self.form.image_name_list.addItem(item)

if __name__ == '__main__':
    Window()