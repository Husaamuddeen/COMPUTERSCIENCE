import pygame
import operator
from sys import exit
import time

class InputBox:
    def __init__(self, _centre,_contents):
        self.centre = _centre
        self.contents = _contents
        self.interpretedContents = 0
        self.text = font.render(self.contents,False,'white')
        self.selected = False
        self.locked = False
        self.timer = 0
        self.full = False
        self.height = 0
        self.width = 0
        self.surface = pygame.image.load('project\images\inputBox.png')
        self.rect = self.surface.get_rect(center = self.centre)

    #method to add a character to the user input
    def add(self,_character):
        if not self.locked and not self.full:
            self.height, self.width = font.size(self.contents+ _character)
            if self.height < 150:
                self.contents = self.contents + _character
                self.text = font.render(self.contents,False,'white')
            else:
                self.full = True

    #method to delete the last character from the input box
    def delete(self):
        if not self.locked:
            self.full = False
            self.surface.fill('black')
            screen.blit(self.surface,self.rect)
            self.surface = pygame.image.load('project\images\inputBox.png')
            self.contents = self.contents[:len(self.contents)-1]
            self.text = font.render(self.contents,False,'white')

    def calculate(self):
        first = True
        num1 = '0'
        operator = ''
        num2 = '0'
        for i in range(len(self.contents)):
            if self.contents[i] in ['0','1','2','3','4','5','6','7','8','9']:
                if first:
                    num1 = num1 + self.contents[i]
                else:
                    num2 = num2 + self.contents[i]
            elif self.contents[i] in operators:
                operator = self.contents[i]
                first = False
        if (not int(num2) == 0 and not num2 == '') and (not int(num1) == 0 and not num1 == ''):
            self.interpretedContents = operators[operator](int(num1),int(num2))
            self.contents = str(round(self.interpretedContents,4))
            self.surface.fill('black')
            screen.blit(self.surface,self.rect)
            self.surface = pygame.image.load('project\images\inputBox.png')
            self.text = font.render(self.contents,False,'white')


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

operators = {'+': operator.add,
             '-': operator.sub,
             '/': operator.truediv,
             '*': operator.mul}



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
                            print('saves')

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
        #check for mouse collisions and mouse presses
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface, buttons[i].rect)
            if buttons[i].rect.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        case 0:
                            triangle()
                        case 1:
                            print('modules')
                        case 9:
                            mainMenu()

        pygame.display.update()
        clock.tick(60)

def triangle():
    screen.fill('black')
    pygame.draw.line(screen,'cyan',(800,0),(800,800))

    buttons= []
    inputBoxes = [InputBox((900,200),'00')]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #check for mouse collisions and mouse presses
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface, buttons[i].rect)
            if buttons[i].rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        case 0:
                            print('options')
                        case 1:
                            modules()
                        case 2:
                            print('saves')
        for i in range(len(inputBoxes)):
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            if inputBoxes[i].selected:
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                else:
                    if not inputBoxes[i].rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            inputBoxes[i].selected = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_0]:
                        inputBoxes[i].add('0')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_1]:
                        inputBoxes[i].add('1')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_2]:
                        inputBoxes[i].add('2')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_3]:
                        inputBoxes[i].add('3')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_4]:
                        inputBoxes[i].add('4')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_5]:
                        inputBoxes[i].add('5')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_6]:
                        inputBoxes[i].add('6')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_7]:
                        inputBoxes[i].add('7')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_8]:
                        inputBoxes[i].add('8')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_9]:
                        inputBoxes[i].add('9')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_PLUS]:
                        inputBoxes[i].add('+')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_MINUS]:
                        inputBoxes[i].add('-')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_ASTERISK]:
                        inputBoxes[i].add('*')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_SLASH]:
                        inputBoxes[i].add('/')
                        inputBoxes[i].locked = True
                    if keys[pygame.K_BACKSPACE]:
                        inputBoxes[i].delete()
                        inputBoxes[i].locked = True
                    if keys[pygame.K_RETURN]:
                        inputBoxes[i].calculate()
                        inputBoxes[i].locked = True


            else:
                if inputBoxes[i].rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        inputBoxes[i].selected = True


        pygame.display.update()
        clock.tick(60)

mainMenu()