'''
Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10.
'''
respuesta = 0


def recortar(numero, minimo, maximo):
    if numero < minimo:
        respuesta = minimo
    elif numero > maximo:
        respuesta = maximo
    else:
        respuesta = numero
    print(respuesta)
    return(respuesta)


if __name__ == "__main__":
    numero = float(input("Ingrese el numero: "))
    minimo = float(input("Ingrese el mínimo: "))
    maximo = float(input("Ingrese el máximo: "))

    recortar(numero, minimo, maximo)
