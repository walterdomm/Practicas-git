import random #Se importa el módulo random para generar un número aleatorio con la función randint.

intentos_realizados = 8
nombre = input('¡Hola! ¿cual es tu nombre? \n')
numero = random.randint(1, 100) #Genera un número aleatorio del 1 al 100.
print(f'¡Bienvenido/a {nombre}! En este juego debes adivinar un número del 1 al 100.\nPara ello tienes 8 intentos.')

while intentos_realizados > 0 :
    print(f"Te quedan: {intentos_realizados} intentos.")
    numero_a_adivinar =input('Intenta adivinar: ')
    
    if not numero_a_adivinar.isdigit(): #La función isdigit() verifica si todos los caracteres en una cadena son dígitos. Retorna True si es así, de lo contrario False.
        print("Lo siento, debes intentar nuevamente ya que lo ingresado no es un numero entero.")
        continue #En caso de que no ingrese un número entero, vuelve atrás en el ciclo. 

    numero_a_adivinar = int(numero_a_adivinar)
    
    if numero_a_adivinar < numero: #Si el número ingresado es MAYOR al "número a adivinar", vuelve atrás en el ciclo.
        print('El número a adivinar es mayor.')
        intentos_realizados -= 1
    
    elif numero_a_adivinar > numero: #Si el número ingresado es MENOR al "número a adivinar", vuelve atrás en el ciclo.
        print('El número a adivinar es menor.')
        intentos_realizados -= 1
       
    else:
        print(f'¡Excelente, {nombre}! Adivinaste el número en {9-intentos_realizados} intentos.')
        break

if intentos_realizados == 0: #En el caso de no adivinar el número, le informa cual era. 
    print(f'Lamentablemente se agotaron todas las oportunidades, el numero era el {numero}.')

#GRUPO 5
#Alvarez Edith
#Domingues Edgar Walter 
#Duarte Maria Lourdes
#Gómez Yordanovich Tiziana Ailén  
#Rodas Sebastian
#Sabadini Roa Axel Emanuel
#Vazquez Sara