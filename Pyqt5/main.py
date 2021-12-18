# Imports
from PyQt5 import uic, QtWidgets
from json import JSONEncoder as JE

# Functions

def save():
    name = form.name_input.text()
    age = form.age_input.text()
    cell = form.cell_input.text()
    data = JE().encode({"Name" : name, "Age" : age, "Cell" : cell})

    file = QtWidgets.QFileDialog.getSaveFileName(filter="Json (*.json)")[0].replace('.json', '')

    with open(f'{file}.json', 'w') as f: f.write(data)

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.menuSave.triggered.connect(save)

# Show, exec

form.show()
app.exec()