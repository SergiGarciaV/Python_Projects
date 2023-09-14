from DispositivoEntrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contadorRatones=0

    def __init__(self,tipoDisp,marca):
        Raton.contadorRatones+=1
        self._idRaton=Raton.contadorRatones
        super().__init__(tipoDisp, marca)

    def __str__(self):
        return f'{DispositivoEntrada.__str__(self)} ----> ID= {self._idRaton}'#Al ser una clase heredada podríamos haber accedido directamente desde aquí a los valores de self._marca y self._tipodeentrada

    @property
    def idRaton(self):
        return self._idRaton

    @idRaton.setter
    def idRaton(self,id):
        self._idRaton=id


if __name__=='__main__':
    Raton1=Raton('Raton','Logitech')
    print(Raton1)

    Raton2=Raton('Raton','MXseries')
    print(Raton2)