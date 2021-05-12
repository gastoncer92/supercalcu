import sys
from main import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.add_item("0"))
        self.pushButton_1.clicked.connect(lambda: self.add_item("1"))
        self.pushButton_11.clicked.connect(self.result)
        self.pushButton_10.clicked.connect(lambda: self.add_item("."))
        self.pushButton_12.clicked.connect(lambda: self.add_item("+"))
        self.pushButton_13.clicked.connect(lambda: self.add_item("-"))
        self.pushButton_14.clicked.connect(lambda: self.add_item("*"))
        self.pushButton_15.clicked.connect(lambda: self.add_item("/"))
        self.pushButton_16.clicked.connect(self.delete_item)
        self.pushButton_17.clicked.connect(lambda: self.add_item("%"))
        self.pushButton_18.clicked.connect(lambda: self.add_item(")"))
        self.pushButton_19.clicked.connect(lambda: self.add_item("("))
        self.pushButton_2.clicked.connect(lambda: self.add_item("2"))
        self.pushButton_3.clicked.connect(lambda: self.add_item("3"))
        self.pushButton_4.clicked.connect(lambda: self.add_item("4"))
        self.pushButton_5.clicked.connect(lambda: self.add_item("5"))
        self.pushButton_6.clicked.connect(lambda: self.add_item("6"))
        self.pushButton_7.clicked.connect(lambda: self.add_item("7"))
        self.pushButton_8.clicked.connect(lambda: self.add_item("8"))
        self.pushButton_9.clicked.connect(lambda: self.add_item("9"))
        self.pushButton_20.clicked.connect(self.delete_all)
        self.lineEdit.textChanged.connect(self.print)

    def print(self):
        print('hola mundo!')

    def delete_all(self):
        return self.lineEdit.setText('')

    def result(self):
        return self.lineEdit.setText(str(eval(self.lineEdit.text().replace('%', '/100'))))

    def delete_item(self):
        todo = self.lineEdit.text()
        new_text = todo[0:-1]
        self.lineEdit.setText(new_text)

    def add_item(self, item: str):
        todo = self.lineEdit.text()
        return self.lineEdit.setText("%s%s" % (todo, item))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

# from PyQt5 import uic, QtWidgets
# from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
# form_class = uic.loadUiType("main.ui")[0]

# class Main(QMainWindow):
#     def __init__(self):
#         super(Main, self).__init__()
#         uic.loadUi("main.ui", self)
#         self.show()


# app = QApplication(sys.argv)
# window = Main()
# app.exec_()
