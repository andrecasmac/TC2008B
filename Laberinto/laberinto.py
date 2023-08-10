import pygame, sys, random
from pygame.locals import *

laberinto = [
    "WWWWWWWWWWWWWWWWW",
    "____W_____W___W_W",
    "W_WWW_W_W_W_W_W_W",
    "W_W___W_W___W_W_W",
    "W_W_WWW_WWWWW_W_W",
    "W_____W_W_______W",
    "W_WWWWW_WWWWWWWWW",
    "W_W_W_W_________W",
    "W_W_W_WWW_WWWWW_W",
    "W___W___W___W___W",
    "WWWWWWW_WWWWW_W_W",
    "W_______W___W_W_W",
    "W_WWWWWWW_W_W_W_W",
    "W_____W___W___W_W",
    "WWWWW_W_WWWWWWW_W",
    "W_______W_______E",
    "WWWWWWWWWWWWWWWWW"
]

class Player(object):
    def __init__(self):
        self.size = 40
        self.x = 40
        self.y = 0
    
    def getRect(self):
        return (self.x, self.y, self.size, self.size)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((680, 680))

walls = set()
clock = pygame.time.Clock()
jugador = Player()

for r, row in enumerate(laberinto):
    for c, char in enumerate(row):
        if char == "W":
            walls.add((r*40, c*40, 40, 40))
        elif char == "E":
            end = (r*40, c*40, 40, 40)


while True: # Main game loop
    DISPLAYSURF.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if (jugador.x-jugador.size, jugador.y, jugador.size, jugador.size) not in walls:
                    jugador.x -= jugador.size
            if event.key == K_RIGHT:
                if (jugador.x+jugador.size, jugador.y, jugador.size, jugador.size) not in walls:
                    jugador.x += jugador.size
            if event.key == K_DOWN:
                if (jugador.x, jugador.y+jugador.size, jugador.size, jugador.size) not in walls:
                    jugador.y += jugador.size
            if event.key == K_UP:
                if (jugador.x, jugador.y-jugador.size, jugador.size, jugador.size) not in walls:
                    jugador.y -= jugador.size

    for wall in walls:
        pygame.draw.rect(DISPLAYSURF, (0, 0, 0), wall)
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), jugador.getRect())
    pygame.draw.rect(DISPLAYSURF, (255,215,0), end)
    
    if jugador.getRect() == end:
        for i in range(5):
            DISPLAYSURF.fill((255,215,0))
            pygame.display.update()
            pygame.time.wait(75)
            DISPLAYSURF.fill((0,0,0))
            pygame.display.update()
            pygame.time.wait(75)
            
        pygame.quit()
        sys.exit()

    pygame.display.update()