import sqlite3
from sqlite3 import Error
from inspect import currentframe, getframeinfo


def connection():
    try:
        conn = sqlite3.connect('calculadora.db')
        return conn
    except Error:
        pass


def crear_tabla_variables():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS [variables] (
        [id_var] INTEGER  NOT NULL PRIMARY KEY,
        [variable] TEXT  NOT NULL)''')
    cantidad_registros = cursor.execute('select count(*) from variables').fetchone()[0]
    while cantidad_registros < 2:
        cursor.execute('insert into variables(variable) VALUES (0)')
        cantidad_registros = cursor.execute('select count(*) from variables').fetchone()[0]
    conn.commit()
    conn.close()


def agregar_var_a_tabla(id_var, var):
    try:
        conn = connection()
        cursor = conn.cursor()
        dato = [var, id_var]
        cursor.execute("UPDATE variables SET variable = (?) FROM variables WHERE 'id_var'=(?)", dato)
        conn.commit()
        conn.close()
    except ValueError:
        print("error en la linea %d" % getframeinfo(currentframe()).lineno)


def ver_variable1(idvar):
    conn = connection()
    try:
        var = conn.cursor().execute('select variable from variables where id_var=(?)', (idvar,)).fetchone()[0]
    except TypeError:
        var = 0
        print('error')
    return var


def agregar_variable(id_var, var):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE variables SET variable=(?) WHERE id_var=(?)""", (var, id_var))
    conn.commit()
