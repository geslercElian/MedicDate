
# PROYECTO INTEGRADOR
# DESARROLLO DE UN PROGRAMA EN LENGUAJE PYTHON
# ENFOCADO EN LA GESTION DE CITAS MEDICAS
# EN PUESTOS DE SALUD DE LA CIUDAD DE LEON

import dataBase
import time
import getpass
import requests
import Admin
import Medico

intentos = 0

while True:

    print("===== Bienvenido a MedicDate =====")

    print("""
    1. Iniciar sesión
    2. Cerrar programa
    """)

    num = int(input('Ingrese el número: '))

    # INICIO DE SESION
    if num == 1:

        usuario = input('Ingrese su usuario: ')
        password = getpass.getpass('Ingrese su contraseña: ')

        # VALIDAR CREDENCIALES
        resultado = dataBase.validar_login(usuario, password)

        if resultado:

            intentos = 0

            rol = resultado[2]
            medico = resultado[3]

            print('Por favor espera...')
            time.sleep(3)

            # MENU ADMINISTRADOR
            if rol == 'admin':

                print(f'Bienvenido {usuario}')

                while True:

                    print('''
                    Elija lo que desea hacer:

                    1. Crear usuario (Paciente)
                    2. Crear usuario (Médico)
                    3. Gestionar Usuarios
                    4. Citas
                    5. Cerrar sesión.
                    ''')

                    accion = int(input(
                        'Ingrese el número de la acción que desea realizar: '
                    ))

                    # CREAR PACIENTE
                    if accion == 1:

                        while True:

                            print('Ingrese los datos del paciente o salir para terminar.')

                            nombP = input('Nombre completo: ')

                            if nombP.lower() == 'salir':
                                break

                            contacto = input('Contacto: ')
                            edadP = input('Edad: ')
                            identificacion = input('Identificación: ')

                            Admin.insertFilaPC(
                                nombP,
                                contacto,
                                identificacion,
                                edadP
                            )

                            print(f'''
                            Usuario creado éxitosamente:
                            {nombP}
                            {contacto}
                            {edadP}
                            {identificacion}
                            ''')

                    # CREAR MEDICO
                    elif accion == 2:

                        print('Ingrese los datos del médico: ')

                        nombM = input('Nombre completo: ')
                        esp = input('Especialidad del médico: ')
                        hor = input('Ingrese el horario del médico: ')

                        Admin.insertRowMd(nombM, esp, hor)

                        print(f'''
                        Nuevo médico creado:
                        Nombre: {nombM}
                        Especialidad: {esp}
                        Horario: {hor}
                        ''')

                    # GESTIONAR USUARIOS
                    elif accion == 3:

                        while True:

                            print('''
                            Seleccione con un número la acción a realizar:

                            1. Gestionar Pacientes.
                            2. Gestionar Médicos.
                            3. Salir
                            ''')

                            acc = int(input('>'))

                            if acc == 1:
                                Admin.Gest_pacientes()

                            elif acc == 2:
                                Admin.Gest_medico()

                            elif acc == 3:
                                break

                    # GESTIONAR CITAS
                    elif accion == 4:
                        Admin.Gest_citas()

                    # CERRAR SESION
                    elif accion == 5:
                        break

            # MENU MEDICO
            elif rol == 'medico':

                MdUser = medico

                if MdUser is None:
                    print('La cuenta no tiene un médico asociado.')
                    continue

                print(f'Bienvenido {MdUser}')

                while True:

                    print('''
                    Elija lo que desea hacer:

                    1. Crear Cita.
                    2. Ver citas.
                    3. Cancelar cita.
                    4. Editar cita.
                    5. Cerrar sesión.
                    ''')

                    accion = int(input(
                        'Ingrese el número de la acción que desea realizar: '
                    ))

                    # CREAR CITA
                    if accion == 1:
                        Medico.registrar_cita_medico(MdUser)

                    # VER CITAS
                    elif accion == 2:
                        Medico.mostrar_citas_medico(MdUser)

                    # CANCELAR CITA
                    elif accion == 3:
                        Medico.cancelar_cita_medico(MdUser)

                    # EDITAR CITA
                    elif accion == 4:

                        citas = Admin.mostrar_citas(MdUser)
                        Admin.listar_citas(citas)

                        selec = Admin.selec_cita(citas)

                        if selec:
                            Medico.editar_cita_medico(selec, MdUser)

                    # CERRAR SESION
                    elif accion == 5:
                        break

            # ROL NO RECONOCIDO
            else:
                print('Rol no reconocido.')

        # CREDENCIALES INCORRECTAS
        else:

            intentos += 1

            print('Usuario o contraseña incorrectos.')
            print(f'Intentos fallidos: {intentos}/3')

            if intentos == 3:

                print('Demasiados intentos fallidos.')
                print('MedicDate permanecerá suspendido durante 1 minuto.')

                time.sleep(60)

                intentos = 0

                print('Suspensión finalizada. Puede volver a intentarlo.')

    # CERRAR PROGRAMA
    elif num == 2:

        print('Cerrando MedicDate...')
        break
