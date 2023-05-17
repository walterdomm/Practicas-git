#Crear una lista con los nombres de tres colores y agregar dos colores más al
#final de la lista. Mostrar la lista resultante.

colores = ['rojo', 'azul', 'negro']
colores.append('verde')
colores.append('violeta')
print(colores)

#otras formas:

colores2 = ['rojo', 'azul', 'negro']
colores2.extend(['verde', 'violeta'])
print(colores2)

colores3 = ['rojo', 'azul', 'negro']
colores3 = colores3 + ['verde', 'violeta']
print(colores3)