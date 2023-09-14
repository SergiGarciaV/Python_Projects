from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado

class Computadora:

    contCompu = 0

    def __init__(self, nombre, Monitor, Raton, Teclado):
         Computadora.contCompu += 1
         self._idComputadora = Computadora.contCompu
         self.nombre = nombre
         self.Monitor=Monitor
         self.Raton=Raton
         self.Teclado=Teclado

    def __str__(self):
        return f'''
                \n\t\t\tComputadora ----> ID={self._idComputadora} ----> Nombre={self.nombre}\n\t\t\t{self.Monitor}\t\t\tTeclado{self.Teclado}
            Raton:{self.Raton}\n\n----------------------------------------------------------------------------------------
                '''#No es necesario especificar que estámos llamando a los métodos __Str__ de cada clase, al hacer la llamada a las clases Monitor,Teclado y Raton, ya se está llamando al metodo __str__ de cada una de ellas de forma automática. Si que deben de importarse al principio del archivo from MundoPC.Monitor import Monitor....

    @property
    def idComputadora(self):
        return self._idComputadora

    @idComputadora.setter
    def idComputadora(self,idComp):
        self._idComputadora=idComp

if __name__ == '__main__':
    Teclado1 = Teclado('Huawei', 'Teclado cableado')
    Raton1 = Raton('Microsoft', 'Ratón WIFI')
    Monitor1 = Monitor('Huawei', 27)
    Computadora1 = Computadora('Apple',Monitor1,Raton1,Teclado1)
    print(Computadora1)

    Raton2=Raton('LG','Ratón bluetooth')
    Teclado2=Teclado('Teclado WIFI','Dell')
    Monitor2 = Monitor('Acer', 23.4)
    Computadora2 = Computadora('Samsung',Monitor2,Raton2,Teclado2)
    print(Computadora2)

    Teclado1 = Teclado('Trust', 'Teclado cableado')
    Raton1 = Raton('AppleMagic', 'Ratón WIFI')
    Monitor1 = Monitor('HP', 34)
    Computadora3 = Computadora('Asus', Monitor1, Raton1, Teclado1)
    print(Computadora3)

    Teclado1 = Teclado('Logitech', 'Teclado cableado')
    Raton1 = Raton('Creative', 'Ratón WIFI')
    Monitor1 = Monitor('MSI', 27)
    Computadora4 = Computadora('HP', Monitor1, Raton1, Teclado1)
    print(Computadora4)