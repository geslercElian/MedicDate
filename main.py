#PROYECTO INTEGRADOR
#DESAROLLO DE UN PROGRAMA EN LNG PYTHON ENFOCADO EN LA GESTION DE CITAS MEDICAS EN PUESTOS DE SALUD DE LA CIUDAD DE LEON

#import  Medico, Admin, mensajes, sqlite3

print("=====Bienvenido a MedicDate.=====")

print(  '=====Inicie sesion====='   )

print("""
        SI ES ADMIN INGRESE '1'
        SI ES MEDICO INGRESE '2'
    """)


num = int(input('Ingrese el numero: '))


if num == 1:
    admUser = str(input('Ingrese su usuario : '))
    admPassw = str(input('Ingrese su contraseña: '))
    if admUser == 'Gesler Calero' and admPassw == '123':
        print(f'''
        Bienvendo {admUser}
        Elija lo que desea hacer:
        1. Crear usuario (Paciente)
        2. Crear usuario (Medico)
        3. Gestionar Usuarios
        4. Reportes de citas
        ''')
    
        accion = int(input('Ingrese el numero de la accion que desea ralizar: '))
        if accion == 1:
            print('Ingrese los datos del paciente:')
            nombP = str(input('Nombre completo:'))
            contacto = str(input('Contacto: '))
            edadP = str(input('Edad: '))
            id = str(input('Identificacion: '))
            print(f'''
                Usuario creado exitosamente:
                {nombP}
                {contacto}
                {edadP}
                {id}
                ''')
            
        elif accion == 2:
            print('Ingrese los datos del medico: ')
            nombM = str(input('Nombre completo: '))
            esp = str(input('Especialidad del medico: '))
            hor = str (input('Ingrese el horario del medico: '))
            print(f'''
                Nuevo medico creado:
                Nombre: {nombM}
                Especialida: {esp}
                Horario: {hor}
                ''')

        elif accion == 3:
            print('Funcion en desarrollo')

        elif accion == 4:
            print('Funcion en desarrollo')
    else:
         print('ACCESO DENEGADO.')

elif num == 2:
    MdUser = str(input('Ingrese su usuario : '))
    MdPassw = str(input('Ingrese su contraseña: '))
    if MdUser == 'Gesler Calero' and MdPassw == '123':
            print(f'''
            Bienvendo {MdUser}
            Elija lo que desea hacer:
            1. Agendar Cita.
            2. Confirmar Asistencia.
            3. Cancelar Cita
            4. Historial de paciente.
        ''')
            accion = int(input('Ingrese el numero de la accion que desea ralizar: '))
