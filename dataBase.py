import sqlite3 as sql
import os
from datetime import datetime
import Admin

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
    instruccion = f"DROP TABLE USARIOS"
    cursor.execute(instruccion)
    print('Tabla eliminada correctamente.')
    conn.commit()
    conn.close()




def cancelar_cita_medico(nombre_medico):

    citas = Admin.mostrar_citas(nombre_medico)

    if not citas:
        print('No hay citas registradas.')
        return

    Admin.listar_citas(citas)

    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    try:
        while True:

            id_cita = input('\nIngrese el ID de la cita que desea cancelar (o salir): ')

            if id_cita.lower() == 'salir':
                print('Volviendo al menú...')
                break

            if not id_cita.isdigit():
                print('ID no válido.')
                continue

            cursor.execute(
                "SELECT estado FROM CITAS WHERE id_cita = ? AND medico = ?",
                (id_cita, nombre_medico)
            )

            cita = cursor.fetchone()

            if cita is None:
                print('No se encontró la cita o no pertenece a este médico.')
                continue

            if cita[0] == 'Cancelada':
                print('Esta cita ya está cancelada.')
                continue

            cursor.execute(
                "UPDATE CITAS SET estado = ? WHERE id_cita = ? AND medico = ?",
                ('Cancelada', id_cita, nombre_medico)
            )

            conn.commit()

            print('¡Cita cancelada correctamente!')

    finally:
        cursor.close()
        conn.close()


#=============================TODO LO RELACIONADO A MEDICO==================================================




def mostrar_citas_medico(nombre_medico):

    while True:
        ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
        conn = sql.connect(ruta_db)
        cursor = conn.cursor()

        instruccion = """
        SELECT * FROM CITAS
        WHERE medico = ? AND estado = ?
        """
        cursor.execute(instruccion, (nombre_medico, 'Pendiente'))

        citas = cursor.fetchall()

        cursor.close()
        conn.close()

        if not citas:
            print('\nNo tienes citas pendientes.')
        else:
            Admin.listar_citas(citas)

        print('''
        1. Consultar nuevamente
        2. Volver al menú
        ''')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            continue
        elif opcion == '2':
            break
        else:
            print('Opción no válida. Intente nuevamente.')

def crearTBcitas():
    '''Crea la tabla de las citas.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS CITAS (
    id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente TEXT,
    medico TEXT,
    fecha TEXT,
    hora TEXT,
    estado TEXT,
    descripcion TEXT
)
""")

    conn.commit()
    conn.close()




def crearTBUSERS():
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS USUARIOS (
id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
usuario TEXT UNIQUE,
password TEXT,
rol TEXT,
medico TEXT
)
    """)
    conn.commit()
    conn.close()

def registrar_usuario(usuario, password, rol, medico=None):

    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = """
    INSERT INTO USUARIOS (usuario, password, rol, medico)
    VALUES (?, ?, ?, ?)
    """

    cursor.execute(instruccion, (usuario, password, rol, medico))

    conn.commit()
    cursor.close()
    conn.close()

def validar_login(usuario, password):

    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = """
    SELECT id_usuario, usuario, rol, medico
    FROM USUARIOS
    WHERE usuario = ? AND password = ?
    """

    cursor.execute(instruccion, (usuario, password))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    return resultado


def asociar_medico(usuario, nombre_medico):

    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = """
    UPDATE USUARIOS
    SET medico = ?
    WHERE usuario = ?
    """

    cursor.execute(instruccion, (nombre_medico, usuario))

    conn.commit()

    cursor.close()
    conn.close()
#Prueba de funcion de registro de usuarios.
    


#def obtener_contacto_paciente(nombre_paciente):
    #

if __name__ == '__main__':
    #crearDB()
    #crearTBmd()
    #nombre = 'Gesler'
    #buscar_usuario(nombre)
    #crearTBcitas()
    while True:
                print('Ingresa los datos o ingresa S para terminar.')
                
                usuario = str(input('Usuario: '))
                if usuario == 'S':
                    break
                passw = str(input('Contraseña: '))
                rol = str(input('Rol: '))
                Asocs = str(input('Ingresa la cuenta asociada: '))
                
                registrar_usuario(usuario, passw, rol, Asocs)


    #crearTBUSERS()
    #crearTBUsers()
    #eliminaTb()
    #insertFilaPC()