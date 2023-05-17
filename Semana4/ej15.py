#Crea una función llamada contar_palabras que tome una cadena de texto
#como parámetro y devuelva el número de palabras que contiene. Se considera
#que las palabras están separadas por espacios.

def contar_palabras(texto):
    palabras = texto.split(' ')
    return len(palabras)

prueba = contar_palabras('Hola como estas?')
print(prueba)