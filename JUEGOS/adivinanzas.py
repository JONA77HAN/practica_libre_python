import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número del 1 al 10")

    while True:
        guess = int(input("¿Cuál pensas que es? "))

        intentos += 1

        if guess == numero_secreto:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
        else:
            print("¡Incorrecto! Inténtalo de nuevo.")

if __name__ == "__main__":
    juego_adivinanza()
