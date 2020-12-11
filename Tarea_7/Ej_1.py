'''
Localiza el error en el siguiente bloque de código.
Crea una excepción para evitar que el programa se bloquee y
además explica en un mensaje al usuario la causa y/o solución:
'''
try:
    resultado = 10/0
except ZeroDivisionError as zd:
    print("ZeroDivisionError :", zd.__class__)
    mensaje = "La division por cero no es permitida"
    print(mensaje)
except Exception as ex:
    print("Excepcion Global", ex.__class__)
finally:
    print("Este bloque se ejecuta siempre")
