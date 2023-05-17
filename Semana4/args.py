#ARGUMENTOS INDETERMINADOS POSICIONALES

#arbitrary arguments #por convención se deja args pero se puede modificar

def suma(*args):
    total = 0
    for n in args:
        total += n
    return total

print(suma(), suma(2, 2), suma(9, 9, 9))

## ejemplo con el nombre modificado:
def info(*profes):
    print("Esta hablando: " + profes[2])

info("Rami", "Cris", "Mica")