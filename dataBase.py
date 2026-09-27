import sqlite3 as sql
print('Base de datos')

def crearDB():
    conn = sql.connect('usuarios.db')
    conn.commit()
    conn.close()

def crearTabla():
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

def insertRow(nombreMedic, especialidad, horario):
    conn = sql.connect('usuarios.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MEDICOS VALUES ('{nombreMedic}', '{especialidad}', '{horario}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    #crearDB()
    #crearTabla()
    insertRow('Gesler', 'Medico General', '8 am - 2 pm')