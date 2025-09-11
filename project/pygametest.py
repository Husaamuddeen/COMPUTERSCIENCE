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
    

#constructTriangle()


button = pygame.Surface(((100,100)))
button.fill('Blue')
buttonrec = button.get_rect(center = (50,50))
print(buttonrec)
#main animation loop
count = 0
def mainMenu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #update surfaces
    count += 1
    if count < 100:
        screen.blit(button,buttonrec)
    else:
        screen.fill('black')
        print('gone')
    #check for mouse collisions and mouse presses
    mouse_pos = pygame.mouse.get_pos()
    if buttonrec.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed()[0]:
            print('maths')

    pygame.display.update()
    clock.tick(60)