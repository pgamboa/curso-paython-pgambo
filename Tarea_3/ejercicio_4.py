# Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.
numeros = int(input("Ingrese la cantidad de números que quiere introducir\n"))
acumulador = 0
bandera = 1

# Con un for
for i in range(numeros):
    acumulador += int(input("Ingrese el numero "))

print(f"Se han introducido {numeros} numeros que suma {acumulador}, y su media aritmetica es {acumulador/numeros} ")

# Con un while, necesito tener una bandera
acumulador = 0
while bandera <= numeros:
    acumulador += int(input("Ingrese el numero "))
    bandera += 1

print(f"Se han introducido {numeros} numeros que suma {acumulador}, y su media aritmetica es {acumulador/numeros} ")
