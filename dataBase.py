import sqlite3 as sql
import os
print('Base de datos')

def crearDB():
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    conn.commit()
    conn.close()

def crearTabla():
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE MEDICOS(
            name text,
            especialidad text,
            horarios text
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombreMedic, especialidad, horario):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MEDICOS VALUES ('{nombreMedic}', '{especialidad}', '{horario}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    #crearDB()
    #crearTabla()
    pass
    #insertRow('Luis', 'Medico General', '8 am - 4pm')