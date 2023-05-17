#Crea una función llamada es_capicua que tome un número como parámetro y
#devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
#derecha a izquierda) y False en caso contrario.

def es_capicua(num):
    cadena_numero = str(num)
    cadena_invertida = cadena_numero[::-1]
    if cadena_numero == cadena_invertida:
        return True
    else:
        return False


resultado = es_capicua(313)
print(resultado)

#otra forma::


def es_capicua2(num):
    ''' Esta función permite realizar la comprobación de si un número es capicúa,
    es decir si se lee igual de adelante hacia atrás y biceversa
    '''
    cadena_numero = str(num)
    if cadena_numero == cadena_numero[::-1]:
        return True
    else:
        return False
    
print(es_capicua2.__doc__)