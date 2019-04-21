from pygame.locals import *
import pygame
import time
import random
#test

class Snake:
    #x = [60,40,20]
    #y = [20,20,20]
    
    x = []
    y = []

    speed = 20
    direction = 1
    length = 0

    def __init__(self):
        self.x.append( random.randint(0,40)*20 )
        self.y.append( random.randint(0,30)*20 )
        self.length = 1

    def Update(self):
        if self.direction == 0:
           self.zamien()
           self.y[0] = self.y[0] - self.speed

        if self.direction == 1:
            self.zamien()
            self.x[0]= self.x[0] + self.speed

        if self.direction == 2:
            self.zamien()
            self.y[0] = self.y[0] + self.speed

        if self.direction == 3:
            self.zamien()
            self.x[0] = self.x[0] - self.speed
            
        #print(self.x)
        #print(self.y)
        time.sleep (100.0 / 1000.0);


    def add(self):
        self.x.append(self.x[0])
        self.y.append(self.y[0])
        self.length+=1
        #self.zamien()
        print(self.length)

    def zamien(self):
        for i in range(self.length-1, 0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]


    def CollisionCheck(self):
        if(self.x[0]<0):
            return False

        if(self.x[0]>=800):
            return False

        if(self.y[0]<0):
            return False

        if(self.y[0]>=600):
            return False

        for i in range(1,self.length):
            if self.x[i] == self.x[0] and self.y[i] == self.y[0]:
                return False

        return True


    def MoveLeft(self):
        if  self.length > 1 and self.x[1] >= self.x[0]:
            self.direction = 3
        elif self.length == 1:
            self.direction = 3

    def MoveRight(self):
        if self.length > 1 and self.x[1] <= self.x[0]:
            self.direction = 1
        elif self.length == 1:
            self.direction = 1

    def MoveUp(self):
        if self.length > 1 and self.y[1] >= self.y[0]:
            self.direction = 0
        elif self.length == 1:
            self.direction = 0

    def MoveDown(self):
        if self.length > 1 and self.y[1] <= self.y[0]:
            self.direction = 2
        elif self.length == 1:
            self.direction = 2




class Punkt:
    x=60
    y=60

    def Update(self,wunsz):
        if self.x == wunsz.x[0] and self.y == wunsz.y[0]:
            wunsz.add()
            self.x= random.randint(0,40)*20
            self.y= random.randint(0,30)*20




class App:
    windowWidth = 800
    windowHeight = 600
    player = 0


    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._image_japko = None
        self._myfont = None
        self.wonsz = Snake() 
        self.punkt = Punkt()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Wunsz')
        self._running = True
        self._image_surf = pygame.image.load("Wonsz.png").convert()
        self._image_japko = pygame.image.load("Japko.png").convert()
        self._myfont = pygame.font.SysFont('Comic Sans MS', 30)
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))

        for i in range(0,self.wonsz.length):
            self._display_surf.blit(self._image_surf,(self.wonsz.x[i],self.wonsz.y[i]))

        self._display_surf.blit(self._image_japko,(self.punkt.x, self.punkt.y))

       # self._display_surf.blit(str(self._myfont.render(self.wonsz.length), False, (0, 0, 255)),(0,0))

        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):


            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.wonsz.MoveRight()
 
            if (keys[K_LEFT]):
                self.wonsz.MoveLeft()
 
            if (keys[K_UP]):
                self.wonsz.MoveUp()
 
            if (keys[K_DOWN]):
                self.wonsz.MoveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False

            #if(keys[K_w]):
                #self.wonsz.add()

            if self.wonsz.CollisionCheck() == False:
                self._running = False

            self.punkt.Update(self.wonsz)

            self.wonsz.Update()

 
            self.on_loop()
            self.on_render()
           # time.sleep (100.0 / 1000.0);

        self.on_cleanup()
 


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()


