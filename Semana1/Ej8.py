# Crea un programa que pida al usuario el radio de un círculo y muestre su
# diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159.

print('TODO SOBRE UN CÍRCULO DADO SU RADIO:')
radio = input('Ingrese el radio del círculo aquí: ')
area = 3.14159*(int(radio)**2)
diametro = int(radio)*2
circunferencia = 3.14159*(int(diametro))
print(f'El diametro es: {diametro}, su circunferencia es: {circunferencia} y su area es: {area}.')