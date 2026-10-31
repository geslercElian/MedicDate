#PROYECTO INTEGRADOR
#DESAROLLO DE UN PROGRAMA EN LNG PYTHON ENFOCADO EN LA GESTION DE CITAS MEDICAS EN PUESTOS DE SALUD DE LA CIUDAD DE LEON
import dataBase

print("=====Bienvenido a MedicDate.=====")

print(  '    =====Inicie sesion=====     '   )

print("""
      SI ES ADMIN INGRESE '1'
      SI ES MEDICO INGRESE '2'
    """)

#Selección de usuario para ingresar al sistema.
num = int(input('Ingrese el número: '))

#Entrada de usuario como administrador.
if num == 1:
    admUser = str(input('Ingrese su usuario : '))

    admPassw = str(input('Ingrese su contraseña: '))
    #Acciones que puede realizar el usuario como administrador.
    if admUser == 'Gesler Calero' and admPassw == '123':
        print(f'''
        Bienvendo {admUser}
        Elija lo que desea hacer:
        1. Crear usuario (Paciente)
        2. Crear usuario (Médico)
        3. Gestionar Usuarios
        4. Reportes de citas
        ''')
        #seleccion de la acción a realizar.
        accion = int(input('Ingrese el número de la acción que desea realizar: '))
        #Crear usuario paciente.
        if accion == 1:
            
            while True:
                
                print('Ingrese los datos del paciente o salir. ')
                nombP = str(input('Nombre completo: '))
                if nombP.lower() == 'salir':
                    break
                contacto = str(input('Contacto: '))
                edadP = str(input('Edad: '))
                id = str(input('Identificación: '))
                #Se ejecuta la función
                dataBase.insertFilaPC(nombP,contacto,id, edadP)
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
            dataBase.insertRowMd(nombM, esp, hor)
            print(f'''
                Nuevo médico creado:
                Nombre: {nombM}
                Especialida: {esp}
                Horario: {hor}
                ''')
        
        #Gestionar usuarios.
        elif accion == 3:
            busUser = str(input('Busque un usuario : '))
            paciente, medico = dataBase.buscar_usuario(busUser)
            usuarios = dataBase.mostrar_user(paciente, medico)
            usuario = dataBase.selecionar_user(usuarios)
            tipo = dataBase.tipo_user(usuario)
            dataBase.mostrar_campos(usuario)
            campo = dataBase.selecionar_campos(usuario)
        
        #Reportes de citas.
        elif accion == 4:
            print('Funcion en desarrollo')
    else:
         print('ACCESO DENEGADO.')

#Entrada de usuario como médico.
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
            accion = int(input('Ingrese el número de la acción que desea ralizar: '))
