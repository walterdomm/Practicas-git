#Escribe un programa que pida al usuario un número y luego imprima la tabla de
#multiplicar correspondiente a ese número del 1 al 10.

num = int(input('Ingresar un número: '))

for n in range(1, 11):
    resultado = num * n
    print(num, "x", n, "=", resultado)
