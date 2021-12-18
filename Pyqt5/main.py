# Imports
from PyQt5 import uic, QtWidgets
from json import JSONEncoder as JE
from json import JSONDecoder as JD

# Functions

def save():
    name = form.name_input.text()
    age = form.age_input.text()
    cell = form.cell_input.text()
    data = JE().encode({"Name" : name, "Age" : age, "Cell" : cell})

    file = QtWidgets.QFileDialog.getSaveFileName(filter="Json (*.json)")[0].replace('.json', '')

    with open(f'{file}.json', 'w') as f: f.write(data)

def open_register():
    try :
        data = JD().decode(open(QtWidgets.QFileDialog.getOpenFileName(filter="Json (*.json)")[0]).read())
    except FileNotFoundError:
        QtWidgets.QMessageBox.warning(form, "Error", "Arquivo não encontrado, insira um arquivo válido!")
    else: 
        try :
            form.name_input.setText(data["Name"])
            form.age_input.setText(data["Age"])
            form.cell_input.setText(data["Cell"])
        except KeyError:
            QtWidgets.QMessageBox.warning(form, "Error", f"Arquivo Inválido, insira um arquivo válido!")

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.menuSave.triggered.connect(save)
form.menuOpen.triggered.connect(open_register)

# Show, exec

form.show()
app.exec()