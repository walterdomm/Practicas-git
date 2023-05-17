#Crea una función llamada calcular_factorial que tome un número entero como
#parámetro y devuelva el factorial de ese número. El factorial de un número
#entero positivo n se define como el producto de todos los números enteros
#positivos desde 1 hasta n.

def calcular_factorial(num):
    if num == 0:
        return 1
    else:
        factorial = 1
        for n in range(1, num+1):
            factorial *= n
        return factorial

prueba = calcular_factorial(3)
print(prueba)
