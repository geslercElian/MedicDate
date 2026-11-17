#PROYECTO INTEGRADOR
#DESAROLLO DE UN PROGRAMA EN LNG PYTHON ENFOCADO EN LA GESTION DE CITAS MEDICAS EN PUESTOS DE SALUD DE LA CIUDAD DE LEON
import dataBase
import time
import getpass
import requests
import Admin
import Medico

#load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
#ruta = os.path.join(os.path.dirname(__file__), ".env")

#
while True:
    print("=====Bienvenido a MedicDate.=====")

    print(  '    =====Inicie sesion=====     '   )

    print("""
        SI ES ADMINISTRADOR INGRESE: 1
        SI ES MEDICO INGRESE: 2
        Cerrar PROGRAMA: 3
        """)

    #Selección de usuario para ingresar al sistema.

    num = int(input('Ingrese el número: '))

    #Entrada de usuario como administrador.

    if num == 1:
        admUser = str(input('Ingrese su usuario : '))

        admPassw = getpass.getpass('Ingrese su contraseña: ')
        #Acciones que puede realizar el usuario como administrador.
        if admUser == 'Gesler Calero' and admPassw == '123':

            print('Por favor espera....')
            time.sleep(3)
            print(f'Bienvenido {admUser}')
            while True:
            
                print(f'''
                Elija lo que desea hacer:
                1. Crear usuario (Paciente)
                2. Crear usuario (Médico)
                3. Gestionar Usuarios
                4. Citas
                5. Cerrar sesion.
                ''')
                #seleccion de la acción a realizar.
            
                accion = int(input('Ingrese el número de la acción que desea realizar: '))
                
                #Crear usuario paciente.
                if accion == 1:
                    
                    while True:
                        
                        print('Ingrese los datos del paciente o salir para terminar. ')
                        nombP = str(input('Nombre completo: '))
                        if nombP.lower() == 'salir':
                            break
                        contacto = str(input('Contacto: '))
                        edadP = str(input('Edad: '))
                        id = str(input('Identificación: '))
                        #Se ejecuta la función
                        Admin.insertFilaPC(nombP,contacto,id, edadP)
                        print(f'''
                            Usuario creado éxitosamente:
                            {nombP}
                            {contacto}
                            {edadP}
                            {id}
                            ''')
                        
                #Crear usuario médico.     
                elif accion == 2:
                    print('Ingrese los datos del médico: ')
                    nombM = str(input('Nombre completo: '))
                    esp = str(input('Especialidad del médico: '))
                    hor = str (input('Ingrese el horario del médico: '))
                    Admin.insertRowMd(nombM, esp, hor)
                    print(f'''
                        Nuevo médico creado:
                        Nombre: {nombM}
                        Especialida: {esp}
                        Horario: {hor}
                        ''')
                
                #Gestionar usuarios.
                elif accion == 3:
                    while True:
                        print('''
                    Seleccione con un numero la accion a realizar:
                    1. Gestionar Pacientes.
                    2. Gestionar Medicos.
                    3. Salir
                        
                    ''')
                        acc = int(input('>'))
                        
                        if acc == 1:
                            Admin.Gest_pacientes()
                        elif acc == 2:
                            Admin.Gest_medico()
                        elif acc == 3:
                            break
                #Reportes de citas.
                elif accion == 4:
                    Admin.Gest_citas()
                elif accion == 5:
                    break
        else:
            print('ACCESO DENEGADO.')

    #Entrada de usuario como médico.
    elif num == 2:
        MdUser = str(input('Ingrese su usuario : '))
        MdPassw = getpass.getpass('Ingrese su contraseña: ')
        if MdUser == 'Luis Vizcaya' and MdPassw == '321':
                print(f'Bienvendo {MdUser}')
                while True:
                    print(f'''
                    Elija lo que desea hacer:
                    1. Crear Cita.
                    2. Ver citas.
                    3. Cancelar cita.
                    4. Editar cita.
                    5. Cerrar sesion.
                ''')
                    accion = int(input('Ingrese el número de la acción que desea ralizar: '))

                    if accion == 1:
                        Medico.registrar_cita_medico(MdUser)
                    if accion == 2:
                        Medico.mostrar_citas_medico(MdUser)
                    elif accion == 3:
                        Medico.cancelar_cita_medico(MdUser)
                    elif accion == 4:
                        citas = Admin.mostrar_citas(MdUser)
                        Admin.listar_citas(citas)
                        selec = Admin.selec_cita(citas)
                        Medico.editar_cita_medico(selec, MdUser)
                    elif accion == 5:
                        break
    elif num == 3:
        break
                