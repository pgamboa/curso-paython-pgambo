'''
Realiza una función separar(lista) que tome una lista de números enteros y 
devuelva dos listas ordenadas. La primera con los números pares y 
la segunda con los números impares.
'''
l_pares = []
l_impares = []


def separar(lista):
    """Separación de la lista en sub listas, con valores pares e impares

    Args:
        lista ([list]): Lista
    """
    for i, v in enumerate(lista):
        print(f"El valor del indice es [{i}] ")
        if v % 2 == 0:
            l_pares.append(v)
        else:
            l_impares.append(v)
    lr_pares = l_pares
    lr_impares = l_impares
    print(f"La lista ordenada de los # pares es: {lr_pares}")
    print(f"La lista ordenada de los # impares es: {lr_impares}")
    return(lr_pares, lr_impares)


if __name__ == "__main__":
    num = int(input("Ingrese el rago de la lista: "))
    lista = list(range(0, num+1))
    print(lista)
    separar(lista)
