'''
En este ejercicio deberás crear un script llamado contador.py que realice varias tareas 
sobre un fichero llamado contador.txt que almacenará un contador de visitas (será un número):

Nuestro script trabajará sobre el fichero contador.txt. 
Si el fichero no existe o está vacío lo crearemos con el número 0. 
Si existe simplemente leeremos el valor del contador.

Luego a partir de un argumento:

    1.- Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
    2.- Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
    3.- Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
    4.- Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.

Utiliza excepciones si crees que es necesario, 
puedes mostrar el mensaje: Error: Fichero corrupto.
'''
from io import open
#contador = 0


def crear_fichero(arg=''):
    # open(nombre,a+) a+= abrir, leer y escribir, se usa si el archivo no existe
    fichero = open('contador.txt', 'a+')
    # seek, regresa un int, posiciona el curso en 0
    fichero.seek(0)
    contenido = fichero.readlines()

    if len(contenido) == 0:
        contenido = '0'
        # escribo contenido en fichero
        fichero.write(contenido)
    else:
        print("EL fichero no esta vacio.")
    fichero.close()
    try:
        contador = int(contenido)
        print(type(contador))
        if arg == 'inc':
            contador += 1
        elif arg == 'dec':
            contador -= 1
        print(contador)

        # Escribo cambios
        fichero = open("contador.txt", 'w')
        fichero.write(str(contador))
        fichero.close()
    except:
        print("Error: Fichero corrupto")


if __name__ == "__main__":
    argumento=str(input("Ingrese el argumento inc o dec: "))
    # print(argumento)
    crear_fichero(argumento)

'''Estimado Darwin, solo corre la primera vez y despues tengo que borrar lo que tiene el archivo.
no use la opción sys.argv pq no la entiendo, por favor tu gentil ayuda revisando este scrip y sugiriendome como 
solucionar el problema TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
'''
