#Escribe un programa que imprima la suma de todos los números pares del 1 al
#100.

suma = 0
for n in range(1, 100+1):
    if n % 2 == 0:
        suma += n

print(f'La suma de todos los números pares del 1 al 100 es: {suma}.')

#otra forma:

suma2 = 0
for n2 in range(2, 101, 2):
    suma2 += n2

print(f'La suma de todos los números pares del 1 al 100 es: {suma2}.')
