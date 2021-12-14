# Imports
from PyQt5 import uic, QtWidgets

def main_function():
    radios_buttons_status = {'azul' : form.azul.isChecked(), 'amarelo' : form.amarelo.isChecked(), 'verde' : form.verde.isChecked(), 'vermelho' : form.vermelho.isChecked()}
    for key, value in radios_buttons_status.items():
        if value:
            option = key
            break

    form.color_label.setText(f'Cor selecionada : {option}')
    form.color_label.adjustSize()

app = QtWidgets.QApplication([])

form = uic.loadUi("interface.ui")
form.pushButton.clicked.connect(main_function)

form.show()
app.exec()