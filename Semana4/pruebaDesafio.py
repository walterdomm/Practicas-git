import random

name = input("¡Hola! ¿Cómo te llamas? ")

print(f"Bienvenido(a) {name} a mi juego de adivinar el número.")
print("Estoy pensando en un número entre 1 y 100. Tienes 8 intentos para adivinarlo.")

number_to_guess = random.randint(1, 100)
attempts_left = 8

while attempts_left > 0:
    print(f"Te quedan {attempts_left} intentos.")
    guess = input("¿Cuál es tu número? ")

    if not guess.isdigit():
        print("Lo siento, eso no es un número entero. Intenta de nuevo.")
        continue

    guess = int(guess)

    if guess < number_to_guess:
        print("El número a adivinar es mayor.")
        attempts_left -= 1
    elif guess > number_to_guess:
        print("El número a adivinar es menor.")
        attempts_left -= 1
    else:
        print(f"¡Felicidades {name}! ¡Adivinaste el número en {9-attempts_left} intentos!")
        break

if attempts_left == 0:
    print(f"Lo siento {name}, se agotaron tus intentos. El número a adivinar era {number_to_guess}.")