#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es múltiplo de 2 y de 3 a la vez.

num = int(input('Ingresar un número entero..'))
if num % 2 == 0 and num % 3 == 0:
    print('El número ingresado es múltiplo de 2 y 3 a la vez')
else:
    print('El número ingresado NO es múltiplo de 2 y 3 a la vez')