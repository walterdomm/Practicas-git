#Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
#e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

print('Calculo del Indice de masa corporal')
peso = input('Ingresar su peso: ')
altura = input('Ingresar su altura: ')
imc = float(peso) / (float(altura)**2)
print('Su índice de masa corporal es: ', imc)