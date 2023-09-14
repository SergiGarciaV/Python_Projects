from Servicio.CatalogoPeliculas import CatalogoPeliculas as cp #No es muy conveniente renombrar el nombre de la clase que se importa.
from Dominio.Pelicula import Pelicula
import os

class inicio():


    def inici(self):

        print('Introduce el número de opción y pulsa enter:'.center(50, '-'))
        print('''
                                     1) Agregar película
                                     2) Listar Películas
                                     3) Eliminar película de la lista
                                     4) Eliminar archivo de películas
                                     5) Crear catálogo de películas
                                     6) Listar catálogos de películas
                                     7) Salir
                       ''')
        try:
            opcion = int(input())
            if opcion == 1:

                if cp.listaCatalogos==[]:
                    print('Debes crear antes un catalogo de películas!!\n')
                    print('Introduce un nombre para el nuevo catálogo:')
                    cp.crearCatalogo(input())
                    print('Introduce ahora el nombre de la película que quieres agregar:')
                    cp.agregarPelicula(input())
                    print('Volviendo al menú principal')
                    Arranque.inici()
                else:
                    print(f'Introduce el número de catálogo al que quieres agregar películas:')
                    cp.listaCat()
                    electCata=int(input())
                    cp.seleccionarCatalogo(electCata)
                    print('Introduce ahora el nombre de la película que quieres agregar:')
                    cp.agregarPelicula(input())
                    Arranque.inici()
               # cp.seleccionarCatalogo(catalogo)
                #catalogoPeliculas1.agregarPelicula(input())

            elif opcion == 2:
                if os.stat('C:\\Users\\sergi\\Desktop\\' + str(cp.CatalogoActual) + '.txt').st_size == 0:
                    print('No hay ninguna película en el archivo\n')
                    Arranque.inici()
                else:
                    cp.listarPeliculas()
                    print('Volviendo al menú principal')
                    Arranque.inici()

            elif opcion == 3:
                print('Introduce el numero de fila de la película a borrar: ')
                cp.listarPeliculas()
                cp.eliminarPelicula(input())
                print('Volviendo al menú principal')
                Arranque.inici()

            elif opcion == 4:

                print('Introduce el numero del catálogo/archivo a Eliminar:')
                cp.listaCat()
                cp.seleccionarCatalogo(int(input()))
                cp.eliminarArchivo()
                print('Catálogo eliminado')
                print('Volviendo al menú principal')
                Arranque.inici()

            elif opcion == 5:

                print('Introduce el nombre del catálogo/archivo a crear:')
                cp.crearCatalogo(input())
                print('Volviendo al menú principal')
                Arranque.inici()

            elif opcion == 6:
                cp.listaCat()
                print('Volviendo al menú principal')
                Arranque.inici()

            elif opcion == 7:
                print('Hasta la proxima!')
                quit()

        except Exception as e:
            print(f'Ha sucedido un error: {e}')
            Arranque.inici()





Arranque=inicio()
Arranque.inici()