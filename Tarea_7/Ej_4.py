'''
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
'''
try:
    resultado = 15 + "20"
except TypeError as te:
    print('TypeError', te.__class__)
    mensaje='No se pueden sumnar valores enteros y cadenas de datos, ingrese datos del mismo tipo'
    print(mensaje)
finally:
   print("Este bloque se ejecuta siempre")
