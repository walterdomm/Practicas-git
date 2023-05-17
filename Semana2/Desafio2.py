
print('ANALIZADOR DE TEXTO:')
texto = input("Ingresar un texto: ").lower()


l1 = input("Ingresar 3 letras a su elección: ").lower()
l2 = input("Ingresar 3 letras a su elección: ").lower()
l3 = input("Ingresar 3 letras a su elección: ").lower()

lista1 = [l1, l2, l3]

print(f" 1) \n La letra \'{lista1[0]}\' aparece {texto.count(l1)} veces. \n La letra \'{lista1[1]}\' aparece {texto.count(l2)} veces. \n La letra \'{lista1[2]}\' aparece { texto.count(l3)} veces.")
lista2 = texto.split()

print(" 2) Hay", len(lista2), "palabras.")


print(f" 3) La primer letra es la \'{texto[0]}\' y la ultima letra es la \'{texto[-1]}\'.")

print(" 4) El texto en orden inverso quedaría así:")
print(f' {texto[::-1]}' )

palabra_python = 'python' in texto
respuesta = {True: 'Si', False: 'No'}[palabra_python]
print(' 5)La palabra \'python\' aparece en el texto?')
print(f' {respuesta}!')

#Integrantes:
##Ricardo Luis Gomez
##Tiziana Ailén Gómez Yordanovich
##Edgar Walter Domingues
##Sergio Omar Montes
##Duarte Maria Lourdes
##Vazquez Sara 
##Rodas Sebastian
##Alvarez Edith
##Gauna Franco
##Sabadini Roa Axel Emanuel