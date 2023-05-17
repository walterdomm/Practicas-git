#Crea una función llamada es_palindromo que tome una cadena de texto como
#parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
#de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
#contrario.

def es_palindromo(texto):
    cadena_texto = str(texto)
    cadena_invertida = cadena_texto[::-1]
    if cadena_texto == cadena_invertida:
        return "Es palíndromo."
    else:
        return "No es palíndromo."

prueba = es_palindromo("neuquen")
print(prueba)