'''
Realiza una función llamada area_rectangulo(base, altura) que devuelva el área 
del rectangulo a partir de una base y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura:

Recordatorio

El área de un rectángulo se obtiene al multiplicar la base por la altura.

'''
def area_rectangulo(base,altura):
    """Área de un rectangulo

    Args:
        base ([float]): base
        altura ([float]): altura
    """
    area_rec=base*altura
    print(f"El área del rectangulo es [{base}] * [{altura}] = [{area_rec}]")
    return(area_rec)

if __name__=="__main__":

    base=float(input("Ingrese el valor de la base del rectangulo: "))
    altura=float(input("Ingrese el valor de la altura del rectangulo: "))

    area_rectangulo(base,altura)