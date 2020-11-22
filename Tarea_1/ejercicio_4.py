# A partir del ejercicio anterior, vamos a suponer que cada número es una nota,
# y lo que queremos es obtener la nota final.
# El problema es que cada nota tiene un valor porcentual:

'''
La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total
Desarrolla un programa para calcular perfectamente la nota final:'''
nota_1 = 10*.15
nota_2 = 7*.35
nota_3 = 4*.5

nota_final = round(((nota_1+nota_2+nota_3)/3), 2) #redonde a dos decimales 

print(f"La nota final es {nota_final} % ")
