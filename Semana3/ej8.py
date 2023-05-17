#Escribe un programa que pida al usuario una cadena de texto y luego imprima
#el número de palabras que contiene.

texto = input('Ingrese un texto cualquiera: ')

palabras = texto.split()

num_palabras = len(palabras)

print(f'El texto contiene {num_palabras}.')