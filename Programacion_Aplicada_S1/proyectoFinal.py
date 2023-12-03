# Proyecto 4: Cubilete
# - Poker de 5 dados.
# - Dos o más jugadores simultáneos.
# - Crédito y apuestas para cada jugador.
# - Apuesta igual para todos en cada juego.
# - Cada jugador puede repetir tiro, cambiando hasta 4 dados (conserva un dado como
# mínimo).
# - El programa tiene que calificar cada mano y determinar la mano ganadora, así como
# repartir el dinero de apuestas.
#--------------------------------------------------------------------------------------
import random

dadoCaras = ["SIETE_NEGROS", "OCHO_ROJOS", "J", "Q" , "K" , "AS"]

dadoValor = {
    "SIETE_NEGROS":7,
    "OCHO_ROJOS":8,
    "J":11,
    "Q":12,
    "K":13,
    "AS":1
}

jugada = {
    "PAR": 10,
    "2 PARES": 20,
    "TERCIA": 30,
    "FULL_HOUSE":40,
    "POCKER":50,
    "QUINTA":60
}

def DadoRandom():
    return dadoCaras[random.randint(0, 5)]

def Cubilete(): 
    dados = {
        "DADO_1":"",
        "DADO_2":"",
        "DADO_3":"",
        "DADO_4":"",
        "DADO_5":""
        }
    
    for posicion,dado in enumerate(dados):
        dados[dado] = DadoRandom()
    
    return dados

def PuntosObtenidos(dados):
    puntosObtenidos = 0
    
    return puntosObtenidos


cantidadJugadores = int(input("¿Cuantos jugadores habrá en la partida?: "))

listaJugadores = []
for numeroJugador in range(cantidadJugadores):
    jugador ={
        "nombre":f"jugador_{numeroJugador+1}",
        "dados":{},
        "credito":100,
        "apuesta":0,
        "mejorarMano":False,
        "puntos":0
    }
    listaJugadores.append(jugador)


#usoAS = input("¿El AS se usará como el valor manor de la mano [MAYOR] o menor de la mano del jugador [MENOR]?: (escribe tu respuesta) ").upper()
ronda = 0
creditoMesa = 0


while True:
    ronda += 1
    print(f"Ronda {ronda}")
    
    print("----------------------------------------------------")
    
    for jugador in listaJugadores:
        print(f"Jugador: {jugador['nombre']}")
        while jugador["apuesta"] == 0 or jugador["apuesta"] > jugador["credito"] or jugador["apuesta"] < 0:
            jugador["apuesta"] = int(input(f"¿Cuanto quieres apostar?:  tiene un credito de: {jugador['credito']}: "))
        jugador["credito"] -= jugador["apuesta"]
        print(f"Apuesta: {jugador['apuesta']}")
        
        print("----------------------------------------------------")
        
        print(f"Tiramos los dados del {jugador["nombre"]} y los dados son: ")
        jugador["dados"] = Cubilete()
        for dado in jugador["dados"]:
            print(f"{dado}: {jugador['dados'][dado]}")
        
        
        
    break