import os
import random
import math
import time
import pygame
from pygame.locals import *
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("TRON")
screen = pygame.display.set_mode((1280, 720))
XDDD = pygame.image.load("XDDD.jpg").convert()
XDC = pygame.image.load("XDC.jpg").convert()
XDD = pygame.image.load("XDD.jpg").convert()
finaltotal = 0




gameClock = pygame.time.Clock()


class Snake(object):


        def __init__(self):
                self.pos = [160, 304] 
                self.body = []    
                self.length = 3      
                self.angle = 270
                self.alive = True
                self.image = pygame.image.load("blueR.png")
                self.x = 160
                self.y = 300
                self.direction = "right"

               

        def update(self):

                self.body.insert(0, list(self.pos))

                if self.angle == 0:
                        self.pos[1] -= 16
                        self.y -= 16
                if self.angle == 90:
                        self.pos[0] -= 16
                        self.x -= 16
                if self.angle == 180:
                        self.pos[1] += 16
                        self.y += 16
                if self.angle == 270:
                        self.pos[0] += 16
                        self.x += 16


                for b in self.body:
                        if self.pos == b:
                                self.alive = False


                if self.pos[0] not in range(1280):
                        self.alive = False
                if self.pos[1] not in range(720):
                        self.alive = False



        def draw(self, surf):
                if self.direction == "right":
                        head = pygame.transform.rotate(self.image, 0)
                if self.direction == "left":
                        head = pygame.transform.rotate(self.image, 180)
                if self.direction == "up":
                        head = pygame.transform.rotate(self.image, 90)
                if self.direction == "down":
                        head = pygame.transform.rotate(self.image, 270)

                surf.blit(head, (self.x, self.y, 16, 16))

                for b in self.body:
                        surf.fill((0, 255, 230), (b[0], b[1], 16, 16))

class Snake2(object):

        def __init__(self):
                self.pos = [1152, 304] 
                self.body = []        
                self.length = 3       
                self.angle = 90        
                self.alive = True
                self.image = pygame.image.load("DGL.png")
                self.x = 1152
                self.y = 300
                self.direction = "left"

        def update(self):

                self.body.insert(0, list(self.pos))

                if self.angle == 0:
                        self.pos[1] -= 16
                        self.y -= 16
                if self.angle == 90:
                        self.pos[0] -= 16
                        self.x -= 16
                if self.angle == 180:
                        self.pos[1] += 16
                        self.y += 16
                if self.angle == 270:
                        self.pos[0] += 16
                        self.x += 16

                for b in self.body:
                        if self.pos == b:
                                self.alive = False

                if self.pos[0] not in range(1280):
                        self.alive = False
                if self.pos[1] not in range(720):
                        self.alive = False

        def draw(self, surf):
                if self.direction == "right":
                        head = pygame.transform.rotate(self.image, 180)
                if self.direction == "left":
                        head = pygame.transform.rotate(self.image, 0)
                if self.direction == "up":
                        head = pygame.transform.rotate(self.image, 270)
                if self.direction == "down":
                        head = pygame.transform.rotate(self.image, 90)

                surf.blit(head, (self.x, self.y, 16, 16))

                for b in self.body:
                        surf.fill((9, 255, 0), (b[0], b[1], 16, 16))

                        


