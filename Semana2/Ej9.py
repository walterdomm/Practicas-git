#Escribir un programa que pida al usuario tres números y muestre por pantalla
#el mayor de ellos.

num = float(input('Ingresar un número'))
num2 = float(input('Ingresar otro número'))
num3 = float(input('Ingresar el último número'))

if num > num2 and num > num3:
    print('El número mayor es el ', num)
elif num2 > num and num2 > num3:
    print('El número mayor es', num2)
else:
    print('El número mayor es ', num3)