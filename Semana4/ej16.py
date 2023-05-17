#Crea una función llamada eliminar_duplicados que tome una lista como
#parámetro y devuelva una nueva lista sin duplicados, conservando el orden
#original.

def eliminar_duplicados(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista

lista2 = ['cosa', 'casa', 'perro', 'gato', 'sabueso', 2, 2, 4, 5, 6, 6, 'cosa']
prueba = eliminar_duplicados(lista2)
print(prueba)
