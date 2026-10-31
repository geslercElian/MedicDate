import sqlite3 as sql
import os
print('Base de datos')



def crearDB():
    '''Se crea la base de datos.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    conn.commit()
    conn.close()

def crearTBmd():
    '''Crea la tabla de los medicos'''
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




def insertRowMd(nombreMedic = str, especialidad = str, horario = str):
    '''Pide e inserta los medicos en su respectiva tabla.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MEDICO VALUES ('{nombreMedic}', '{especialidad}', '{horario}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def crearTBPc():
    '''Crea la tabla de los pacientes.'''
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
    '''Pide e inserta los datos del paciente en su respectiva tabla.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO PACIENT VALUES ('{nombrePC}', '{contacto}', '{identificacion}', '{edad}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def buscar_usuario(busqueda=str):
    '''Busca los usuarios relacionados al nombre que busca.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor() 
    instruccion_paciente = "SELECT * FROM PACIENT WHERE name LIKE  ?"
    cursor.execute(instruccion_paciente, (f'%{busqueda}%',))
    paciente = cursor.fetchall()

    instruccion_medico = "SELECT * FROM MEDICO WHERE name LIKE ?"
    cursor.execute(instruccion_medico, (f'%{busqueda}%',))
    medicos = cursor.fetchall()

    cursor.close()

    return paciente, medicos

def mostrar_user(pacientes, medicos):
    '''Muestra los usuarios encontrados en cada tabla.'''
    usuarios = []

    contador = 1

    print('\nPacientes')

    for paciente in pacientes:
        print(f'{contador}. {paciente[0]}')
        usuarios.append(('Paciente', paciente))
        contador += 1

    print('\nMedicos')

    for medico in medicos:
        print(f'{contador}. {medico[0]}')
        usuarios.append(('medico', medico))
        contador += 1

    return usuarios

def selecionar_user(usuarios):
    '''Selecciona el usuario a editar.'''
    seleccion = int(input('\nSeleccione el usuario que desea modificar: '))
    usuario = usuarios[seleccion - 1]
    return usuario

def tipo_user(usuario):
    tipo = usuario[0]
    return tipo

def mostrar_campos(usuario):
    '''Muestra los campos disponibles para editar'''
    tipo = usuario[0]

    if tipo == 'Paciente':
        print('\nSeleccione lo que va a modificar: ')
        print('''
            1. Nombre
            2. Contacto
            3. Identificacion
            4. Edad
        ''')
    elif tipo == 'medico':
        print('\nSeleccione lo que va a modificar: ')
        print('''
            1. Nombre
            2. Especialidad
            3. Horario
        ''')

def selecionar_campos(usuario):
    '''Selecciona el campo a editar'''
    tipo = usuario[0]

    if tipo == 'Paciente':
        seleccion = int(input('\nSeleccione el dato que desea modificar: '))


        campos = {
            1: 'nombre',
            2: 'contacto',
            3: 'identificacion',
            4: 'edad'
        }
    elif tipo == 'medico':
        seleccion = int(input('\nSeleccione el dato que desea modificar: '))

        campos = {
            1: 'nombre',
            2: 'especialidad',
            3: 'horario'
        }
    return campos[seleccion]

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
    pass
    #eliminaTb()
    #insertFilaPC()