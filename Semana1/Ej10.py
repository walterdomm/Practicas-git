# Crea un programa que pida al usuario una cantidad en dólares y la convierta a
# euros.
# Supón que el tipo de cambio es de 0.84 euros por dólar.

print('Dólares a Euros')
dolares = int(input('Ingresar cantidad de dolares a convertir'))
euros = dolares*0.84
print(f'{int(dolares)} dólares equivalen a {euros} euros')