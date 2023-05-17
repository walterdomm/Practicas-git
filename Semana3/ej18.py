#Escribe un programa que pida al usuario un número y luego imprima un
#triángulo de números como el siguiente:
#1
#2 3
#4 5 6
#7 8 9 10

n = int(input('Ingrese un número: '))

numero = 1

for i in range(n):
    for j in range(i+1):
        print(numero, end=" ")
        numero += 1
    print()


#otra posible solución:

num = int(input("Ingrese un número: "))

current_num = 1
for i in range(1, num+1):
    for j in range(i):
        if current_num > num:
            break
        print(current_num, end=" ")
        current_num += 1
    print()
    if current_num > num:
        break