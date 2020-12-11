class Mamifero():
    def __init__(self, ojos=None, nariz=None, boca=None, pelo=None):
        self.ojos = ojos
        self.nariz = nariz
        self.boca = boca
        self.pelo = pelo
    # Redefine el método que se va ha ejecutar, debe retornar un STR

    def __str__(self):
        return '[{}] ({})'.format(self.ojos, self.nariz, self.boca, self.pelo)

    # Creo los metodos=acciones de mi clase
    # Se puede utilizar para realizar polimorfismo entre las Clases Admin-Cliente-Invitado
    def duermen(self):
        """
        Dormir
        """
        print("Dormir")

    def comer(self):
        print("Comer")

    def moverse(self):
        print("Moverse")


class Perro(Mamifero):
    def __init__(self, sangre, huesos, pelaje, pulmones, **kwargs):
        self.sangre = sangre
        self.huesos = huesos
        self.pelaje = pelaje
        self.pulmones = pulmones
        super().__init__(**kwargs)

    def __str__(self):
        super_clase = super().__str__()
        return (f"{super_clase}\n Nombre: {self.nombre} Procedencia: {self.procedencia} Peso:{self.peso} Tamaño: {self.tamanio} ")

    def morder(self):
        print("morder")

    def jugar(self):
        print("jugar")

    def correr(self):
        print("correr")
