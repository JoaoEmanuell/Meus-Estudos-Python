# Imports
from os import replace
from PyQt5 import uic, QtWidgets

# Functions

def sum():
    check_boxs_status = {'checkBox' : form.checkBox.isChecked(), 'checkBox_2' : form.checkBox_2.isChecked(), 'checkBox_3' : form.checkBox_3.isChecked(), 'checkBox_4' : form.checkBox_4.isChecked(), 'checkBox_5' : form.checkBox_5.isChecked()}
    values = [15, 20, 10, 32, 5.50]

    sum = 0
    pos = 0
    for key, value in check_boxs_status.items():
        if value == True:
            sum += values[pos]
        pos += 1
    
    form.output.setText(f'<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:600;">Valor total : <span style="color : red">{(sum):.2f}</span></span></p></body></html>')

    reset_check_boxs()

def reset_check_boxs(): form.checkBox.setChecked(False) ,form.checkBox_2.setChecked(False) ,form.checkBox_3.setChecked(False) ,form.checkBox_4.setChecked(False) ,form.checkBox_5.setChecked(False)

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.pushButton.clicked.connect(sum)

# Show, exec

form.show()
app.exec()