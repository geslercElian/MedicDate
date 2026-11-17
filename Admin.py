import sqlite3 as sql
import os
from dotenv import load_dotenv
from datetime import datetime

#

#Registrar los pacientes en la bd.
def insertFilaPC(nombrePC = str, contacto = str, identificacion = str, edad = str):
    '''Pide e inserta los datos del paciente en su respectiva tabla.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO PACIENT VALUES ('{nombrePC}', '{contacto}', '{identificacion}', '{edad}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#Registra los pacientes en la db.
def insertRowMd(nombreMedic = str, especialidad = str, horario = str):
    '''Pide e inserta los medicos en su respectiva tabla.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MEDICO VALUES ('{nombreMedic}', '{especialidad}', '{horario}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#Utilidades de Gest_pacientes()
def mostrar_pacientes():
    ''''Muestra todos los pacientes registrados.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM PACIENT")
    pacientes = cursor.fetchall()

    # Obtener nombres de las columnas
    columnas = [columna[0] for columna in cursor.description]

    conn.close()

    if not pacientes:
        print('No hay pacientes registrados.')
        return []

    # Mostrar encabezados
    print('\n' + '-' * 90)
    print(' | '.join(f'{col:<20}' for col in columnas))
    print('-' * 90)

    # Mostrar registros
    for paciente in pacientes:
        print(' | '.join(f'{str(dato):<20}' for dato in paciente))

    print('-' * 90)

    return pacientes

def buscar_paciente(busqueda=str):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor() 
    instruccion_paciente = "SELECT * FROM PACIENT WHERE name LIKE  ?"
    cursor.execute(instruccion_paciente, (f'%{busqueda}%',))
    paciente = cursor.fetchall()
    cursor.close()
    return paciente

def mostrar_paciente(paciente):
    usuarios = []
    
    contador = 1
    
    print('\nPacientes')
    
    for paciente in paciente:
            print(f'{contador}. {paciente[0]}')
            usuarios.append( paciente)
            contador += 1
    return usuarios

def selec_userP(pacientes):
    '''Selecciona el usuario a editar.'''

    if not pacientes:
        return 'No valido'

    seleccion = int(input('\nSeleccione una opcion: '))

    if seleccion < 1 or seleccion > len(pacientes):
        return 'No valido'

    paciente = pacientes[seleccion - 1]

    return paciente

def editar_paciente(nombre):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    campos = {
        1: 'name',
        2: 'contacto',
        3: 'identificacion',
        4: 'edad'
    }

    while True:
        print('\n¿Qué dato desea modificar?')
        print('1. Nombre')
        print('2. Contacto')
        print('3. Identificación')
        print('4. Edad')
        print('5. Volver')

        opcion = input('Seleccione una opción: ')

        if opcion == '5':
            break

        if not opcion.isdigit() or int(opcion) not in campos:
            print('Opción no válida')
            continue

        campo = campos[int(opcion)]

        nuevo_valor = input(f'Ingrese el nuevo valor para {campo}: ')

        instruccion = f'UPDATE PACIENT SET {campo} = ? WHERE name = ?'

        cursor.execute(instruccion, (nuevo_valor, nombre))
        conn.commit()

        if cursor.rowcount > 0:
            print('\nPaciente actualizado correctamente.')

            # Si modificamos el nombre, actualizamos la variable.
            if campo == 'name':
                nombre = nuevo_valor

        else:
            print('\nNo se encontró paciente.')

    conn.close()

def eliminar_paciente(nombre):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    
    print(f'\n¿Está seguro de que desea eliminar a {nombre}?')
    confirmacion = input('Escriba S para confirmar o N para cancelar: ').strip().upper()

    if confirmacion == 'S':
        instruccion = "DELETE FROM PACIENT WHERE name = ?"
        cursor.execute(instruccion, (nombre,))
        conn.commit()

        if cursor.rowcount > 0:
            print('\nPaciente eliminado correctamente.')
        else:
            print('\nNo se encontró el paciente.')

    else:
        print('\nEliminación cancelada.')

    conn.close()

#Gestion de pacientes.
def Gest_pacientes():
    while True:
        print("\nGestione un paciente: ")
        print('''
        1. Mostrar pacientes.
        2. Editar paciente.
        3. Eliminar paciente.
        4. Salir
        ''')
        opcion = int(input('> '))
        if opcion == 1:
            while True:
                mostrar_pacientes()
                print('Ingrese 1 para volver a Gestion: ')
                opt = int(input('> '))
                if opt == 1:
                    break
        elif opcion == 2:
            print('--Busque un paciente: ')
            busqueda = str(input('Ingrese el nombre del paciente: '))
            paciente = buscar_paciente(busqueda)
            usuarios = mostrar_paciente(paciente)
            selec = selec_userP(usuarios)
            
            editar_paciente(selec[0])
        elif opcion == 3:
            while True:
                busc = str(input('Busque un paciente o ingrese salir para cerra este menu > '))
                if busc == 'salir':
                    break
                pacientes = buscar_paciente(busc)
                usuarios = mostrar_paciente(pacientes)
                selec = selec_userP(usuarios)
                eliminar_paciente(selec[0])
        elif opcion == 4:
            break

#Utilidades de Gest_medicos()
def mostrar_medicos():
    ''''Muestra todos los medicos registrados.'''
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM MEDICO")
    medicos = cursor.fetchall()

    # Obtener nombres de las columnas
    columnas = [columna[0] for columna in cursor.description]

    conn.close()

    if not medicos:
        print('No hay medicos registrados.')
        return []

    # Mostrar encabezados
    print('\n' + '-' * 90)
    print(' | '.join(f'{col:<20}' for col in columnas))
    print('-' * 90)

    # Mostrar registros
    for medico in medicos:
        print(' | '.join(f'{str(dato):<20}' for dato in medico))

    print('-' * 90)

    return medicos

def buscar_medico(busqueda=str):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor() 
    instruccion_medico = "SELECT * FROM MEDICO WHERE name LIKE  ?"
    cursor.execute(instruccion_medico, (f'%{busqueda}%',))
    medico = cursor.fetchall()
    cursor.close()
    return medico

def mostrar_medico(medicos):
    usuarios = []
        
    contador = 1
    
    print('\nMedicos')
    
    for medico in medicos:
            print(f'{contador}. {medico[0]}')
            usuarios.append(medico)
            contador += 1
    return usuarios

def selec_userM(medicos):
    '''Selecciona el usuario a editar.'''
    
    if not medicos:
        return 'No valido'

    seleccion = int(input('\nSeleccione una opcion: '))

    if seleccion < 1 or seleccion > len(medicos):
        return 'No valido'

    medico = medicos[seleccion - 1]

    return medico

def editar_medico(nombre):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    campos = {
        1: 'name',
        2: 'especialidad',
        3: 'horarios',
    }

    while True:
        print('\n¿Qué dato desea modificar?')
        print('1. Nombre')
        print('2. Contacto')
        print('3. Horario')
        print('4. Volver')

        opcion = input('Seleccione una opción: ')

        if opcion == '4':
            break

        if not opcion.isdigit() or int(opcion) not in campos:
            print('Opción no válida')
            continue

        campo = campos[int(opcion)]

        nuevo_valor = input(f'Ingrese el nuevo valor para {campo}: ')

        instruccion = f'UPDATE MEDICO SET {campo} = ? WHERE name = ?'

        cursor.execute(instruccion, (nuevo_valor, nombre))
        conn.commit()

        if cursor.rowcount > 0:
            print('\nMedico actualizado correctamente.')

            # Si modificamos el nombre, actualizamos la variable.
            if campo == 'name':
                nombre = nuevo_valor

        else:
            print('\nNo se encontró medico.')

    conn.close()

def eliminar_medico(nombre):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    
    print(f'\n¿Está seguro de que desea eliminar a {nombre}?')
    confirmacion = input('Escriba S para confirmar o N para cancelar: ').strip().upper()

    if confirmacion == 'S':
        instruccion = "DELETE FROM MEDICO WHERE name = ?"
        cursor.execute(instruccion, (nombre,))
        conn.commit()

        if cursor.rowcount > 0:
            print('\nMedico eliminado correctamente.')
        else:
            print('\nNo se encontró el medico.')

    else:
        print('\nEliminación cancelada.')

    conn.close()

#Gestion de Medicos.
def Gest_medico():
    while True:
        
        print('\nGestione un medico: ')
        print('''
        1. Mostrar medicos.
        2. Editar medico.
        3. Eliminar medico.
        4. Salir
        ''')
        opcion = int(input('> '))
        if opcion == 1:
            while True:
                mostrar_medicos()
                print('Ingrese 1 para volver Gestion :')
                opt = int(input('> '))
                if opt == 1:
                    break
        elif opcion == 2:
            print('--Busque un medico: ')
            busqueda = str(input('Ingrese el nombre del medico:'))
            medico = buscar_medico(busqueda)
            usuarios = mostrar_medico(medico)
            selec = selec_userM(usuarios)
            editar_medico(selec[0])
        elif opcion == 3:
            while True:
                busqueda = str(input('Busque un medico o salir para cerra este menu > '))
                if busqueda == 'salir':
                    break
                medico = buscar_medico(busqueda)
                usuarios = mostrar_medico(medico)
                selec = selec_userM(usuarios)
                eliminar_medico(selec[0])
        elif opcion == 4:
            break

#Utilidades de Gest_citas()
def registrar_cita():
    #Seleccionar paciente
    print('\nBusque un paciente')
    busqueda = input('Ingrese el nombre del paciente: ')
    paciente = buscar_paciente(busqueda)
    usuarios = mostrar_paciente(paciente)
    selec = selec_userP(usuarios)

    if selec == 'No valido':
        print('Paciente no valido.')
        return

    nombre_paciente = selec[0]

    #Seleccionar medico
    print('\nBusque un medico')
    busqueda = input('Ingrese el nombre del medico: ')
    medico = buscar_medico(busqueda)
    usuarios = mostrar_medico(medico)
    selec = selec_userM(usuarios)

    if selec == 'No valido':
        print('Medico no valido.')
        return

    nombre_medico = selec[0]
    #Validar fecha
    while True:
        fecha = input('\nIngrese la fecha de la cita (DD/MM/AAAA):' \
        '')
        try:
            fecha_valida = datetime.strptime(fecha,'%d/%m/%Y')
            break
        except ValueError:
            print('Fecha incorrecta.intente nuevamente.')
    #Validar hora
    while True:
        hora = input('Ingrese la hora de la cita (HH:MM): ')
        try:
            datetime.strptime(hora, '%H:%M')
            break
        except ValueError:
            print('Hora incorrecta, Utilice el formato HH:MM.')
        


    print('\n--Estado de la cita--')
    print('''
    1. Pendiente
    2. Confirmada
    3. Cancelada
    4. Completada
    ''')
    
    estados = {
        1: 'Pendiente',
        2: 'Confirmada',
        3: 'Cancelada',
        4: 'Completada'
    }
    while True:
        try:
            opcion = int(input('> '))
            if opcion in estados:
                estado = estados[opcion]
                break
            else:
                print('Opcion no valida. Intente de nuevo.')
        except ValueError:
            print('Ingresa un numero valido.')

            
    descripcion = input('Ingrese la descripcion de la cita: ')
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = "INSERT INTO CITAS (paciente, medico, fecha, hora, estado, descripcion) VALUES (?, ?, ?, ?, ?, ?)"
    
    cursor.execute(instruccion, (
        nombre_paciente,
        nombre_medico,
        fecha,
        hora,
        estado,
        descripcion
    ))
    conn.commit()
    cursor.close()
    conn.close()
    print('\n Cita registrada')

def mostrar_cita():
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    instruccion = "SELECT * FROM CITAS"
    cursor.execute(instruccion)

    citas = cursor.fetchall()

    cursor.close()
    conn.close()
    return citas

def listar_citas(citas):
    contador = 1
    print('\n --Citas Pendientes --')
    for cita in citas:
        print(f'''
        {contador}. ID: {cita[0]}
        Paciente: {cita[1]}
        Medico: {cita[2]}
        Fecha: {cita[3]}
        Hora: {cita[4]}
        Estado: {cita[5]}
        Descripcion: {cita[6]}
        ''')
        contador += 1
    return citas

def selec_cita(citas):
    if not citas:
        return 'No valido'

    seleccion = input('\nSeleccione el ID que desea editar: ')
    if not seleccion.isdigit():
        return 'No valido'

    for cita in citas:
        if cita[0] == int(seleccion):
            return cita
    return 'No valido'

def editar_cita(cita):
    campos = {
        '1': 'paciente',
        '2': 'medico',
        '3': 'fecha',
        '4': 'hora',
        '5': 'estado',
        '6': 'descripcion'
    }
    while True:
        print('\nQue dato desea modificar ?')
        print('''
        1. Paciente
        2. Medico
        3. Fecha
        4: Hora
        5: Estado
        6: Descripcion
        7: Volver
        ''')
        opcion = input('Selecciona una opcion: ')
        if opcion == '7':
            break

        if opcion not in campos:
            print('Opcion no valida.')
            continue

        campo = campos[opcion]

        nuevo_valor = input(f'Ingrese el nuevo valor para {campo}: ')
        ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
        conn = sql.connect(ruta_db)
        cursor = conn.cursor()
        instruccion = f"UPDATE CITAS SET {campo} = ? WHERE id_cita = ?"

        cursor.execute(instruccion, (nuevo_valor, cita[0]))

        conn.commit()
        cursor.close()
        conn.close()

        print('Cita actualizada correctamente.')


def cancelar_cita():

    citas = mostrar_cita()

    if not citas:
        print('No hay citas registradas.')
        return

    listar_citas(citas)

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
                "SELECT estado FROM CITAS WHERE id_cita = ?",
                (id_cita,)
            )

            cita = cursor.fetchone()

            if cita is None:
                print('No se encontró la cita.')
                continue

            if cita[0] == 'Cancelada':
                print('Esta cita ya está cancelada.')
                continue

            cursor.execute(
                "UPDATE CITAS SET estado = ? WHERE id_cita = ?",
                ('Cancelada', id_cita)
            )

            conn.commit()

            print('¡Cita cancelada correctamente!')

    finally:
        cursor.close()
        conn.close()


