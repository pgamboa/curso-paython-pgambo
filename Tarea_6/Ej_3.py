'''
Durante la planificación de un proyecto se han acordado una lista de tareas. 
Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
'''
from collections import deque
# deque es para agregar y eliminar elementos de cualquier extremo de la cola

tareas = [[6, 'Distribucion'], [2, 'Diseño'], [1, 'Concepción'], [
    7, 'Mantenimiento'], [4, 'Producción'], [5, 'Planificación']]

# Con sort ordeno de menor a mayor
tareas.sort()

# Creo la cola vacia
cola = deque()

for t in tareas:
    cola.append(t)  # incluto uno a uno los elementos en cola=deque()

# iteración de el deque() cola de forma ordenada, y se presenta como una lista en columnas
for tarea in cola:
    print(tarea)
