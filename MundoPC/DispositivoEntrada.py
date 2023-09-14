class DispositivoEntrada:

    opcio=0

    def __init__(self, marca, tipoEntrada):
        self._tipoEntrada=str(tipoEntrada)
        self._marca=str(marca)


    def __str__(self):
            return f' ----> Marca= {self.marca} ----> Tipo Entrada={self.tipoEntrada}'


    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self,tipoEntrada):
        self._tipoEntrada=tipoEntrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca=marca