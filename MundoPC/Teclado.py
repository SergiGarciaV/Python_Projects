from DispositivoEntrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contadorTeclados=0

    def __init__(self,marca,tipoDisp):
        Teclado.contadorTeclados+=1
        self._idTeclado=Teclado.contadorTeclados
        super().__init__(marca,tipoDisp)#Siempre que estemos en una clase heredada "ej: class Teclado(DispositivoEntrada)" tenemos que poner el init padre dentro del init hijo y pasar los argumentos


    def __str__(self):
        return f' ----> ID={self._idTeclado}{DispositivoEntrada.__str__(self)}'#Al ser una clase heredada podríamos haber accedido directamente desde aquí a los valores de self._marca y self._tipodeentrada

    @property
    def idTeclado(self):
        return self._idTeclado

    @idTeclado.setter
    def idTeclado(self,id):
        self._idTeclado=id


if __name__=='__main__':
    Teclado1=Teclado('Microsoft','Teclado')
    print(Teclado1)

    Teclado2=Teclado('Corsair','Teclado')
    print(Teclado2)