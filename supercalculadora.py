from main import *
from db_calc import *
import string
from inspect import currentframe, getframeinfo


# pyuic5 -x main.ui -o main.py

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Super-Calcu")
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
        crear_tabla_variables()
        self.actualiza_variables()
        self.pushButton_21.clicked.connect(self.agregar_variable1)
        self.pushButton_22.clicked.connect(self.agregar_variable2)
        self.pushButton_23.clicked.connect(self.cargar_variable1)
        self.pushButton_24.clicked.connect(self.cargar_variable2)

    def cargar_variable1(self):
        var = self.pushButton_21.text()
        self.add_item(var)

    def cargar_variable2(self):
        var = self.pushButton_22.text()
        self.add_item(var)

    def actualiza_variables(self):
        conn = connection()
        cursor = conn.cursor()
        variable1 = cursor.execute("select variable from variables where id_var=1").fetchone()[0]
        variable2 = cursor.execute("select variable from variables where id_var=2").fetchone()[0]
        self.pushButton_21.setText(variable1)
        self.pushButton_22.setText(variable2)

    def agregar_variable1(self):
        self.agregar_variable(1)

    def agregar_variable2(self):
        self.agregar_variable(2)

    def agregar_variable(self, idvar):
        contenido = self.label_2.text()
        for i in contenido:
            contenido = contenido.replace(' ', '')
        for i in string.ascii_lowercase:
            contenido = contenido.replace(i, '')
        for i in string.ascii_uppercase:
            contenido = contenido.replace(i, '')
        print("en la linea %d" % getframeinfo(currentframe()).lineno)
        print(contenido)
        agregar_variable(idvar, contenido)
        var = ver_variable1(idvar)
        if idvar == 1:
            self.pushButton_21.setText('%s' % var)
        elif idvar == 2:
            self.pushButton_22.setText('%s' % var)
        else:
            print('error')

    def delete_all(self):
        return self.lineEdit.setText('')

    def result(self):
        try:
            resultado = str(eval(self.lineEdit.text().replace('%', '/100')))
            self.label_2.setText("%.2f" % float(resultado))
            return self.lineEdit.setText("")
        except SyntaxError:
            return self.label_2.setText("")
        except ZeroDivisionError:
            return self.label_2.setText("No se puede dividir por cero")
        except NameError:
            return self.label_2.setText("")

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
