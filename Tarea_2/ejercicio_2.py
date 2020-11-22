# Utilizando operadores lógicos, determinar si una cadena de texto introducida por el usuario
# tiene una longitud mayor o igual que 3 y a su vez es menor que 10

cadena = input("Escriba una cadena\t")
longitud = len(cadena)
print(longitud)
print(f"¿La longitud de la cadena es mayor o igual que 3 y menor que 10? {longitud>=3 and longitud<=10} ")
