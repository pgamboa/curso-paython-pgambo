'''
Realiza una función llamada intermedio(a, b) que a partir de dos números, 
devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio
 entre -12 y 24:

Recordatorio

El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
'''


def intermedio(a, b):
    punto_intermedio = (a+b)/2
    print(f"El punto intermedio entre [{a}] y [{b}] es [{punto_intermedio}] ")
    return(punto_intermedio)


if __name__ == "__main__":
    a = float(input("Ingrese el primer valor [a]: "))
    b = float(input("Ingrese el segundo valor [b]: "))

    intermedio(a, b)
