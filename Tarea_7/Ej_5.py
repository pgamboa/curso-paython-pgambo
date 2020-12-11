'''
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError 
que debes capturar y mostrar este mensaje en su lugar:
'''


def agregar_una_vez(lista, el):
    """Funsion para excepciones de errores

    Args:
        lista ([lista]): [Lista]
        el ([entero]): [Elemmento ingresado]

    Raises:
        ValueError: [COndicional ]
    """
    try:
        if el in lista:
            raise ValueError
        else:
            elementos.append(el)

    except ValueError:
        print("Error, no se puede añadir duplicados ")


if __name__ == "__main__":
    elementos = [1, 5, -2]
    agregar_una_vez(elementos, 26)
    print(elementos)
