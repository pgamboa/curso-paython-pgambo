'''
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
'''


try:
    colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
    colores['blanco']
except KeyError as ke:
    print("KeyError", ke.__class__)
    mensaje = 'En el diccionario no existe esa clave, ingresar claves que existan'
    print(mensaje)
finally:
    print("Este bloque se ejecuta siempre")
