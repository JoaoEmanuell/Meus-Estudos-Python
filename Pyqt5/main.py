# Imports
from PyQt5 import uic, QtWidgets

# Functions

def green_menu(): setOutput("Green", "green")

def red_menu(): setOutput("Red", "red")

def blue_menu(): setOutput("Blue", "blue")

def setOutput(text, color): form.output.setText(f'<html><head/><body><p align="center"><span style=" font-size:20pt; font-weight:600; color : {color}">{text}</span></p></body></html>')

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.menuGreen.triggered.connect(green_menu)
form.menuRed.triggered.connect(red_menu)
form.menuBlue.triggered.connect(blue_menu)

# Show, exec

form.show()
app.exec()