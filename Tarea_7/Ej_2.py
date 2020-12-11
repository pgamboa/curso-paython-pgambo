'''
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica 
en un mensaje al usuario la causa y/o solución:
'''
try:
    lista = [1, 2, 3, 4, 5]
    lista[10]
except IndexError as ie:
    print('IndexError: ', ie.__class__)
    mensaje='La lista no tiene este indice, ingrese el indice correcto '
    print(mensaje)
finally:
    print("Este bloque se ejecuta siempre")
