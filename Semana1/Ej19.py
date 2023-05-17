#Escribe un programa que solicite al usuario un número decimal y luego
#imprima la parte entera y decimal por separado.

nro_decimal = float(input('Ingrese un número decimal...'))
parte_entera = int(nro_decimal)
parte_decimal = nro_decimal - parte_entera

print('La parte entera es:', parte_entera)
print('La parte decimal es: ', parte_decimal)