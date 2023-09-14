# Aquí realizaremos las operaciones CRUD:
#    -Create--> Insert
#    -Read --> Select
#    -Update --> Update
#    -Delete --> Delete


# DAO(Data Acces Object)
import sys

from CursorDelPool import CursorDelPool
from LoggerBase import log
from Conexion import Conexion
from User import User


class UserDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY user_id'
    _INSERTAR = 'INSERT INTO usuario (name, last_name, email) VALUES(%s, %s, %s)'  # No estamos insertando el id, porque sabemos que es autoincrementable
    _ACTUALIZAR = 'UPDATE user SET name=%s, last_name=%s, email=%s WHERE user_id=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE user_id=%s'
    _SELECCIONporID='SELECT * FROM usuario WHERE user_id=%s'


    @classmethod
    def _newUser(cls):
        user=User(nom=input('Introduce el name: '), apellido=input('Introduce el lastName: '),
                          email=input('Introduce el email: '))
        return user

    @classmethod
    def select(cls):
        with CursorDelPool() as cur:
            print('ALL USERS IN:'.center(50, '-'))
            cur.execute(cls._SELECCIONAR)
            registros = cur.fetchall()
            users = []  # creamos una lista
            for registro in registros:
                user=User(registro[0], registro[1], registro[2], registro[3])
                users.append(user)  # Agregamos la persona creada a la lista
            return users

    @classmethod
    def _selectOne(cls,id):
        with CursorDelPool() as cur:
            cur.execute(cls._SELECCIONporID,id)#Ejecutamos el código SQL de _SELECCIONporID
            registros = cur.fetchall()
            users = []  # creamos una lista
            for registro in registros:
                user=User(registro[0], registro[1], registro[2], registro[3])  # Pongo el 3 primero porque en mi postgree tengo el ID en la 4ª posición de las columnas de persona
                users.append(user)  # Agregamos la persona creada a la lista
            return users







    @classmethod
    def insert(cls):
        with CursorDelPool() as cur:
            print('NEW USER'.center(50, '-'))
            user = cls._newUser()
            valores = (user.name, user.last_name, user.email)
            cur.execute(cls._INSERTAR, valores)
            log.debug(f'Persona Introducida con exito --> Nombre={user.name} \nApellido={user.last_name} \nEmail={user.email}')
            print('USER CREATE END'.center(50, '-'))
            return cur.rowcount


    @classmethod
    def update(cls):
        with CursorDelPool() as cur:
            print('USER UPDATE'.center(50, '-'))
            print('Introduce los siguientes datos actualizados:')
            user=cls._newUser()
            valores=(user.name, user.last_name, user.email, input('Ahora introduce el id de la user a la que se aplicarán estos valores:'))
            cur.execute(cls._ACTUALIZAR, valores)
            log.debug(
                f'Persona actualizada con exito --> Nombre={user.name}\nApellido={user.last_name}\nEmail={user.email}\nid={user.user_id}'),
            print('USER UPDATE END\n'.center(50, '-'))


    @classmethod
    def delete(cls):

        with CursorDelPool() as cur:
            print('USER DELETE'.center(50, '-'))
            id = input('Introduce la ID de la user a eliminar de la Base de datos: ')
            print('\n La user a eliminar es:')
            user = cls._selectOne((id,))  # Pasamos el id introducido al método _selectOne() , ya le hemos puesto la _ para que se sepa que no se debe acceder directamente a el (se accederá a partir de este método, delete()), para que se pueda trabajar bien con el .cursor hay que convertir la id a una tupla, ya que es la unica manera de trabajar con el cursor.execute.
            for users in user:
                print(users)
            verificar = input('Introduzca \'1\' si es correcto, para eliminar, de lo contrario introduzca \'2\':  ')
            if verificar == '1':
                CursorDelPool()
                cur.execute(cls._ELIMINAR, (id,))
                log.debug(
                    f'Usuario con id={id} eliminada con exito'),
                print('DELETE USER END'.center(50, '-'))
            else:
                cls.delete()


if __name__ == '__main__':


     UserDAO.insert()

     UserDAO.delete()

     users=UserDAO.select()
     for user in users:
         print(user)

     Conexion.cerrarConexiones()#Después de las ejecuciones que se quieran realizar en un momento dado , hay que cerrar la conexión.