#Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la
#lista. Mostrar la lista resultante.

frutas = ['pera', 'naranja', 'banana']
frutas.remove('naranja')
print(frutas)

#another way
frutas2 = ['pera', 'naranja', 'banana']
del frutas2[1]
print(frutas2)