from Conexion import Conexion
from LoggerBase import log


class CursorDelPool:

    def __init__(self):
        self._conexion=None
        self._cursor=None


    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion=Conexion.obtenerConexion()#Obtenemos la conexión a través del método obtenerConexion() del módulo Conexiones que a sunvez llama al método poolConexiones() para obtener esa conexión.
        self._cursor=self._conexion.cursor()#Obtenemos el cursor sobre la conexión que hay establecida, a partir del método base .cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valorExcepcion, traceback):#Hay que pasarle el 1º tipo de excepción, 2º el valor de la excepción y 3º el detalle de la excepción o traceback
        log.debug('Se ejecuta método __exit__')
        if valorExcepcion:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepcion, se activa rollback: {valorExcepcion} {traceback}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()#cerramos el cursor
        Conexion.liberarConexion(self._conexion)#liberamos el objeto conexión de vuelta al pool.


if __name__=='__main__':
    with CursorDelPool() as cursor: #al poner el with, de forma automática se inicia el __init__ y luego el __enter__
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())