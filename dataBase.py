import sqlite3 as sql
print('Base de datos')

def crearDB():
    conn = sql.connect('usuarios.db')
    conn.commit()
    conn.close()

def crearTBMd():
    conn = sql.connect('usuarios.db')
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
    conn = sql.connect('usuarios.db')
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
    #crearTBPc()
    #insertRowMd('Gesler', 'Medico General', '8 am - 2 pm')
    insertRowPC("Luis", "57900190", "282567896F")