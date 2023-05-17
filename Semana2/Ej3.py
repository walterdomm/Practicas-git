#Escribir un programa que pida al usuario dos números y muestre por pantalla
#cuál de ellos es mayor.

num1 = float(input('Ingresar el primer número '))
num2 = float(input('Ingresar el segundo número '))

if num1 > num2:
    print('El número ', num1, ' es el mayor.')
else:
    print('El número', num2, ' es el mayor.')