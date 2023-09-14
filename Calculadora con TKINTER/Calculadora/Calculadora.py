import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('510x540+650+340')
        self.title('Calculadora')
        self.iconbitmap('icon.ico')
        self.resizable(0,0)


        self.expresion = ''#Variable de clase
        self.entrada = None#Variable de clase que será una caja de texto (input)
        self.entrada_texto = tk.StringVar()#StringVar , lo utilizamos para obtener el valor del input

        self._crearComponentes()

    def _limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _total(self):
        try:
            if self.expresion:#este if lo ponemos porque si clickamos en igual con la cadena vacia devolverá error, así lo evitamos , diciendo que solo ejecute en caso de que la cadena sea True
                resultado = eval(self.expresion)
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error: {e}')
            self.entrada_texto.set('')#Si se da un error como pedir resultado de unicamente el carácter '*'... pone vacia la calculadora
        finally:
            self.expresion = ''  # Tras obtener el resultado, si se pulsa cualquier tecla la pondrá sobre la caja de entrada_texto ya limpia, porque habrá acudido al método _addValue y se añadirá el valor que hayamos clickado sobre la cadena vaciada.
    def _addValue(self, tecla):
        #Concatenamos la nueva tecla clickada a la expresion ya existente
        self.expresion = self.expresion+tecla #Esto también se podría hacer con la siguiente expresión: self.expresion = f'{self.expresion}{tecla} --> Así también se concatena el str
        self.entrada_texto.set(self.expresion)

    def _crearComponentes(self):

        frameEntrada = tk.Frame(self, width=507, height=50, bg='grey')
        frameEntrada.pack(side=tk.TOP)

        Entrada = tk.Entry(frameEntrada, font="Helvetica 24", textvariable=self.entrada_texto, width=27, justify=tk.RIGHT, bd=2)
        Entrada.grid(row=0,column=0,ipady=16, ipadx=5)

        #Las 2 lineas de codigo de arriba son equivalentes a lo siguiente:
        #Entrada = tk.Entry(frameEntrada, font="Helvetica 24", textvariable=self.entrada_texto, width=27,justify=tk.RIGHT, bd=2).grid(row=0, column=0, ipady=16, ipadx=5)


        frameTeclado = tk.Frame(self, height=500,width=500 , bg='grey')
        frameTeclado.pack(side=tk.TOP)

        cButton = tk.Button(frameTeclado, text='C', font="Helvetica 12 bold", width=37, height=4, bd=0, bg='#eee', cursor='hand2', command=self._limpiar)
        cButton.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        divButton = tk.Button(frameTeclado, text='/', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#eee', cursor='hand2', command=lambda: self._addValue('/'))#MUCHO OJO AQUÍ: gracias a lambda , no se llamará a la función en este instante , que es lo que nos interesa, así que hay que usar lambda.
        divButton.grid(row=0, column=3, padx=1, pady=1, ipadx=3)

        sevenButton = tk.Button(frameTeclado, text='7', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._addValue('7'))
        sevenButton.grid(row=1, column=0, padx=1, pady=1, ipadx=4)

        eightButton = tk.Button(frameTeclado, text='8', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._addValue('8'))
        eightButton.grid(row=1, column=1, padx=1, pady=1, ipadx=5)

        nineButton = tk.Button(frameTeclado, text='9', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._addValue('9'))
        nineButton.grid(row=1, column=2, padx=1, pady=1, ipadx=3)

        multipButton = tk.Button(frameTeclado, text='*', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#eee', cursor='hand2', command=lambda: self._addValue('*'))
        multipButton.grid(row=1, column=3, padx=1, pady=1, ipadx=3)

        fourButton = tk.Button(frameTeclado, text='4', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff',cursor='hand2', command=lambda: self._addValue('4'))
        fourButton.grid(row=2, column=0, padx=1, pady=1, ipadx=4)

        fiveButton = tk.Button(frameTeclado, text='5', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff',cursor='hand2', command=lambda: self._addValue('5'))
        fiveButton.grid(row=2, column=1, padx=1, pady=1, ipadx=5)

        sixButton = tk.Button(frameTeclado, text='6', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff',cursor='hand2', command=lambda: self._addValue('6'))
        sixButton.grid(row=2, column=2, padx=1, pady=1, ipadx=3)

        subButton = tk.Button(frameTeclado, text='-', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#eee',cursor='hand2', command=lambda: self._addValue('-'))
        subButton.grid(row=2, column=3, padx=1, pady=1, ipadx=3)

        oneButton = tk.Button(frameTeclado, text='1', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff',cursor='hand2', command=lambda: self._addValue('1'))
        oneButton.grid(row=3, column=0, padx=1, pady=1, ipadx=4)

        twoButton = tk.Button(frameTeclado, text='2', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff',cursor='hand2', command=lambda: self._addValue('2'))
        twoButton.grid(row=3, column=1, padx=1, pady=1, ipadx=5)

        threeButton = tk.Button(frameTeclado, text='3', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#fff',cursor='hand2', command=lambda: self._addValue('3'))
        threeButton.grid(row=3, column=2, padx=1, pady=1, ipadx=3)

        sumButton = tk.Button(frameTeclado, text='+', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#eee',cursor='hand2', command=lambda: self._addValue('+'))
        sumButton.grid(row=3, column=3, padx=1, pady=1, ipadx=3)

        zeroButton = tk.Button(frameTeclado, text='0', font="Helvetica 12 bold", width=24, height=4, bd=0, bg='#fff',cursor='hand2', command=lambda: self._addValue('0'))
        zeroButton.grid(row=4, column=0, columnspan=2, padx=1, pady=1, ipadx=3)

        pointButton = tk.Button(frameTeclado, text='.', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#eee',cursor='hand2', command=lambda: self._addValue('.'))
        pointButton.grid(row=4, column=2, padx=1, pady=1, ipadx=3)

        totalButton = tk.Button(frameTeclado, text='=', font="Helvetica 12 bold", width=11, height=4, bd=0, bg='#eee',cursor='hand2', command=self._total)
        totalButton.grid(row=4, column=3, padx=1, pady=1, ipadx=3)


if __name__=='__main__':
    calculadora = Calculadora()
    calculadora.mainloop()