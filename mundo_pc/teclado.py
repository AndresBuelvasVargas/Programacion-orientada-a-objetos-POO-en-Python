from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, marca, tipo_entrada) -> None:
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self) -> str:
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    teclado = Teclado('Corsair K70 MK.2 RGB Low Profile RapidFire', 'USB')
    print(teclado)

    teclado1 = Teclado('HP', 'Bluetooth')
    print(teclado1)