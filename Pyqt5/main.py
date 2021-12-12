# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton ,QLabel

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "PyQt5 Window"

        button = self.CreateButton("Click Me", css="background-color: red; font-weight: bold;")
        self.text = 'Hello World'
        button.clicked.connect(self.buttonClicked)
        self.label = self.CreateLabel("Hello World", move=(100, 50), css = "color : blue")

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def CreateButton(self, name='Button', move=(100, 100), resize=(100, 100), **kw):
        css = kw.get('css', '')
        button = QPushButton(name, self)
        button.move(move[0], move[1]), button.resize(resize[0], resize[1]), button.setStyleSheet(css)
        return button

    def CreateLabel(self, text='Label', move=(100, 100), **kw):
        css = kw.get('css', '')
        label = QLabel(self)
        label.setText(text), label.move(move[0], move[1]), label.setStyleSheet(css)
        return label

    def buttonClicked(self):
        self.label.setText('Button Clicked')
        self.label.adjustSize()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec_())