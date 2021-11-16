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
global tomar_carta
def tomar_carta():
    num_cartas=0
    puntuacion=0
    total = 21
    global carta_elegida
    numerorandom= random.randint (2, 11)
    carta_elegida=cartas.pop(numerorandom)
    print(f"Tienes esta carta: {carta_elegida}")
    num_cartas=+1
    print(num_cartas)
    print(puntuacion)
tomar_carta()

#while num_cartas < 4 and puntuacion != 21:
#tomar_carta()

