# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición,
# y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
# ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

'''
Ayuda:
La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!
'''
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
a = matriz[0][:4]
b = matriz[1][:4]
c = matriz[2][:4]
d = matriz[3][:4]

a[3] = sum(a[0:3])
b[3] = sum(b[0:3])
c[3] = sum(c[0:3])
d[3] = sum(d[0:3])

matriz = [a, b, c, d]
print(f"La matriz corregida es: \n matrizcorregida = [{a}, \n {b}, \n {c},\n {d}] ")
