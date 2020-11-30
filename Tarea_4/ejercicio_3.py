'''Realiza una función llamada relacion(a, b) 
que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.'''

respuesta = 1


def relacion(a, b):
    """Comparación entre dos valores

    Args:
        a ([float]): [El primer valor]
        b ([float]): [El segundo valor]
    """
    if a > b:
        respuesta = 1
    elif a < b:
        respuesta = -1
    elif a == b:
        respuesta = 0
    print(respuesta)
    return(respuesta)


if __name__ == "__main__":
    a = float(input("Ingrese el primer valor [a]: "))
    b = float(input("Ingrese el segundo valor [b]: "))
    relacion(a, b)