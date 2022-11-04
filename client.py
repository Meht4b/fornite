import pygame
from gameclass import *

win = pygame.display.set_mode((1000,1000))

p1 = Player(50,50,(255,0,0),10,10,30)

clock = pygame.time.Clock()

enemyLis = []

while True:

    for eve in pygame.event.get():
            
        if eve.type==pygame.QUIT:
            pygame.quit()


    win.fill((0,0,0))

    if p1.collisionSelf():
        break

    for ene in enemyLis:
        if p1.collisionEnemy(ene):
            break

    p1.update(win)

    pygame.display.update()

    clock.tick(60)
    
while True:
    print('you lost dumbass')

    for eve in pygame.event.get():
                
        if eve.type==pygame.QUIT:
            pygame.quit()
