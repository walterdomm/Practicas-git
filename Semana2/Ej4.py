#Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
#pantalla si está aprobado (5 o más) o no.

nota = float(input('Ingresar la nota obtenida '))

if nota >= 5:
    print('APROBADO!')
else:
    print('DESAPROBADO :(')