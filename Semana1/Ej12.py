# Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

print('Calculadora de edad según fecha de nacimiento')
fechaDeNacimiento = input('Ingrese su fecha de nacimiento con formato dd/mm/aaaa')
dia, mes, anio = fechaDeNacimiento.split('/')
edad = 2023-int(anio)
print('Su edad es ', edad, ' años.')