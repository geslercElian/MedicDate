#PROYECTO INTEGRADOR
#DESAROLLO DE UN PROGRAMA EN LNG PYTHON ENFOCADO EN LA GESTION DE CITAS MEDICAS EN PUESTOS DE SALUD DE LA CIUDAD DE LEON

import  Medico, Admin, mensajes, sqlite3

conexion = sqlite3.connect('dataBase.db')


print("BIENVENID@ AL SISTEMA DE GESTION DE CITAS MEDICAS")

Usuario = str(input('Ingrese su usuario: '))

contraseña = str(input('Ingrese su contraseña'))



