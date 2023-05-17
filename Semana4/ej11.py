#Crea una función llamada contar_vocales que tome una cadena de texto como
#parámetro y devuelva el número de vocales que contiene.

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    return contador

texto = 'Hola como estas ?'
prueba = contar_vocales(texto)
print(prueba)
