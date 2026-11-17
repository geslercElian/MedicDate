import sqlite3 as sql
import os
from dotenv import load_dotenv
from datetime import datetime
import Admin

#Utilidades de registrar_cita_medico()

#Registro de citas.
def registrar_cita_medico(nombre_medico):

    # Seleccionar paciente
    while True:
        print('\nBusque un paciente')
        busqueda = input('Ingrese el nombre del paciente o ingrese salir para regresar al menu: ')
        paciente = Admin.buscar_paciente(busqueda)
        usuarios = Admin.mostrar_paciente(paciente)
        selec = Admin.selec_userP(usuarios)
        if busqueda == 'salir':
            break

        if selec == 'No valido':
            print('Paciente no valido.')
            return

        nombre_paciente = selec[0]

        # Validar fecha
        while True:
            fecha = input('\nIngrese la fecha de la cita (DD/MM/AAAA): ')
            try:
                datetime.strptime(fecha, '%d/%m/%Y')
                break
            except ValueError:
                print('Fecha incorrecta. Intente nuevamente.')

        # Validar hora
        while True:
            hora = input('Ingrese la hora de la cita (HH:MM): ')
            try:
                datetime.strptime(hora, '%H:%M')
                break
            except ValueError:
                print('Hora incorrecta. Utilice el formato HH:MM.')

        # Estado de la cita
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

        instruccion = """
        INSERT INTO CITAS
        (paciente, medico, fecha, hora, estado, descripcion)
        VALUES (?, ?, ?, ?, ?, ?)
        """

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

        print('\n¡Cita registrada correctamente!')

#Muestra las citas del medico activo en la sesion.
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

#Cancelar cita por medico.
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

#Editar citas.
def editar_cita_medico(cita, nombre_medico):
    campos = {
        '1': 'fecha',
        '2': 'hora',
        '3': 'estado',
        '4': 'descripcion'
    }

    while True:
        print('''
        ¿Qué dato desea modificar?

        1. Fecha
        2. Hora
        3. Estado
        4. Descripcion
        5. Volver
        ''')

        opcion = input('Selecciona una opcion: ')

        if opcion == '5':
            break

        if opcion not in campos:
            print('Opcion no valida.')
            continue

        campo = campos[opcion]

        nuevo_valor = input(f'Ingrese el nuevo valor para {campo}: ')

        ruta_db = os.path.join(os.path.dirname(__file__), 'usuarios.db')
        conn = sql.connect(ruta_db)
        cursor = conn.cursor()

        try:
            instruccion = f'''
            UPDATE CITAS
            SET {campo} = ?
            WHERE id_cita = ? AND medico = ?
            '''

            cursor.execute(instruccion, (nuevo_valor, cita[0], nombre_medico))

            conn.commit()

            if cursor.rowcount > 0:
                print('Cita actualizada correctamente.')
            else:
                print('No se pudo actualizar la cita.')

        finally:
            cursor.close()
            conn.close()