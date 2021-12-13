# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton ,QLabel
from PyQt5 import QtGui

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "PyQt5 Window"

        self.button = self.createButton("Hide image", css="background-color: #FF6363; font-weight: bold; border-radius : 15px;")
        self.button.clicked.connect(self.buttonClicked)
        self.label = self.createLabel("Hello World", move=(100, 50), css = "color : blue")

        self.image = self.createLabel("", move=(100, 300))
        self.image.setPixmap(QtGui.QPixmap("car.webp"))
        self.image.adjustSize()
        self.showImage = 1

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def createButton(self, name='Button', move=(100, 100), resize=(100, 100), **kw):
        css = kw.get('css', '')
        button = QPushButton(name, self)
        button.move(move[0], move[1]), button.resize(resize[0], resize[1]), button.setStyleSheet(css)
        return button

    def createLabel(self, text='Label', move=(100, 100), **kw):
        css = kw.get('css', '')
        label = QLabel(self)
        label.setText(text), label.move(move[0], move[1]), label.setStyleSheet(css)
        return label

    def buttonClicked(self):
        images_list = ['car.webp', '']
        self.label.setText('Button Clicked')
        self.image.setPixmap(QtGui.QPixmap(images_list[self.showImage]))
        self.image.adjustSize()
        
        if self.showImage == 0:
            self.showImage = 1
            self.button.setText("Hide image")
        else:
            self.showImage = 0
            self.button.setText("Show image")

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec_())