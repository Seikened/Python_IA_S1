import sys, pygame
pygame.init()

# creamos la ventana de juego
tamano = (800, 600)
screen = pygame.display.set_mode(tamano)

amarillo = (255, 255, 0)

x = 10
y = 10
vx = 60 #px/seg
vy = 100 #px/seg
deltaT = 0.010 #segundos

salir = False
while salir == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True
    
    #recalcular posicion
    x = x + vx * deltaT
    y = y + vy * deltaT
    
    #dibujamos la pelota
    screen.fill((0,0,0))
    pygame.draw.circle(screen, amarillo, (x,y), 20)
    
    #flip para pantalla
    pygame.display.flip()
    pygame.time.wait(10)
    print(x)



print("Game Over")