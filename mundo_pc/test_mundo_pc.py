from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado

#Primer objeto tipo computadora
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Acer', 25)
computadora = Computadora('Acer', monitor1, teclado1, raton1)


#Segundo objeto tipo computadora
teclado2 = Teclado('Azus', 'USB')
raton2 = Raton('Logitech', 'USB')
monitor2 = Monitor('Acer', 25)
computadora1 = Computadora('Acer', monitor2, teclado2, raton2)

#Tercer objeto tipo computadora
teclado3 = Teclado('Gamer', 'USB')
raton3 = Raton('Logitech', 'USB')
monitor3 = Monitor('Samsung', 20)
computadora2 = Computadora('Acer', monitor3, teclado3, raton3)

computadoras1 = [computadora, computadora1]
orden1 = Orden(computadoras1)
print(orden1)
orden1.agragar_computadora(computadora2)
print(orden1)