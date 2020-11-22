'''Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
'''

lis_1=list(range(0,11)) #intervalo por defecto es 1
print(lis_1)

list_2=list(range(-10,1))
print(list_2)

list_3=list(range(0,21,2))
print(list_3)

list_4=list(range(-19,0,2))
print(list_4)

list_5=list(range(0,51,5))
print(list_5)