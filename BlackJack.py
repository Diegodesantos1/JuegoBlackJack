import random

cartas = { 
    11:chr(0x1f0a1), 
    2:chr(0x1f0a2), 
    3:chr(0x1f0a3), 
    4:chr(0x1f0a4), 
    5:chr(0x1f0a5), 
    6:chr(0x1f0a6), 
    7:chr(0x1f0a7), 
    8:chr(0x1f0a8), 
    9:chr(0x1f0a9), 
    10:chr(0x1f0aa), 
    10:chr(0x1f0ab), 
    10:chr(0x1f0ad), 
    10:chr(0x1f0ae), 
}
numcartas=52
cartas=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Cartasquellevas=[]
Cartasquellevabanca=[]
numcartas=52
def tomar_carta():
    global numcartas
    numerorandom= random.randint (2, 11)
    carta_elegida=cartas.pop(numerorandom)
    print(f"Tienes esta carta: {carta_elegida}")
    Cartasquellevas.append(carta_elegida)
    numcartas-=1

def tomar_2carta():
    global numcartas
    numerorandom= random.randint (2, 11)
    carta_elegida=cartas.pop(numerorandom)
    print(f"Tienes esta carta: {carta_elegida}")
    Cartasquellevas.append(carta_elegida)
    numerorandom= random.randint (2, 11)
    carta_elegida=cartas.pop(numerorandom)
    print(f"Tienes esta carta: {carta_elegida}")
    Cartasquellevas.append(carta_elegida)
    numcartas -= 2

def banca_tomar_carta():
    global numcartas
    global puntuacion_banca
    puntuacion_banca=0
    numerorandom= random.randint (2, 11)
    puntuacion_banca=puntuacion_banca + numerorandom
    carta_elegida_banca=cartas.pop(numerorandom)
    Cartasquellevabanca.append(carta_elegida_banca)
    numcartas-= 1

def banca_tomar_2carta():
    global numcartas
    global puntuacion_banca
    puntuacion_banca=0
    numerorandom= random.randint (2, 11)
    puntuacion_banca=puntuacion_banca + numerorandom
    carta_elegida_banca=cartas.pop(numerorandom)
    Cartasquellevabanca.append(carta_elegida_banca)
    numerorandom= random.randint (2, 11)
    puntuacion_banca=puntuacion_banca + numerorandom
    carta_elegida_banca=cartas.pop(numerorandom)
    Cartasquellevabanca.append(carta_elegida_banca)
    numcartas-=2


def pasar_turno():
    print("Paso turno")

def plantarse():
    tu_puntuacion=sum(Cartasquellevas)
    print ("Me planto")
    if puntuacion_banca > 21 and tu_puntuacion < 21:
        print ("Has ganado el blackjack")
    elif tu_puntuacion > 21:
        print("Perdiste")
    elif tu_puntuacion < puntuacion_banca:
        print ("Perdiste")
    elif tu_puntuacion > puntuacion_banca and tu_puntuacion < 21:
        print("Ganaste")

def juego():
    print ("¿Qué deseas hacer?" + " 1: tomar otra carta, 2: pasar turno, 3: plantarse")
    eleccion=int(input())
    while eleccion != 3 or cartas :
        tomar_carta()
        print(Cartasquellevas)
    while eleccion == 2:
        pasar_turno()
    while eleccion ==3:
        plantarse()

print("Comienza el blackjack")
tomar_2carta()
banca_tomar_2carta()
print(Cartasquellevas)
juego()