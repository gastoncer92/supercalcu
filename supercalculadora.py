import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication

form_class = uic.loadUiType("main.ui")[0]


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("main.ui", self)
        self.show()




app = QApplication(sys.argv)
window = Main()
app.exec_()
