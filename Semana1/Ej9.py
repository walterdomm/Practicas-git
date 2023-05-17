# Escribe un programa que solicite al usuario dos números y luego imprima la
# suma, la resta, la multiplicación y la división de los dos números.

print('Sumando, restando, multiplicando y dividiendo dos números.')
nro1 = int(input('Ingresar el primer numero'))
nro2 = int(input('Ingresar el segundo numero'))
suma = nro1+nro2
resta = nro1-nro2
multiplicacion = nro1*nro2
division = nro1//nro2
print(f'Los resultados son suma: {suma}, resta: {resta}, multiplicacion: {multiplicacion} y division: {division}.')