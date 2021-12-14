# Imports
from PyQt5 import uic, QtWidgets

# Functions

def add_to_list():
    text = form.textBox.text()
    if text != '':
        form.list.addItem(text)
        form.textBox.setText("")

def remove_last_item_to_list():
    #form.list.clear()
    form.list.takeItem(form.list.count() - 1)

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.add.clicked.connect(add_to_list)
form.remove.clicked.connect(remove_last_item_to_list)

# Show, exec

form.show()
app.exec()