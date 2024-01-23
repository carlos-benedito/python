import random

class Carta:
    def __init__(self, nombre, palo, valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.nombre}"

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []

    def tomar_decision(self):
        return input(f"{self.nombre}, ¿quieres tomar otra carta? (s/n): ").lower()

def crear_baraja():
    baraja = []
    palos = ["bastos", "oros", "copas", "espadas"]
    valores = list(range(1, 11)) + [10, 10, 10]

    for palo in palos:
        for n in range(1, 11):
            if n == 1:
                baraja.append(Carta(f"As de {palo}", palo, 1))
            elif n == 8:
                baraja.append(Carta(f"Sota de {palo}", palo, 10))
            elif n == 9:
                baraja.append(Carta(f"Caballo de {palo}", palo, 10))
            elif n == 10:
                baraja.append(Carta(f"Rey de {palo}", palo, 10))
            else:
                baraja.append(Carta(f"{n} de {palo}", palo, n))

    random.shuffle(baraja)
    return baraja

def valor_carta(cartas):
    valor = 0
    tiene_as = False
    for carta in cartas:
        valor += carta.valor
        if carta.nombre.startswith('As'):
            tiene_as = True
    if tiene_as and valor + 10 <= 21:
        valor += 10
    return valor

def repartir_carta(baraja):
    if not baraja:
        print("La baraja está vacía. Reiniciando...")
        baraja = crear_baraja()
    return baraja.pop()

def mostrar_cartas(jugador):
    print(f"\nCartas de {jugador.nombre}:")
    for carta in jugador.cartas:
        print(f"{carta}")
    print(f"Puntuación de {jugador.nombre}: {valor_carta(jugador.cartas)}")

def crear_jugador(nombre):
    return Jugador(nombre)

def jugar_las_21():
    rondas_ganadas_jugador1 = 0
    rondas_ganadas_banca = 0

    jugador1 = crear_jugador(input("Ingresa el nombre del primer jugador: "))

    while True:
        baraja = crear_baraja()

        jugador1.cartas = [repartir_carta(baraja), repartir_carta(baraja)]
        banca = Jugador("Banca")
        banca.cartas = [repartir_carta(baraja), repartir_carta(baraja)]

        mostrar_cartas(jugador1)
        mostrar_cartas(banca)

        # Turno del primer jugador
        while True:
            eleccion = jugador1.tomar_decision()
            if eleccion == 's':
                jugador1.cartas.append(repartir_carta(baraja))
                mostrar_cartas(jugador1)
                if valor_carta(jugador1.cartas) > 21:
                    print(f"{jugador1.nombre}, ¡te has pasado de 21! Has perdido la ronda.")
                    rondas_ganadas_banca += 1
                    break
            else:
                break

        # Turno de la banca (juega automáticamente)
        while valor_carta(banca.cartas) < 17:
            banca.cartas.append(repartir_carta(baraja))

        mostrar_cartas(jugador1)
        mostrar_cartas(banca)

        # Evaluar el resultado de la ronda
        if valor_carta(jugador1.cartas) <= 21 and valor_carta(banca.cartas) <= 21:
            if valor_carta(jugador1.cartas) > valor_carta(banca.cartas):
                print(f"{jugador1.nombre}, ¡has ganado la ronda!")
                rondas_ganadas_jugador1 += 1
            elif valor_carta(jugador1.cartas) < valor_carta(banca.cartas):
                print("La banca ha ganado la ronda.")
                rondas_ganadas_banca += 1
            else:
                print("Empate en esta ronda.")
        elif valor_carta(jugador1.cartas) <= 21:
            print(f"{jugador1.nombre}, ¡has ganado la ronda!")
            rondas_ganadas_jugador1 += 1
        elif valor_carta(banca.cartas) <= 21:
            print("La banca ha ganado la ronda.")
            rondas_ganadas_banca += 1
        else:
            print("Ambos jugadores se han pasado de 21. Es un empate.")

        print(f"\nRondas ganadas por {jugador1.nombre}: {rondas_ganadas_jugador1}")
        print(f"Rondas ganadas por la banca: {rondas_ganadas_banca}")

        continuar = input("¿Quieren jugar otra ronda? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    jugar_las_21()

