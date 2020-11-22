# Realizar un programa que lea 2 números por teclado y determinar los siguientes aspectos:
# Si los dos numeros son iguales
# Si los dos numeros son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

num_1 = float(input("Por favor ingrese el primer numero: "))
num_2 = float(input("Por favor ingrese el segundo numero: "))

print(f"¿Son iguales? {num_1==num_2} ")
print(f"¿Son diferentes? {num_1!=num_2} ")
print(f"¿El primer número es mayor que el segundo? {num_1>num_2} ")
print(f"¿El segundo es mayor o igual que el primero? {num_2>=num_1} ")
