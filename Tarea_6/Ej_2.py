'''
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. 
Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes.
'''

# Debo aplicar diccionarios {clave:valor}
vida = 2
ataque = 2
defensa = 2
alcance = 2

caballero = {'vida': 2*vida, 'ataque': 2, 'defensa': 2*defensa, 'alcance': 2}
guerrero = {'vida': vida, 'ataque': 2*ataque,
            'defensa': defensa, 'alcance': 2*alcance}
arquero = {'vida': vida, 'ataque': 2*ataque,
           'defensa': defensa/2, 'alcance': 2*(2*alcance)}

print(f"Caballero:=>\t{caballero},\nGuerrero:=>\t{guerrero}, \nArquero:=>\t{arquero}")
