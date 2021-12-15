# Imports
from PyQt5 import uic, QtWidgets

# Functions

def show_mensage():
    mensage = form.textBox.text()
    form.textBox.setText("")
    if mensage == "":
        QtWidgets.QMessageBox.about(form, "Texto em branco !", mensage)
    else:
        QtWidgets.QMessageBox.about(form, "Bem vindo : ", mensage)

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.verify.clicked.connect(show_mensage)

# Show, exec

form.show()
app.exec()