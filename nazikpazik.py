from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
#створення додатку
app=QApplication([])
win=QWidget()

win.resize(500,500)
win.setWindowTitle("Tест ГібХаб")

title=QLabel("Тестовий додаток для гіт хабу ")

line_h=QHBoxLayout()
line_h.addWidget(title)
win.setLayout(line_h)

win.show()
app.exec_()
