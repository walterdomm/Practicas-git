#Escribe un programa que pida al usuario una cadena de texto y determine
#cuántas veces aparece cada letra en la cadena.

texto = input('Ingresa un texto cualquiera: ')

texto = texto.lower()

frecuencias = {}

for l in texto:
    if l == " ":
        continue
    if l not in frecuencias:
        frecuencias[l] = 1
    else:
        frecuencias[l] += 1

for l, frecuencias in frecuencias.items():
    print(f'La letra {l} aparece {frecuencias} vez/veces en la cadena.')