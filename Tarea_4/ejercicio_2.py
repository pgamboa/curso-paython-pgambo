'''
Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo 
a partir de un radio. Calcula el área de un círculo de 5 de radio:

Recordatorio

El área de un círculo se obtiene al elevar el radio a dos y multiplicando 
el resultado por el número pi. 

Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:
'''
import math


def area_circulo(radio):
    """Área del circulo

    Args:
        radio ([float]): radio en cm
    """
    area_circulo = round(((radio**2)*math.pi),2)
    print(f"El área del circulo con un radio {radio} cm es = {area_circulo} cm\u00B2") 
    #\u00B2 para poner el elevado al cuadrado

    return(area_circulo)

if __name__=="__main__":
    radio=float(input("Ingrese el radio en cm: "))

    area_circulo(radio)