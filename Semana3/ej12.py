#Escribe un programa que pida al usuario una lista de números separados por
#comas y calcule su promedio.

numeros = input('Ingrese varios números separados por comas: ')

numeros_lista = numeros.split(",")

numeros_enteros = []

for n in numeros_lista:
    numeros_enteros.append(int(n))

promedio = sum(numeros_enteros) / len(numeros_enteros)

print(f'El promedio de los números ingresados es {promedio}.')