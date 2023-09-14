from Dominio.Pelicula import Pelicula
import os


class CatalogoPeliculas:
    listaPelis = []
    CatalogoActual = ''
    listaCatalogos = []
    idCatalogo = -1

    @classmethod
    def crearCatalogo(cls, nombreCatalogo):
        cls.idCatalogo += 1
        cls.CatalogoActual = str(cls.idCatalogo) + '-' + nombreCatalogo
        cls.listaCatalogos.append(str(cls.idCatalogo) + '-' + nombreCatalogo)
        with open('C:\\Users\\sergi\\Desktop\\' + (str(cls.idCatalogo) + '-' + nombreCatalogo) + '.txt', 'a',
                  encoding='utf8') as archivo:
            print(f'El archivo del catálogo {nombreCatalogo} ha sido creado')

    @classmethod
    def listaCat(cls):
        listaCat = cls.listaCatalogos
        return print(listaCat)

    @classmethod
    def seleccionarCatalogo(cls, indiceCatalogo):
        cls.CatalogoActual = cls.listaCatalogos[indiceCatalogo]
        return print(f'El catálogo seleccionado es= {cls.CatalogoActual}')

    @classmethod
    def agregarPelicula(cls, Peli):
        with open('C:\\Users\\sergi\\Desktop\\' + str(cls.CatalogoActual) + '.txt', 'a', encoding='utf8') as archivo:
            archivo.write(f'\n{Peli}')

    @classmethod
    def listarPeliculas(cls):
        with open('C:\\Users\\sergi\\Desktop\\' + str(cls.CatalogoActual) + '.txt', 'r', encoding='utf8') as archivo:
            for pelicula in archivo:
                print(pelicula)

    @classmethod
    def eliminarPelicula(cls, numFila):
        with open('C:\\Users\\sergi\\Desktop\\' + str(cls.CatalogoActual) + '.txt', 'r', encoding='utf8') as archivo:
            filas = archivo.readlines()
        with open('C:\\Users\\sergi\\Desktop\\' + str(cls.CatalogoActual) + '.txt', 'w', encoding='utf8') as archivo:
            fila = filas[numFila - 1]
            filas.remove(fila)
            for fila in filas:
                archivo.write(fila)


@classmethod
def eliminarArchivo(cls):
    os.remove('C:\\Users\\sergi\\Desktop\\' + str(cls.CatalogoActual) + '.txt')


if __name__ == '__main__':
    CatalogoPeliculas1 = CatalogoPeliculas()
    CatalogoPeliculas1.crearCatalogo('Accion')
    CatalogoPeliculas2 = CatalogoPeliculas()
    CatalogoPeliculas2.crearCatalogo('Drama')
    print(CatalogoPeliculas.listaCatalogos)