# Imports
from PyQt5 import uic, QtWidgets

# Functions

value = 0
def more_progresse_bar():
    global value
    value += 10
    form.progressBar.setValue(value)

def zero_progress_bar():
    global value
    value = 0
    form.progressBar.setValue(0)

app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.more.clicked.connect(more_progresse_bar)
form.zero.clicked.connect(zero_progress_bar)

# Show, exec

form.show()
app.exec()