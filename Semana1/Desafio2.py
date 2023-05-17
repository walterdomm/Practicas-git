#Escribe un programa que solicite al usuario su información personal, incluyendo
#su nombre completo, edad, estatura, peso, dirección y número de teléfono.
#A continuación, el programa deberá imprimir un mensaje con los datos
#ingresados por el usuario en el siguiente formato:
#La información ingresada es la siguiente:
#Nombre completo: [nombre completo]
#Edad: [edad]
#Estatura: [estatura] cm
#Peso: [peso] kg
#Dirección: [dirección]
#Número de teléfono: [número de teléfono]

print('Formulario a completar:')
nombreCompleto = input('Ingresar nombres y apellido.. ej: "Juan Perez"')
edad = input('Ingresar edad ')
estatura = input('Ingresar estatura ')
peso = input('Ingresar peso ')
direccion = input('Ingresar dirección/domicilio ')
contacto = input('Por último ingresar un teléfono de contacto ')
print('Nombre Completo: ',nombreCompleto)
print('Edad: ',edad)
print('Estatura: ',estatura)
print('Peso: ',peso,' kg')
print('Dirección: ',direccion)
print('Número de teléfono: ',contacto)