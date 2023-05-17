#Escribe un programa que pida al usuario un número y luego imprima si ese
#número es un número perfecto o no. Un número perfecto es aquel que es igual a
#la suma de sus divisores propios (excluyendo el propio número).
#Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
#puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

numero = int(input('Ingresar un número: '))

suma_div = 0

for i in range(1, numero):
    if numero % i == 0:
        suma_div += i

if suma_div == numero:
    print(f'El número {numero} es un número perfecto.')
if suma_div != numero:
    print(f'El número {numero} NO es un número perfecto.')
