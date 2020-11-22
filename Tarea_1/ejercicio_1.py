# Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:
'''
"Hola Mundo"
[1, 10, 100]
-25
1.167
["Hola", "Mundo"]
' '
'''
a = "Hola Mundo"
b = [1, 10, 100]
c = -25
d = 1.167
e = ["Hola", "Mundo"]
f = ''

tipo_dato = [a, b, c, d, e, f]
for i in tipo_dato:
    print(f"El tipo de dato {i} es: {type(i)} ")