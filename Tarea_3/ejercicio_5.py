'''Realiza un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
 Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Concepto útil

La sintaxis [valor] in [lista] permite comprobar si un valor se encuentra en una lista (devuelve True o False).
'''

lista = [1, 3, 6, 9, 4, 11]

while True:
    numero = int(input("Ingrese un numero entero entre el 0 al 9 \n"))
    if numero >= 0 and numero <= 9:
        break
if numero in lista:
    print(f"El numero {numero} existe en la lista {lista} ")
else:
    print(f"El numero {numero} no existe en la lista {lista} ")