def citas_por_medico():

    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    try:
        while True:

            print('\n-- Busque un médico --')
            busqueda = input('Ingrese el nombre del médico (o salir): ')

            if busqueda.lower() == 'salir':
                print('Volviendo al menú...')
                break

            medico = buscar_medico(busqueda)

            if not medico:
                print('No se encontraron médicos.')
                continue

            usuarios = mostrar_medico(medico)
            selec = selec_userM(usuarios)

            if isinstance(selec, str):
                print('Selección no válida.')
                continue

            nombre_medico = selec[0]

            instruccion = """
            SELECT * FROM CITAS
            WHERE medico = ?
            ORDER BY fecha, hora
            """

            cursor.execute(instruccion, (nombre_medico,))
            citas = cursor.fetchall()

            if not citas:
                print(f'\nEl médico {nombre_medico} no tiene citas registradas.')
                continue

            print(f'\n-- Historial de citas de {nombre_medico} --')

            for cita in citas:
                print(f'\nID de cita: {cita[0]}')
                print(f'Paciente: {cita[1]}')
                print(f'Médico: {cita[2]}')
                print(f'Fecha: {cita[3]}')
                print(f'Hora: {cita[4]}')
                print(f'Estado: {cita[5]}')
                print(f'Descripción: {cita[6]}')
                print('-----------------------------------')

    finally:
        cursor.close()
        conn.close()

def mostrar_citas(nombre_medico=None):
    ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    if nombre_medico:
        instruccion = "SELECT * FROM CITAS WHERE medico = ?"
        cursor.execute(instruccion, (nombre_medico,))
    else:
        instruccion = "SELECT * FROM CITAS"
        cursor.execute(instruccion)

    citas = cursor.fetchall()

    cursor.close()
    conn.close()

    return citas

#Gestion de citas.
def Gest_citas():
    while True:
        print('Gestion de Citas.\nSeleccione una opcion: ')
        print('''
        1. Registrar cita.
        2. Editar cita.
        3. Cancelar cita
        4. Ver citas.
        5 . Salir.
        ''')
        selec = int(input('> '))
        if selec == 1:
            registrar_cita()
        if selec == 2:
            citas = mostrar_cita()
            listar_citas(citas)
            selec = selec_cita(citas)
            if selec == 'No valido':
                print('Cita no valida.')
                return
            editar_cita(selec)
        if selec == 3:
            
            cancelar_cita()

        if selec == 4:

            citas_por_medico()

        if selec == 5:
            break