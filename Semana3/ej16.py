#Escribe un programa que pida al usuario una cadena de texto y luego imprima
#la misma cadena pero con cada palabra al revés.

texto = input('Ingresar un texto cualquiera: ')

palabras_invertidas = texto[::-1]

print(palabras_invertidas)

#otra opción de interpretación de la consigna:

texto2 = input('Ingresar un texto cualquiera: ')

texto2 = texto2.strip()

palabras = texto2.split()

palabras_invertidas2 = [palabra[::-1] for palabra in palabras]

texto2_invertido = " ".join(palabras_invertidas2)

print(texto2_invertido)