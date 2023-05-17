#-Escribe un programa que pida al usuario un número y luego imprima un
#triángulo de asteriscos con esa cantidad de filas.
#*
#**
#***
#****
#*****

num = int(input('Ingrese un número de filas: '))

for n in range(num):
    for c in range(n+1):
        print('*', end=' ')
    print()

#otra manera pero con WHILE

numero = int(input("Ingresar un numero: "))
piramide = ""
i = 1

while i <= numero:
    piramide += "*"*i+"\n"
    i += 1

print(piramide)