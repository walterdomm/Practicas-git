#ARGUMENTOS INDETERMINADOS NOMBRE
#KWARGS

def indeterminado_nombre(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} : {valor}')

print('Asistencia')
indeterminado_nombre(nombre="Walter", edad="31", comision="6")