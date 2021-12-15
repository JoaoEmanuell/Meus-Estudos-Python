# Imports
from PyQt5 import uic, QtWidgets

# Functions

def call_second_screen():
    form_2.show()
    form.close()

def call_first_screen():
    form.show()
    form_2.close()

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")
form_2 = uic.loadUi("interface_2.ui")

# Buttons

form.pushButton.clicked.connect(call_second_screen)
form_2.pushButton.clicked.connect(call_first_screen)

# Show, exec

form.show()
app.exec()