import sqlite3 as sql
import os
print('Base de datos')

def crearDB():
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    conn.commit()
    conn.close()

def crearTBmd():
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

def crearTBpc():
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



def insertRowMd(nombreMedic, especialidad, horario):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MEDICOS VALUES ('{nombreMedic}', '{especialidad}', '{horario}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def crearTBPc():
    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute(
            """CREATE TABLE PACIENTES(
                name text,
                contacto text,
                identificacion text
            )"""
        )
    conn.commit()
    conn.close()

def insertRowPC(nombrePC, contacto, identificacion):
    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO PACIENTES VALUES ('{nombrePC}', '{contacto}', '{identificacion}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    

if __name__ == '__main__':
    #crearDB()
    #crearTabla()
    pass
    #insertRow('Luis', 'Medico General', '8 am - 4pm')