import pygame
import math

class rec:
    
    def __init__(self,posx,posy,colour,size):
        self.posx=posx
        self.posy=posy

        self.colour=colour

        self.velx=0
        self.vely=0

        self.size = size

    def move(self):

        self.posx += self.velx
        self.posy += self.vely

    def draw(self,win):

        pygame.draw.rect(win,self.colour,(self.posx,self.posy,self.size,self.size))


class Player(rec):

    def __init__(self,posx,posy,colour,speed,size,length):
        super().__init__(posx,posy,colour,size)

        self.trailLis = []
        self.speed = speed
        self.length = length

    def mouseMov(self,vel):
        mx,my = pygame.mouse.get_pos()

        disx,disy = mx-self.posx,my-self.posy

        angle = math.atan(abs(disy/disx))


        if disx<0 and disy>0:

            self.velx=-math.cos(angle)*vel
            self.vely=math.sin(angle)*vel

        elif disx<0 and disy<0:

            self.velx=-math.cos(angle)*vel
            self.vely=-math.sin(angle)*vel

        elif disx>0 and disy<0:

            self.velx=math.cos(angle)*vel
            self.vely=-math.sin(angle)*vel

        elif disx>0 and disy>0:

            self.velx=math.cos(angle)*vel
            self.vely=math.sin(angle)*vel


    def trail(self,length):

        if len(self.trailLis)>length:

            del self.trailLis[0]

        self.trailLis.append(rec(self.posx,self.posy,self.colour,self.size-3))

    def collisionEnemy(self,enemy):

        #checks if we need to check collision, i.e. enemy is too far away

        if abs(self.posx-enemy.posx)>enemy.length and abs(self.posy-enemy.posy)>enemy.length:
            return False

        #checks collision, returns True if collision
        
        for t in enemy.trailLis:
            if pygame.Rect.colliderect(pygame.Rect(self.posx,self.posy,self.size,self.size),pygame.Rect(t.posx,t.posy,t.size,t.size)):
                return True
        return False

    def collisionSelf(self):

        #checks collision, returns True if collision 

        for i,t in enumerate(self.trailLis):

            if i > len(self.trailLis)-3:
                continue

            if pygame.Rect.colliderect(pygame.Rect(self.posx,self.posy,self.size,self.size),pygame.Rect(t.posx,t.posy,t.size,t.size)):
                print(self.posx,self.posy,t.posx,t.posy)
                print(i)
                return True
        return False
        
    def drawPlayer(self,win):

        self.draw(win)

        for tra in self.trailLis:
            
            tra.draw(win)

    def update(self,win):

        #calls all the methods to be called every frame

        self.trail(self.length)
        self.drawPlayer(win)
        self.mouseMov(self.speed)
        self.move()
