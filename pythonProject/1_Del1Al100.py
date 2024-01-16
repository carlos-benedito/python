
import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego de adivinanza!")

while True:
    intento_usuario = int(input("Introduce tu intento (entre 1 y 100): "))
    intentos += 1
    if intento_usuario == numero_secreto:
        print(f"Felicidades, ¡adivinaste el número en {intentos} intentos!")
        break
    elif intento_usuario < numero_secreto:
        print("Intenta con un número mayor.")
    else:
        print("Intenta con un número menor.")