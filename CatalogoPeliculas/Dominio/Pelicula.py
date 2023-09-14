class Pelicula:
    linesCount=0

    def __init__(self,nombre):
        Pelicula.linesCount+=1
        self.numFila=Pelicula.linesCount
        self._nombre=nombre

    def __str__(self):

        return f'{self.numFila}- NombrePelicula= {self._nombre}\n'


if __name__=='__main__':
    Pelicula1=Pelicula('JurasicPark')
    print(Pelicula1)