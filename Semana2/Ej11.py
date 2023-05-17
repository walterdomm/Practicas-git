#Escribir un programa que pida al usuario dos números y muestre por pantalla
#la suma de ellos solo si ambos son pares.

num = float(input('Ingresar un número..'))
num2 = float(input('Ingresar otro número..'))
if num % 2 == 0 and num2 % 2 == 0:
    print(num+num2)
else:
    print('Uno o ambos números no son pares')