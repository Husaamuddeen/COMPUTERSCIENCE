import pygame
from sys import exit
import time

class InputBox:
    def __init__(self, inHeight, inWidth, inColour):
        self.height = height
        self.width = width
        self.colour = colour
        

    def move(self):
        mouse_pos = pygame.mouse.get_pos()
        if buttonrec.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed()[0]:
                print('maths')

#class to hold all the data about a triangle: sides, angles, area, perimeter
class Triangle:
    def __init__(self, _a, _b, _c, _A, _B, _C, _area, _perimeter):
        self.a = _a
        self.b = _b
        self.c = _c
        self.A = _A
        self.B = _B
        self.C = _C
        self.area = _area
        self.perimeter = _perimeter

#initialise pygame screen
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('graphs')
clock = pygame.time.Clock()

#set default font
font = pygame.font.Font(None,50)
pygame.draw.line(screen,'blue',(800,0),(800,800))
#pygame.draw.line(screen,'white',(0,400),(800,400))
#pygame.draw.line(screen,'white',(400,0),(400,800))

def constructTriangle():
    a = 3
    longest = a
    workingTriangle = Triangle(a,None,None,None,None,None,None,None)
    scale = 600/a
    line_a = pygame.draw.line(screen, 'white', (50,550), (50+scale*a,550))
    b = int(input(': '))
    if b > longest:
        line_a = 0
        pygame.display.flip()
        longest = b

class Button:
    def __init__(self, _height, _width, _colour, _centre):
        self.height = _height
        self.width = _width
        self.colour = _colour
        self.centre = _centre
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill(self.colour)
        self.rect = self.surface.get_rect(center = self.centre)

class Image:
    def __init__(self, _path, _centre):
        self.centre = _centre
        self.surface = pygame.image.load(_path)
        self.rect = self.surface.get_rect(center = self.centre)

#main animation loop
def mainMenu():
    screen.fill('black')
    buttons = [Image('project/images/options.png',(500,400)),Image('project/images/modules.png',(600,400)),Image('project/images/saves.png',(700,400))]
    #buttons = [Image('project\\images\options.png',(500,400)),Image('project\\images\modules.png',(600,400)),Image('project\\images\saves.png',(700,400))]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #update surfaces
        screen.blit(buttons[0].surface, buttons[0].rect)

        #check for mouse collisions and mouse presses
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface, buttons[i].rect)
            if buttons[i].rect.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        case 0:
                            print('options')
                        case 1:
                            modules()
                        case 2:
                            print('settings')

        pygame.display.update()
        clock.tick(60)

def modules():
    screen.fill('black')
    #buttons = [Button(100,250,'yellow',(300,200)),Button(100,250,'yellow',(600,200)),Button(100,250,'yellow',(900,200)),
    #           Button(100,250,'yellow',(300,400)),Button(100,250,'yellow',(600,400)),Button(100,250,'yellow',(900,400)),
    #           Button(100,250,'yellow',(300,600)),Button(100,250,'yellow',(600,600)),Button(100,250,'yellow',(900,600)),
    #           Image('project\\images\\back.png',(1000,700))]
    buttons = [Button(100,250,'yellow',(300,200)),Button(100,250,'yellow',(600,200)),Button(100,250,'yellow',(900,200)),
               Button(100,250,'yellow',(300,400)),Button(100,250,'yellow',(600,400)),Button(100,250,'yellow',(900,400)),
               Button(100,250,'yellow',(300,600)),Button(100,250,'yellow',(600,600)),Button(100,250,'yellow',(900,600)),
               Image('project/images/back.png',(1000,700))]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #update surfaces
        screen.blit(buttons[0].surface, buttons[0].rect)

        #check for mouse collisions and mouse presses
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface, buttons[i].rect)
            if buttons[i].rect.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        case 0:
                            print('options')
                        case 1:
                            print('modules')
                        case 9:
                            mainMenu()

        pygame.display.update()
        clock.tick(60)

mainMenu()