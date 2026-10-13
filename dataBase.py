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
    '''Pacientes'''
    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute(
            """CREATE TABLE PACIENT(
                name text,
                contacto text,
                identificacion text,
                edad text
            )"""
        )
    conn.commit()
    conn.close()

def insertFilaPC(nombrePC = str, contacto = str, identificacion = str, edad = str):
    '''Pide los datos basicos del paciente.'''
    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO PACIENT VALUES ('{nombrePC}', '{contacto}', '{identificacion}', '{edad}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def eliminaTb():
    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()
    instruccion = f"DROP TABLE PACIENTES"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
    

if __name__ == '__main__':
    #crearDB()
    #crearTBPc()
    pass
    # eliminaTb()
    #insertFilaPC()