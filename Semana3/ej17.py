#Escribe un programa que pida al usuario una cadena de texto y luego imprima
#la misma cadena pero con las palabras en orden inverso.

texto = input('Ingresar un texto cualquiera: ')

texto = texto.strip()

palabras = texto.split()

palabras_invertidas = palabras[::-1]

texto_invertido = " ".join(palabras_invertidas)

print(texto_invertido)