def dist(x1,y1,x2,y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = math.sqrt(dsquared)
        return result
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def game_intro():
        
    intro = True
    hugeFont= pygame.font.Font( pygame.font.get_default_font(), 100)

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(XDDD,[0,0])
        gameovertext = hugeFont.render("Tron", 1, (255, 0, 0))
        screen.blit(gameovertext, (screen.get_width()/2-125, screen.get_height()/2-40))

        mouse = pygame.mouse.get_pos()

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, (0, 255, 0),(350,450,150,70))
        else:
            pygame.draw.rect(screen, (0, 255, 0),(350,450,150,70))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Start", smallText)
        textRect.center = ( (375+(100/2)), (460+(50/2)) )
        screen.blit(textSurf, textRect)

        pygame.draw.rect(screen, (255, 0, 0),(750,450,150,70))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Quit", smallText)
        textRect.center = ( (775+(100/2)), (460+(50/2)) )
        screen.blit(textSurf, textRect)
        button("Start",350,450,150,70,(0, 255, 0),(0, 250, 0),main)
        button("Quit",750,450,150,70,(255, 0, 0),(250, 0, 0),pygame.quit)
        
        pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def main():
    
        pygame.mixer.music.load('Surface.mp3')
        pygame.mixer.music.play(-1)
        snake = Snake()
        snake2= Snake2()
        outro = False
        
        font = pygame.font.Font(None, 32)
        defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
        hugeFont= pygame.font.Font( pygame.font.get_default_font(), 50)

        score1 =0
        score2= 0

        global finaltotal
        totaltime = 0
        finaltotal = 0


        while 1:
         
                gameClock.tick()
                totaltime += gameClock.get_time()
              
         
                for e in pygame.event.get():
                        if e.type == KEYDOWN:


                                if e.key == K_ESCAPE:
                                        pygame.quit()
                                        return

                                if e.key == K_w:
                                        snake.angle = 0
                                        snake.direction = "up"
                                        
                                if e.key == K_a:
                                        snake.angle = 90
                                        snake.direction = "left"
                                        
                                if e.key == K_s:
                                        snake.angle = 180
                                        snake.direction = "down"
                                        
                                if e.key == K_d:
                                        snake.angle = 270
                                        snake.direction = "right"
                                        


                            
                                if e.key == K_UP:
                                        snake2.angle = 0
                                        snake2.direction = "up"
                                        
                                if e.key == K_LEFT:
                                        snake2.angle = 90
                                        snake2.direction = "left"
                                        
                                if e.key == K_DOWN:
                                        snake2.angle = 180
                                        snake2.direction = "down"
                                        
                                if e.key == K_RIGHT:
                                        snake2.angle = 270
                                        snake2.direction = "right"

                pygame.display.flip()
                pygame.time.delay(40)
                snake.update()
                snake2.update()
        
                for b in snake.body:
                        if snake2.pos == b:
                                snake2.alive = False

                for b in snake2.body:
                        if snake.pos == b:
                                snake.alive = False



                if not snake.alive:
                        score2+=1 

                        if score2== 10:
                                 gameovertext = hugeFont.render("Player 2 WINS!", 1, (255, 0, 0))
                                 screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                 pygame.display.flip()
                                 pygame.time.wait(2000)
                                 score1=0
                                 score2=0
                                 snake = Snake()
                                 snake2= Snake2()
                                 finaltotal = finaltotal + totaltime
                                 totaltime= 0
                                 outro = True
                                 if outro == True:
                                         game_outro(main)
                                 
                        
                        else:
                                gameovertext = hugeFont.render("Player 1 has died", 1, (255, 0, 0))
                                screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                snake = Snake()
                                snake2 = Snake2()
                                finaltotal = finaltotal + totaltime
                                totaltime=0

                if not snake2.alive:
                        score1+=1

                        if score1== 10:
                                 gameovertext = hugeFont.render("Player 1 WINS!", 1, (255, 0, 0))
                                 screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                 pygame.display.flip()
                                 pygame.time.wait(2000)
                                 score1=0
                                 score2=0
                                 snake = Snake()
                                 snake2= Snake2()
                                 finaltotal = finaltotal + totaltime
                                 totaltime=0
                                 outro = True
                                 if outro == True:
                                         game_outro(main)
                        
                        else:
                                gameovertext = hugeFont.render("Player 2 has died", 1, (255, 255, 0))
                                screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                snake = Snake()
                                snake2= Snake2()
                                finaltotal = finaltotal + totaltime
                                totaltime=0

        

                screen.blit(XDC, (0,0))
                out = round(totaltime,2)


                snake.draw(screen)
                snake2.draw(screen)
                ren1 = defaultFont.render("Player 1 Score: "+str(score1), 1, (0,255,0))
                ren2 = defaultFont.render("Player 2 Score: "+str(score2), 1, (0,255,0))
                ren3 = defaultFont.render("Time: "+ str(out*0.001)+ "s", 1, (0,255,0))
                screen.blit(ren1, (0, 0))
                screen.blit(ren2, (1100, 0))
                screen.blit(ren3, (550, 0))
                pygame.display.flip()

                pygame.time.wait(100)

def game_outro(main):

    global finaltime
    x = finaltotal
    output = round(x,2)
    outro = True
    hugeFont= pygame.font.Font( pygame.font.get_default_font(), 100)
    smallFont= pygame.font.Font( pygame.font.get_default_font(), 30)

    while outro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                            pygame.quit()
                    if event.key == pygame.K_c:
                            main()

        screen.blit(XDD,[0,0])
        gameovertext1 = hugeFont.render("GameOver", 1, (102, 255, 255))
        screen.blit(gameovertext1, (screen.get_width()/2-500, screen.get_height()/2-40))
        gameovertext2 = smallFont.render("Press C to play again or press Q to quit", 1, (102, 255, 51))
        screen.blit(gameovertext2, (screen.get_width()/2-500, screen.get_height()/2+200))
        ren1 = smallFont.render("Total time: "+ str(output*0.001)+ "s", 1, (0,255,0))
        screen.blit(ren1, (screen.get_width()/2-500, screen.get_height()/2+100))
        pygame.display.update()

if __name__ == "__main__":

    game_intro()
    main()
    game_outro()
