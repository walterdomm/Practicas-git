#Escribe un programa que imprima los números pares del 1 al 100.
print('Los números pares del 1 al 100 son:')
for n in range(1, 100+1):
    if n % 2 == 0:
        print(n)

#OTRA FORMA:

print('Los números pares del 1 al 100 son:')
for n in range(2, 101, 2):
    print(n)