from random import random
import random
import sys, pygame
pygame.init()




def ColorRandom():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
# creamos la ventana de juego
tamano = (800, 600)
screen = pygame.display.set_mode(tamano)

amarillo = (255, 255, 0)
masa = 100
x = 100
y = 300
vx = 50 #px/seg
vy = 0 #px/seg
deltaT = 0.001 #segundos

aceleracionY = 1000 #px/seg^2

salir = False
while salir == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True
    
    #recalcular posicion
    x = x + vx * deltaT
    vyOriginal = vy
    vy = vyOriginal + aceleracionY * deltaT
    vyPromerdio = (vyOriginal + vy)/2
    y = y + vyPromerdio * deltaT
    
    energiaCinetica = (masa * (vy**2)/2)
    h = 600 - y
    energiaPotencial = masa * aceleracionY * h
    Et = energiaCinetica + energiaPotencial
    
    if x>=800: vx = -vx # pared derecha
    if x<=0: vx = -vx # pared izquierda
    if y>=600 and vy>0: # pared inferior
        vy = vy *-1*0.8 
        if abs(vy)<50: vy=0
        vx = vx * 0.8
        y = 600

    if y<=0: vy = -vy # pared superior
    
    
    
    
    #dibujamos la pelota
    screen.fill((0,0,0))
    pygame.draw.circle(screen, amarillo, (x,y), 5)
    pygame.draw.circle(screen, (255,0,0), (x,y), 2)
    
    #flip para pantalla
    pygame.display.flip()
    pygame.time.wait(int(deltaT*1000)) # 30 fps
    #print(x)



print("Game Over")