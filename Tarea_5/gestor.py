'''
Utilizando como base el ejercicio de los personajes que hicimos,
en este ejercicio tendrás que crear un gestor de personajes gestor.py para añadir
y borrar la información de los siguientes personajes:

Nombre     Vida	Ataque	Defensa	Alcance
Caballero	4	  2	      4	          2
Guerrero	2	  4	      2	          4
Arquero		2	  4	      1           8
Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando
en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistirán.

Crea dos clases, una Personaje y otra Gestor.
La clase Personaje deberá permitir crear un personaje con el nombre (que será la clase),
y sus propiedades de vida, ataque, defensa y alcance (que deben ser números enteros mayor que cero obligatoriamente).

Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes,
mostrarlos y borrarlos (a partir de su nombre por ejemplo, tendrás que pensar una forma de hacerlo),
además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl
que se deberían ejecutar automáticamente.

En caso de que el personaje ya exista en el Gestor entonces no se creará.
Una vez lo tengas listo realiza las siguientes prueba en tu código:

Crea los tres personajes de la tabla anterior y añádelos al Gestor.
Muestra los personajes del Gestor.
Borra al Arquero.
Muestra de nuevo el Gestor.
'''
from io import open
import pickle


class Personaje():

    # Creo mi contructor con el nombre que es la Clase y sus propiedades
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    # Redefinir el metodo a utilizar

    def __str__(self):
        return f"{self.nombre} => vida {self.vida}, ataque{self.ataque}, defensa {self.defensa}, alcance {self.alcance}"


class Gestor():
    # Donde creo mis personajes
    personajes = []

    # Constructor del Gestor
    def __int__(self):
        self.cargar_personaje()

    def cargar_personaje(self):
        # ab+ = a=si el fichero no existe lo crea y lo abre b=modo binario
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            pass
        finally:
            fichero.close()
            print("Se ha cargado {} personajes".format(len(self.personajes)))

    def anadir_personaje(self, per):  # per=Pesonaje
        """Metodo para añadir personajes

        Args:
            per ([string]): [Información de ejercicio Personajes]
        """
        for pTemporal in self.personajes:
            if pTemporal.nombre == per.nombre:
                return
        self.personajes.append(per)
        self.guardar_cambios_personaje()

    def borrar_personaje(self, nombre):
        for pTemporal in self.personajes:
            if pTemporal.nombre == nombre:
                self.personajes.remove(pTemporal)
                self.guardar_cambios_personaje()
                print(f"\nPesonaje [{nombre}] se ha borrado ")
                return

    def guardar_cambios_personaje(self):
        fichero = open('personajes.pckl', 'wb')
        # pickle permite almacenar bd, tx archivo en la RED
        # la función dump() 2 argumentos: obj pickle (lista de tareas) y obj file(donde escribimos pickle)
        pickle.dump(self.personajes, fichero)
        fichero.close()

    def mostrar_personaje(self):
        if self.personajes == 0:
            print("El gestor esta vacio")
            return
        for per in self.personajes:
            print(per)


if __name__ == "__main__":
    # Llamo a la clase Gestor
    gestor = Gestor()
    # Utilizando la Clase Personaje y el método anadir_personaje realizado en la Clase Gestor
    # Añado personajes
    gestor.anadir_personaje(Personaje("Arquero", 2, 4, 1, 8))
    gestor.anadir_personaje(Personaje("Caballero", 4, 2, 4, 2))
    gestor.anadir_personaje(Personaje("Guerrero", 2, 4, 2, 4))

    gestor.mostrar_personaje()
    gestor.borrar_personaje("Arquero")
    gestor.mostrar_personaje()
