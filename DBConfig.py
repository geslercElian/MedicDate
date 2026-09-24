import sqlite3

conn = sqlite3.connect('Usuarios.db')
conn.commit()
print(conn)

tabMedicos = conn.cursor()
tabMedicos.execute(
    """CREATE TABLE MEDICOS(
        name text,
        especialidad text,
        horarios text
    )"""
)
tabMedicos.commit()
print(tabMedicos)
