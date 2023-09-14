import sys
from psycopg2 import pool #Importamos el modulo pool de psycopg2
from LoggerBase import log

class Conexion:

    _DATABASE='Users'
    _USERNAME='postgres'
    _PASSWORD='root'
    _DB_PORT='5432'
    _HOST='localhost'
    _MIN_CON=1#Variable que indica el nº mínimo de objetos conexión del pool.
    _MAX_CON=5#Variable que indica el nº máximo de objetos conexión en el pool de conexiones.
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool=pool.SimpleConnectionPool(cls._MIN_CON, #Hacemos el mismo proceso que al realizar una conexión pero sobre cls._pool=pool.SimpleConnectionPool y añadiendo 1º el minimo/máximo de objetos de tipo conexión
                                                    cls._MAX_CON,
                                                    host=cls._HOST,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    port=cls._DB_PORT,
                                                    database=cls._DATABASE
                                                    )
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
            conexion=cls.obtenerPool().getconn()#Le pasamos al cliente un objeto del pool de conexiones para que tenga acceso a la DB
            log.debug(f'Conexion obtenida del pool: {conexion}')
            return conexion

    @classmethod
    def liberarConexion(cls, conexion):#Cuando el cliente acaba con sus consultas/acciones sobre la DB debe llamar a este método para liberar la conexión de nuevo al pool
        cls.obtenerPool().putconn(conexion)#Llamamos al método obtenerPool() que nos devolverá un objeto de tipo conexión, y le decimos con el .putconn que lo devuelva al pool de conexiones.
        log.debug(f'Devolvemos la conexión al pool: {conexion}')


    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()#Cierra todas las conexiones del pool.


if __name__=='__main__': #Ojo estámos accediendo a los métodos mediante la clase en si 'Conexion' no hace falta crear objetos para acceder ya que son todos métodos de clase.

    conexion1=Conexion.obtenerConexion()#Damos una conexión
    Conexion.liberarConexion(conexion1)#Liberamos la conexión que habiamos dado