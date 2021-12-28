# Imports
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from pathlib import Path
from source import image_convert
from os import listdir

class window():
    def __init__(self):
        """[Launches the interface and tells you what each button should do when it's clicked]
        """        
        self.app = QtWidgets.QApplication([])

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
        self.files = QtWidgets.QFileDialog.getOpenFileNames(filter=filter)[0]
        self.set_images_in_list()

    def convert_images(self):
        """[Convert the images and place an icon in the status list, if the image is successfully converted the icon will be "Successful_Image_Conversion" if not converted the icon will be "Unsuccessful_image_conversion"]
        """        
        new_type_images = self.form.comboBox.currentText()
        icon_path = listdir(f'{Path().absolute()}/icons/')
        self.form.status_list.clear()
        for image in self.files:
            im = image_convert.ImageConvert(image, new_type_images).convertImage()
            icon = QtGui.QIcon(f'{Path().absolute()}/icons/{icon_path[im]}')
            item = QtWidgets.QListWidgetItem(icon, "")
            item.setSizeHint(QtCore.QSize(25, 25))
            self.form.status_list.addItem(item)

    def set_images_in_list(self):
        """[Set the image names in the image name list, it removes the image name path, making the interface more pleasant.]
        """        
        for image in self.files:
            # Remove the path from the image and add it to the list and set size of the item
            item = QtWidgets.QListWidgetItem(image.split('/')[-1])
            item.setSizeHint(QtCore.QSize(25, 25))
            self.form.image_name_list.addItem(item)

if __name__ == '__main__':
    window()