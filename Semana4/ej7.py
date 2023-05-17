#Crea una función llamada imprimir_pares que tome un número entero como
#parámetro y imprima todos los números pares desde 1 hasta ese número.

def imprimir_pares(num):
    for n in range(1, num+1):
        if n % 2 == 0:
            print(n)


imprimir_pares(20)
