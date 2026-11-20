import os
import sqlite3 as sql


def insertUsersMd(nombre, contraseña):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO USERSMEDIC VALUES ('{nombre}', '{contraseña}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

print('\nIngrese las credenciales del medico nuevo: ')
nombre = str(input('Nombre y apellido: '))
contraseña = str(input('Ingrese sa contraseña que va asignar: '))

insertUsersMd(nombre, contraseña)