# Imports
from PyQt5 import uic, QtWidgets

# Functions

def get_calendar_date():
    date = str(form.calendar.selectedDate()).replace(',', '/').replace(' ', '').strip()
    date = date[19:len(date)-1]
    #date = {'year' : date[0:4], 'month' : date[4:6], 'day' : date[6:len(date)]}
    #form.date.setText(f'Data selecionada : {date["day"]}/{date["month"]}/{date["year"]}')
    form.date.setText(f'Data selecionada : {date}')
    form.date.adjustSize()
app = QtWidgets.QApplication([])

# Form

form = uic.loadUi("interface.ui")

# Buttons

form.calendar.selectionChanged.connect(get_calendar_date)

# Show, exec

form.show()
app.exec()