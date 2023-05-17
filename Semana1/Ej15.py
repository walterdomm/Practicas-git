#Escribe un programa que solicite al usuario una temperatura en grados
#Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
#La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

print('Transforando °C a °F...')
temperatura = float(input('Ingrese la temperatura: '))
farenheit = (temperatura * 1.8) + 32
print('La temperatura ingresada en °F es: ',farenheit)