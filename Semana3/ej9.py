num = int(input("Ingresa un número: "))

if num <= 0:
   print("Ingresa un número positivo")
else:
   n1, n2 = 0, 1
   count = 0
   if num == 1:
       print(n1)
   else:
       print("Secuencia de Fibonacci:")
       while count < num:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1