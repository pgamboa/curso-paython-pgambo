'''
En este ejercicio deberás crear un script llamado personas.py 
que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y 
lo añada a una lista llamada personas. Luego rocorre las personas de la lista y 
parac ada una muestra de forma amigable todos sus campos.

El fichero de texto se denomina r personas.txt y tendrá el siguiente contenido 
en texto plano (créalo previamente):
'''
from io import open
import time


def personas():
    # se usa encoding para leer los caracteres
    # personas.txt ya fie creado
    fichero = open('personas.txt', 'r', encoding="utf8")
    filas = fichero.readlines()  # lee el fichero por filas
    fichero.close()

    # Pongo una lista vacia
    personas = []

    for fila in filas:
        # replace= syntax= string.replace(oldvalue, newvalue, count)
        # split=  usa un separador= string.split(separator,maxsplit),
        campos = fila.replace("\n", "").split(";")
        persona = {"id": campos[0], "nombre": campos[1],
                   "apellido": campos[2], "f_nacimiento": campos[3]}
        personas.append(persona)
    # print(f"Los campos son {personas}")

    for i in personas:
        print("(id={})\t {} {}\t=>\t{}".format(
            i['id'], i['nombre'], i['apellido'], i['f_nacimiento']))


'''
        for i, c in enumerate(campos):
            persona = {i : c}
            personas.append(persona)
    print(personas)
    for p in personas:
        print(p)
        print("(id={})  {} {} => {}".format(p,p,p,p) )

    #print(personas)



       # print(f"F: {fila}")

        for i, v in enumerate(campos):
            dic = {'id': v[i]}

            lista.append(dic)

            # print(i,v)

        # creo mi Diccionario con el formato

        # lista.append(separar)

        #print (lista)

    print(lista)'''


if __name__ == '__main__':
    personas()
