# Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar,
# debe repetise el proceso hasta que lo introduzca correctamente.
num = float(input("Ingresa un numero impar:\n"))

while num % 2 == 0:
    num = float(input("Ingresa un numero impar:\n"))
