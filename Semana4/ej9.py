#Crea una función llamada promedio que tome una lista de números como
#parámetro y devuelva el promedio de esos números.

def promedio(lista):
    if len(lista) == 0:
        return 0
    else:
        return sum(lista) / len(lista)


numeros = [2, 4, 6]
sacar_promedio = promedio(numeros)
print(sacar_promedio)