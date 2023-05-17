#Crea una función llamada convertir_temperatura que tome una temperatura
#en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
#es: Fahrenheit = (Celsius * 9/5) + 32.

def convertir_temperatura(temp):
    return ((temp * 9/5)+32)

prueba = convertir_temperatura(45)
print(prueba)