'''Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
pero no debe repetirse ningún elemento en la nueva lista:'''

l_1 = ['E', 'l', ' ', 'a', 'm', 'o', 'r', ' ', 'e', 't',
       'i', 'e', 'm', 'p', 'o', 's', ' ', 'd', 'e', ' ', 'c', 'l', 'e', 'r', 'a']
l_2 = ['H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
l_3 = []

for i in l_1:
    if i in l_2 and i not in l_3:
        l_3.append(i)
print(l_3)
