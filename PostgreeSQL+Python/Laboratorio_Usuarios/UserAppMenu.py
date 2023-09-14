import sys

from UserDAO import UserDAO



def inicio():
    print('''Introduzca el valor deseado:\n\n
    1- Crear nuevo usuario\n
    2- Modificar usuario\n
    3- Eliminar usuario\n
    4- Listar todos los usuarios\n
    5- Salir\n''')
    print('Eleccion:')
    opcion=int(input())
    if opcion == 1:
        UserDAO.insert()
        inicio()
    elif opcion == 2:
        UserDAO.update()
        inicio()
    elif opcion == 3:
        UserDAO.delete()
        inicio()
    elif opcion == 4:
        users = UserDAO.select()
        for user in users:
            print(user)
        inicio()
    elif opcion == 5:
        sys.exit()
    else:
        inicio()

inicio()