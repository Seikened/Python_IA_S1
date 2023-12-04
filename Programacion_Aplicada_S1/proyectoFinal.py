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
from collections import Counter
import os


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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    
    for i,dado in enumerate(dados):
        dados[dado] = DadoRandom()
    
    return dados

def TipoJugada(conteo):
    conteos = {
        "PAR": 0,
        "2_PARES": False,
        "TERCIA": False,
        "FULL_HOUSE": False,
        "POCKER": False,
        "QUINTA": False
    }
    for cantidad in conteo.values():
        if cantidad == 2:
            conteos["PAR"] += 1
        elif cantidad == 3:
            conteos["TERCIA"] = True
        elif cantidad == 4:
            conteos["POCKER"] = True
        elif cantidad == 5:
            conteos["QUINTA"] = True

    if conteos["PAR"] == 2:
        conteos["2_PARES"] = True

    if conteos["TERCIA"] and conteos["PAR"] >= 1:
        conteos["FULL_HOUSE"] = True
    
    return conteos


def PuntosObtenidos(dados):
    valores_dados = list(dados.values())
    conteo = Counter(valores_dados)
    jugadaContada = TipoJugada(conteo)
    puntosObtenidos = 0
    nombreJugada = ""

    for dado in valores_dados:
        puntosObtenidos += dadoValor[dado]

    if jugadaContada["QUINTA"]:
        puntosObtenidos += jugada["QUINTA"]
        nombreJugada = "QUINTA"
    elif jugadaContada["POCKER"]:
        puntosObtenidos += jugada["POCKER"]
        nombreJugada = "POCKER"
    elif jugadaContada["FULL_HOUSE"]:
        puntosObtenidos += jugada["FULL_HOUSE"]
        nombreJugada = "FULL_HOUSE"
    elif jugadaContada["TERCIA"]:
        puntosObtenidos += jugada["TERCIA"]
        nombreJugada = "TERCIA"
    elif jugadaContada["2_PARES"]:
        puntosObtenidos += jugada["2 PARES"]
        nombreJugada = "2 PARES"
    elif jugadaContada["PAR"] == 1:
        puntosObtenidos += jugada["PAR"]
        nombreJugada = "PAR"

    return puntosObtenidos, nombreJugada





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
numeroRondas = int(input("¿Cuantas rondas se jugarán?: "))
ronda = 0
creditoMesa = 0


while True:
    clear_screen()
    ronda += 1
    print("----------------------------------------------------")
    print(f"Ronda {ronda}")
    
    for jugador in listaJugadores:
        print("----------------------------------------------------")
        print(f"Jugador: {jugador['nombre']}")
        while jugador["apuesta"] == 0 or jugador["apuesta"] > jugador["credito"] or jugador["apuesta"] < 0:
            
            jugador["apuesta"] = int(input(f"¿Cuanto quieres apostar?:  tiene un credito de: {jugador['credito']}: "))
            
        
        jugador["credito"] -= jugador["apuesta"]
        print(f"Credito Restante: {jugador['credito']}")
        print(f"Apuesta: {jugador['apuesta']}")
        
        print("--------------")
        
        print(f"Tiramos los dados del {jugador["nombre"]} y los dados son: ")
        jugador["dados"] = Cubilete()
        for dado in jugador["dados"]:
            print(f"{dado}: {jugador['dados'][dado]}")
        
        puntosJugador,jugadorJugada = PuntosObtenidos(jugador["dados"])
        print(f"Puntos obtenidos por el jugador {jugador["nombre"]}: {puntosJugador} y su tipo de jugada es: {jugadorJugada}")
        

        jugador["puntos"] = puntosJugador
        jugador["jugada"] = jugadorJugada



        print("---------------------------------------------------------------")
        print("¿Desea mejorar su mano? [SI] o [NO]")
        respuesta = input("Escribe tu respuesta: ").upper()
        if respuesta == "SI":
            print("¿Cuantos dados desea cambiar?")
            cantidadDadosCambiar = int(input("Escribe tu respuesta: "))
            if cantidadDadosCambiar > 4 or cantidadDadosCambiar < 0:
                print("No puedes cambiar esa cantidad de dados")
            else:
                for i in range(cantidadDadosCambiar):
                    print(f"¿Que dado desea cambiar? (escribe el nombre del dado)")
                    dadoCambiar = input("Escribe tu respuesta: ").upper()
                    if dadoCambiar in jugador["dados"]:
                        jugador["dados"][dadoCambiar] = DadoRandom()
                        print(f"El dado {dadoCambiar} ha sido cambiado por {jugador["dados"][dadoCambiar]}")
                    else:
                        print("Ese dado no existe")
                puntosJugador,jugadorJugada = PuntosObtenidos(jugador["dados"])
                print(f"Puntos obtenidos por el jugador {jugador["nombre"]}: {puntosJugador} y su tipo de jugada es: {jugadorJugada}")
        else:
            print("El jugador no desea mejorar su mano")

            
        jugador["puntos"] = puntosJugador
        # Creditos y apuestas
        creditoMesa += jugador["apuesta"]
        jugador["apuesta"] = 0
    
    
    # Determinar ganador
    ganador = ""
    ganadorPuntos = 0
    empate = False

    for jugador in listaJugadores:
        if jugador["puntos"] > ganadorPuntos:
            ganador = jugador["nombre"]
            ganadorPuntos = jugador["puntos"]
            empate = False
        elif jugador["puntos"] == ganadorPuntos:
            empate = True

    if empate:
        print("----------------------------------------------------")
        print("Empate")
        print("----------------------------------------------------")
        print("Se repartirá el credito de la mesa entre los jugadores empatados")
        creditos_a_repartir = creditoMesa / len([j for j in listaJugadores if j["puntos"] == ganadorPuntos])
        for jugador in listaJugadores:
            if jugador["puntos"] == ganadorPuntos:
                jugador["credito"] += creditos_a_repartir
                print(f"El jugador {jugador['nombre']} ha ganado {creditos_a_repartir} de credito")
    else:
        print("----------------------------------------------------")
        print(f"El ganador de la ronda {ronda} es: {ganador}")
        print("----------------------------------------------------")
        print(f"El jugador {ganador} ha ganado {creditoMesa} de credito")
        for jugador in listaJugadores:
            if jugador["nombre"] == ganador:
                jugador["credito"] += creditoMesa

    creditoMesa = 0


    for jugador in listaJugadores:
        jugador["puntos"] = 0
        jugador["dados"] = {}
        jugador["mejorarMano"] = False




    
    
    input("Presiona ENTER para continuar")
    if ronda == numeroRondas:
        break