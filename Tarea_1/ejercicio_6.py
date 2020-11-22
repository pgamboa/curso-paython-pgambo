# Al raliza una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
# Al parecer contiene el nombre de un alumno y la nota de un examén.
# ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
# Nombre Apellido ha sacado una Nota de  nota.
cadena_corrupta = 'zeréP nauJ,01' 

cadena = cadena_corrupta[::-1] #Invierto la cadena
print(cadena)

print(cadena[slice(3, 7)], " ", cadena[slice(8, 12)], "ha sacado una ", cadena[slice(0, 2)]) #saco los slice de la cadena corregida
