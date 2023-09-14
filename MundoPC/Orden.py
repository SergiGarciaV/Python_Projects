from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora

class Orden:

    listaComputadoras=[]
    contador_ordenes=0

    def __init__(self,compu):
        Orden.contador_ordenes+=1
        self._idOrden=Orden.contador_ordenes
        self._listCompus=compu


    def __str__(self):
        stringListaComps=''
        for comp in self._listCompus:
            stringListaComps+=comp.__str__()
        return f'\n\nNºOrden={self._idOrden}\n----------------------------------------------------------------------------------------{stringListaComps}'

    def agregarComputadora(self,computadora):
        self._listCompus.append(computadora)

    @property
    def listCompus(self):
        return self._listCompus

    @listCompus.setter
    def listCompus(self,lista):
        self._listCompus=lista

Teclado1 = Teclado('Huawei', 'Teclado cableado')
Raton1 = Raton('Microsoft', 'Ratón WIFI')
Monitor1 = Monitor('Huawei', 27)
Computadora1 = Computadora('Apple',Monitor1,Raton1,Teclado1)

Raton2=Raton('LG','Ratón bluetooth')
Teclado2=Teclado('Teclado WIFI','Dell')
Monitor2 = Monitor('Acer', 23.4)
Computadora2 = Computadora('Samsung',Monitor2,Raton2,Teclado2)

Teclado1 = Teclado('Trust', 'Teclado cableado')
Raton1 = Raton('AppleMagic', 'Ratón WIFI')
Monitor1 = Monitor('HP', 34)
Computadora3 = Computadora('Asus', Monitor1, Raton1, Teclado1)

Teclado1 = Teclado('Logitech', 'Teclado cableado')
Raton1 = Raton('Creative', 'Ratón WIFI')
Monitor1 = Monitor('MSI', 27)
Computadora4 = Computadora('HP', Monitor1, Raton1, Teclado1)


listaOrden1=[Computadora1,Computadora3]
Orden1=Orden(listaOrden1)


listaOrden2=[Computadora2,Computadora4]
Orden2=Orden(listaOrden2)
print(Orden2)

Orden1.agregarComputadora(Computadora3)#Una vez creado un objeto 'orden', podemos usar el método de la misma clase (orden) para agregar otra computadora a la orden1 .
print(Orden1)