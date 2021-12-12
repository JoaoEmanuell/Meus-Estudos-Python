# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "PyQt5 Window"

        button = self.createButton("Click Me", 100, 100)
        self.text = 'Hello World'
        button.clicked.connect(self.buttonClicked)

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def createButton(self, name, x, y):
        button = QPushButton(name, self)
        button.move(x, y)
        button.resize(100, 100)
        button.setStyleSheet("background-color: red;font-weight: bold;")
        return button

    def buttonClicked(self):
        print(self.text)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec_())