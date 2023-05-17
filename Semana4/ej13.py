#Crea una función llamada calcular_descuento que tome dos parámetros:
#precio y porcentaje_descuento. La función debe calcular y devolver el precio
#después de aplicar el descuento.

def calcular_descuento(precio, descuento):
    return (precio*(100-descuento)/100)

prueba = calcular_descuento(10000, 10)
print(prueba)