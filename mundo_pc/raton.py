from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada) -> None:
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self) -> str:
        return f'Id: {self._id_raton}, Marca: {self.marca}, Tipo entrada: {self.tipo_entrada}'

if __name__ == '__main__':
    raton = Raton('Logitech', 'USB')
    print(raton)

    raton1 = Raton('Razer', 'USB')
    print(raton1)
