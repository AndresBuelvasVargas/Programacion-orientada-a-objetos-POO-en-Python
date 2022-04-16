from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton) -> None:
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self) -> str:
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__ == '__main__':
    #Primer objeto
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('Acer', 25)
    computadora = Computadora('Acer', monitor1, teclado1, raton1)
    print(computadora)

    #Segundo objeto
    teclado2 = Teclado('Azus', 'USB')
    raton2 = Raton('Logitech', 'USB')
    monitor2 = Monitor('Acer', 25)
    computadora1 = Computadora('Acer', monitor2, teclado2, raton2)
    print(computadora1)