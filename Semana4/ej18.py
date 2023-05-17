#Crea una función llamada calcular_mayor_diferencia que tome una lista de
#números como parámetro y devuelva la mayor diferencia entre el numero mas
#alto y el numero mas bajo en la lista.

def calcular_mayor_diferencia(numeros):
    if len(numeros) < 2:
        return 0
    max(numeros)
    min(numeros)
    diferencia = max(numeros) - min(numeros)
    return diferencia

lista = [4, 6, 10, 100]
resultado = calcular_mayor_diferencia(lista)
print(resultado)