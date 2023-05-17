#Escribe un programa que pida al usuario un número y calcule la suma de todos
#los números naturales del 1 hasta ese número.

num = int(input('Ingresar número '))
suma = 0

for n in range(1, num+1):
    suma += n

print(f'La suma de todos los números naturales hasta el número ingresado es: {suma}.')