#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es positivo, negativo o cero.

numero = int(input('Ingresar un numero entero '))

if numero == 0:
    print('El número es cero')
elif numero > 0:
    print('El número es positivo')
else:
    print('El número es negativo')