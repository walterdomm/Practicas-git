#Escribe un programa que pida al usuario una palabra y luego imprima la misma
#palabra pero con las letras en orden inverso.

palabra = input('Escribe una palabra: ')

palabra_invertida = palabra[::-1]

print(f'La palabra invertida es: {palabra_invertida}.')