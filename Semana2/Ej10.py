#Escribir un programa que pida al usuario una letra y muestre por pantalla si es
#una vocal o una consonante.

letra = input('Ingresar una letra')
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print('La letra es una vocal')
else:
    print('La letra es una consonante')

#otra manera de obtener el mismo resultado:

if letra in "aeiouAEIOU":
    print('La letra es una vocal')
else:
    print('La letra es una consonante')