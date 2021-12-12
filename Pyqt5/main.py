# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "PyQt5 Window"
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec_())