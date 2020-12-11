'''
Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
Crea un conjunto llamado administradores con los administradores Juan y Marta.
Borra al administrador Juan del conjunto de administradores.
Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
Muestra todos los usuarios por pantalla de forma dinámica, 
además debes indicar cada usuario es administrador o no.

Sugerencia

Los conjuntos se pueden recorrer dinámicamente utilizando 
el bucle for de forma similar a una lista.

También cuentan con un método llamado .discard(elemento) 
que sirve para borrar o descartar un elemento.
'''
usuarios = {'Martha', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Maria'}
administradores.discard('Juan')
administradores.add('Marcos')

for user in usuarios:
    # EL in se usa para ver si un elemento pertenece al grupo 
    if user in administradores:
        print(f"{user}, es un admin")
    else:
        print(f"{user}, no es admin")



    '''
    Muy especifico 
    if user == 'Marcos':
        print(f"{user}, es un admin")
    elif user != 'Marcos':
        print(f"{user}, no es admin")
    else:
        for admin in administradores:
            if admin == 'Maria':
                print(f"{admin}, es un admin")'''