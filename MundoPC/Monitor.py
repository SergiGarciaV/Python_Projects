class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contador_monitores += 1
        self._idMonitor = Monitor.contador_monitores
        self._marca = marca
        self._tamano = tamaño

    def __str__(self):
        return f'Monitor ----> ID={self._idMonitor} ----> Marca={self._marca} ----> tamano={self._tamano}\n'

    @property
    def idMonitor(self):
        return self._idMonitor

    @idMonitor.setter
    def idMonitor(self, idMonitor):
        self._idMonitor = idMonitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano


if __name__ == '__main__':
    Monitor1 = Monitor('Toshiba', 27)
    print(Monitor1)

    Monitor2 = Monitor('ASUS', 32)
    print(Monitor2)
