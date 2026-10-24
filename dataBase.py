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
        """CREATE TABLE MEDICO(
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
    instruccion = f"INSERT INTO MEDICO VALUES ('{nombreMedic}', '{especialidad}', '{horario}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def crearTBPc():
    '''Pacientes'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
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
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO PACIENT VALUES ('{nombrePC}', '{contacto}', '{identificacion}', '{edad}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def buscar_usuario(busqueda=str):
    '''Busca los usuarios relacionados'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor() 
    instruccion_paciente = "SELECT * FROM PACIENT WHERE name LIKE  ?"
    cursor.execute(instruccion_paciente, (f'%{busqueda}%',))
    paciente = cursor.fetchall()

    instruccion_medico = "SELECT * FROM MEDICOS WHERE name LIKE ?"
    cursor.execute(instruccion_medico, (f'%{busqueda}%',))
    medicos = cursor.fetchall()

    cursor.close()

    return paciente, medicos

def eliminaTb():
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"DROP TABLE MEDICOS"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
    

if __name__ == '__main__':
    #crearDB()
    #crearTBmd()
    #nombre = 'Gesler'
    #buscar_usuario(nombre)
    eliminaTb()
    #insertFilaPC()