#Crea una función llamada es_anagrama que tome dos cadenas de texto como
#parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
#letras pero en distinto orden), o False en caso contrario.

def es_anagrama(texto, texto2):
    if len(texto) != len(texto2):
        return False
    else:
        lista1 = list(texto)
        lista2 = list(texto2)
        lista1.sort()
        lista2.sort()
        if lista1 == lista2:
            return True
        else:
            return False

prueba = es_anagrama('casa', 'saca')
print(prueba)