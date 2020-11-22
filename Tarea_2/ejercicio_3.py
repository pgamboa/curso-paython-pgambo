#Realizar un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores
#de asignación

numero_magico = 12345679 #numeros enteros entre el 0 al 65.535
numero_usuario = int(input("Ingrese un numero entre el 1 al 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario

print(f"El número mágico es {numero_magico} ")