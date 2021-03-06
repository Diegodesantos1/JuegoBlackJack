import random
import sys
dibujocartas = {
    11: chr(0x1f0a1),
    2: chr(0x1f0a2),
    3: chr(0x1f0a3),
    4: chr(0x1f0a4),
    5: chr(0x1f0a5),
    6: chr(0x1f0a6),
    7: chr(0x1f0a7),
    8: chr(0x1f0a8),
    9: chr(0x1f0a9),
    10: chr(0x1f0aa),
    10: chr(0x1f0ab),
    10: chr(0x1f0ad),
    10: chr(0x1f0ae),
}
print(dibujocartas)

cartas = list(dibujocartas.keys()) * 4

# He transformado el diccionario en una lista

Cartasquellevas = []
Cartasquellevabanca = []
numcartas = 52


def comprobarcartas():
    if numcartas == 0 or numcartas < 0:
        print("Se han terminado las cartas")
        plantarse()


def elegir_jugadores():  # creada función para implementar más jugadores (hecho en clase)
    nombres = []
    jugadores = int(input('¿Cuantos jugadores van a jugar?: '))
    for i in range(jugadores):
        nombre = str(input('Nombre del jugador ' + str(i + 1)))
        nombres.append(nombre)


def tomar_carta():
    comprobarcartas()
    global numcartas
    numerorandom = random.randint(1, len(cartas))
    carta_elegida = cartas.pop(numerorandom)
    print(f"Tienes esta carta: {carta_elegida}")
    Cartasquellevas.append(carta_elegida)
    numcartas -= 1
    print(Cartasquellevas)


def tomar_2carta():  # No hace falta poner la función comprobarcartas, ya que es la que se ejecuta al inicio del programa
    global numcartas
    global carta_elegida
    numerorandom = random.randint(1, len(cartas))
    carta_elegida = cartas.pop(numerorandom)
    print(f"Tienes esta carta: {carta_elegida}")
    Cartasquellevas.append(carta_elegida)
    numerorandom = random.randint(1, len(cartas))
    carta_elegida = cartas.pop(numerorandom)
    print(f"Tienes esta carta: {carta_elegida}")
    Cartasquellevas.append(carta_elegida)
    numcartas -= 2


def banca_tomar_carta():
    comprobarcartas()
    global carta_elegida_banca
    global numcartas
    numerorandom = random.randint(1, len(cartas))
    carta_elegida_banca = cartas.pop(numerorandom)
    Cartasquellevabanca.append(carta_elegida_banca)
    numcartas -= 1


def banca_tomar_2carta():  # No hace falta poner la función comprobarcartas, ya que es la que se ejecuta al inicio del programa
    global numcartas
    numerorandom = random.randint(1, len(cartas))
    carta_elegida_banca = cartas.pop(numerorandom)
    Cartasquellevabanca.append(carta_elegida_banca)
    numerorandom = random.randint(1, len(cartas))
    carta_elegida_banca = cartas.pop(numerorandom)
    Cartasquellevabanca.append(carta_elegida_banca)
    numcartas -= 2


def cambiar_cartas():
    print("¿Qué carta quieres cambiar? Pon la posición 0, 1, 2 de la carta que desee eliminar")
    seleccion_cambio = int(input())
    Cartasquellevas.pop(seleccion_cambio)


def cambiar_cartas_banca():
    seleccion_cambio = random.randint(0, 2)
    Cartasquellevabanca.pop(seleccion_cambio)


def pasar_turno():
    comprobarcartas()
    print("Paso turno")


def plantarse():
    tu_puntuacion = sum(Cartasquellevas)
    puntuacion_banca = sum(Cartasquellevabanca)
    if puntuacion_banca > 21 and tu_puntuacion < 21:
        print(
            f"Has ganado el blackjack, tu puntuación ha sido {tu_puntuacion} y la banca ha tenido {puntuacion_banca} puntos")
    elif tu_puntuacion > 21:
        print(
            f"Has perdido el blackjack, tu puntuación ha sido {tu_puntuacion} y la banca ha tenido {puntuacion_banca} puntos")
    elif tu_puntuacion < puntuacion_banca <= 21:
        print(
            f"Has perdido el blackjack, tu puntuación ha sido {tu_puntuacion} y la banca ha tenido {puntuacion_banca} puntos")
    elif tu_puntuacion > puntuacion_banca and tu_puntuacion <= 21:
        print(
            f"Has ganado el blackjack, tu puntuación ha sido {tu_puntuacion} y la banca ha tenido {puntuacion_banca} puntos")
    elif tu_puntuacion == puntuacion_banca:
        print(
            f"Has empatado al blackjack, tu puntuación ha sido {tu_puntuacion} y la banca ha tenido {puntuacion_banca} puntos")
    sys.exit()


def juegobanca():
    comprobarcartas()
    if sum(Cartasquellevabanca) >= 16:
        plantarse()
    else:
        eleccion_banca = random.randint(4, 5)
        if eleccion_banca == 4:
            if len(Cartasquellevabanca) == 3:
                cambiar_cartas_banca()
            else:
                banca_tomar_carta()
                juego()
        elif eleccion_banca == 5:
            print("Ha pasado turno la banca")


def juego():
    comprobarcartas()
    print(f"Quedan {numcartas} cartas")
    print("¿Qué deseas hacer?" +
          " 1: tomar otra carta, 2: pasar turno, 3: plantarse")
    eleccion = int(input())
    if eleccion == 1:
        print()
    elif eleccion == 2:
        print()
    elif eleccion == 3:
        plantarse()
    while eleccion != 3:
        if eleccion == 1:
            if len(Cartasquellevas) == 3:
                cambiar_cartas()
                tomar_carta()
                juegobanca()
                juego()
            else:
                tomar_carta()
                juegobanca()
                juego()
        elif eleccion == 2:
            pasar_turno()
            juegobanca()
            juego()


print("Comienza el blackjack")
tomar_2carta()
banca_tomar_2carta()
print(Cartasquellevas)
juego()
