# Imports
from PyQt5 import uic, QtWidgets

# Functions

def city_selected():
    city = form.cityBoxOptions.currentText()

    form.selectedCity.setText(f'<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:600;">Cidade : <span style="color : red">{city}</span></span></p></body></html>')

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.cityBoxOptions.addItems(["Paraíba", "São Paulo", "Rio de Janeiro", "Belo Horizonte"])
form.selectCityButton.clicked.connect(city_selected)

# Show, exec

form.show()
app.exec()