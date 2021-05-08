import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtWidgets


class Main(QtWidgets.QApplication):

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.loadUi('main.ui')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Main()
    GUI.show()
    sys.exit(app.exec_())
