'''
Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números

En caso de introducir una opción inválida, el programa informará de que no es correcta.
'''
import time

while True:
    print("{}\n".format("Menu Principal"),
          "{:15}\n".format("1.- Suma"),
          "{:15}\n".format("2.- Resta"),
          "{:15}\n".format("3.- Multiplicación"),
          "{:15}\n".format("S.- Salir")
          )
    opcion = int(input("Seleccione la operacion a realizar : \n"))

    if opcion == 1:
        print('-'*20, "Suma", '-'*20, )
        num_1 = float(input("Ingresa el primer numero:\n"))
        num_2 = float(input("Ingresa el segundo numero:\n"))
        print(f"El resultado de la suma {num_1} + {num_2} = {num_1+num_2} ")
        print('-'*20, "Suma", '-'*20, )
    elif opcion == 2:
        print('-'*20, "Resta", '-'*20, )
        num_1 = float(input("Ingresa el primer numero:\n"))
        num_2 = float(input("Ingresa el segundo numero:\n"))
        print(f"El resultado de la resta {num_1} - {num_2} = {num_1-num_2} ")
        print('-'*20, "Resta", '-'*20, )
    elif opcion == 3:
        print('-'*20, "Multiplicación", '-'*20, )
        num_1 = float(input("Ingresa el primer numero:\n"))
        num_2 = float(input("Ingresa el segundo numero:\n"))
        print(f"El resultado de la multiplicación es {num_1} * {num_2} = {num_1*num_2} ")
        print('-'*20, "Multiplicación", '-'*20, )
    elif opcion == 's' or opcion == 'S':
        break
    else:
        print("No existe la opcion")