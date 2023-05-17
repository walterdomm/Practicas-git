#Crear una lista con los nombres de tres animales y agregar una cuarta animal
#al principio de la lista. Mostrar la lista resultante.

animales = ['leon', 'jirafa', 'ciervo']
animales.insert(0, 'gato')
print(animales)

#another way
animales2 = ['leon', 'jirafa', 'ciervo']
animales2 = ['gato'] + animales2
print(animales2)