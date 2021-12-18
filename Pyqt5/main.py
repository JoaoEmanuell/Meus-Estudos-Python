# Imports
from PyQt5 import uic, QtWidgets

# Functions

def frame_1():
    form.frame_2.close()

def frame_2():
    form.frame_2.show()

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.button_frame_1.clicked.connect(frame_1)
form.button_frame_2.clicked.connect(frame_2)

# Show, exec

form.show()
app.exec()