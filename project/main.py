import pygame
import operator
from sys import exit
import time
import math

#initialise pygame screen
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('graphs')
clock = pygame.time.Clock()

#set default font
font = pygame.font.Font(None,50)
small_font = pygame.font.Font(None,20)

operators = {'+': operator.add,
             '-': operator.sub,
             '/': operator.truediv,
             '*': operator.mul}


#class for an input box which allows the user to enter numbers and basic arithmetic operations
class InputBox:
    def __init__(self, _centre,_contents):
        #attribute for the coordinates of the centre of the input box
        self.centre = _centre
        #attribute to store the contents of the input box in string/uninterpreted form
        self.contents = _contents
        #attribute to store the interpreted value of the input box
        self.interpretedContents = 0
        #attribute to store the rendered text for pygame
        self.text = font.render(self.contents,False,'white')
        #attribute to store wether or not the input box is currently selected
        self.selected = False
        #attribute to store wether or not the input box is locked due to a recent key press
        self.locked = False
        #attribute to store the time since the last entry into the input box
        self.timer = 0
        #attribute to store wether or not the capacity of the input box has been reached
        self.full = False
        #attributes to store the height and width of the input box
        self.height = 0
        self.width = 0
        #initialising a pygame surface and rectangle for the input box
        self.surface = pygame.image.load('project\images\inputBox.png')
        self.rect = self.surface.get_rect(center = self.centre)

    #method to add a character to the user input
    def add(self,_character):
        #check if the input box is neither locked nor full
        if not self.locked and not self.full:
            #get the height and width of the new requested contents of the input box
            self.height, self.width = font.size(self.contents+ _character)
            #check if the new height of the new contents fit in the input box
            if self.height < 150:
                #if they fit, update the contents and text of the input box
                self.contents = self.contents + _character
                self.text = font.render(self.contents,False,'white')
            else:
                #if they don't fit, set the input box to full
                self.full = True

    #method to delete the last character from the input box
    def delete(self):
        #check that the input box is not locked
        if not self.locked:
            #set the input box to not full
            self.full = False
            #clear the previous contents fo the input box and re-blit the image
            self.surface.fill('black')
            screen.blit(self.surface,self.rect)
            self.surface = pygame.image.load('project\images\inputBox.png')
            #remove the last character form the contents of the input box
            self.contents = self.contents[:len(self.contents)-1]
            self.text = font.render(self.contents,False,'white')

    #method to calculate the value of the contents of the input box after a return key press
    def calculate(self):
        #variable to store wether or not the program is reading the first number in the input box
        first = True
        #variables to store the first number, arithmetic operator and second number in the input
        num1 = '0'
        operator = ''
        num2 = '0'
        negative = False
        if self.contents[0] == '-':
            negative = True
            self.contents = self.contents[1:len(self.contents)]

        #for loop to separate the contents of the input box into the arithmetic prompt
        for i in range(len(self.contents)):
            #if the character is a number, add it to either the first or second number
            if self.contents[i] in ['0','1','2','3','4','5','6','7','8','9']:
                if first:
                    num1 = num1 + self.contents[i]
                else:
                    num2 = num2 + self.contents[i]
            #if the character exists in the operators dictionary, store it as the operator
            elif self.contents[i] in operators:
                operator = self.contents[i]
                first = False
        if first:
            self.interpretedContents = int(num1)
        #once the prompt has been separated, check that the input is actaully an arithmetic prompt consisting of two numbers
        if (not int(num2) == 0 and not num2 == '') and (not int(num1) == 0 and not num1 == ''):
            #perform the arithmetic operation and store to interpretedContents
            self.interpretedContents = operators[operator](int(num1),int(num2))
            if negative:
                self.interpretedContents = (0-self.interpretedContents)
            #update the contents of the input box, clear the box and update the surface and text
            self.contents = str(round(self.interpretedContents,4))
            self.surface.fill('black')
            screen.blit(self.surface,self.rect)
            self.surface = pygame.image.load('project\images\inputBox.png')
            self.text = font.render(self.contents,False,'white')

#class to hold all the data about a triangle: sides, angles, area, perimeter
class Triangle:
    def __init__(self, _a, _b, _c, _A, _B, _C, _area, _perimeter):
        self.a = Line(_a.interpretedContents)
        self.b = Line(_b.interpretedContents)
        self.c = Line(_c.interpretedContents)
        self.A = _A
        self.B = _B
        self.C = _C
        self.area = _area
        self.perimeter = _perimeter

#class for a solid button to initialise a button on the pygame display
class Button:
    def __init__(self, _height, _width, _colour, _centre):
        #attributes for height and width of the button
        self.height = _height
        self.width = _width
        #attribute for the colour of the button
        self.colour = _colour
        #attribute for the coordinates of the centre of the button
        self.centre = _centre
        #initialising a pygame surface and rectangle for the button
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill(self.colour)
        self.rect = self.surface.get_rect(center = self.centre)

#class for an image button which serves the same purpose as a button but displays an image
class Image:
    def __init__(self, _path, _centre):
        #attribute for the coordinates of the centre of the button
        self.centre = _centre
        #initialising a pygame surface and rectangle for the button
        self.surface = pygame.image.load(_path)
        self.rect = self.surface.get_rect(center = self.centre)

#class to store the values of a line in a triangle
class Line:
    def __init__(self,_length):
        self.length = _length
        self.angle = 0
        self.surface = None
        self.position = [100,400]

    def drawLine(self,scale,progress):
        if self.surface == None:
            self.surface = pygame.Surface((1,1))
        self.surface = pygame.Surface((self.length*scale*progress,1))
        self.surface.fill('white')
        screen.blit(self.surface,self.position)
        progress = progress + 0.02
        return progress
    
    def moveLine(self,end,progress):
        self.surface.fill('black')
        screen.blit(self.surface,self.position)
        self.position[0] = self.position[0]+ 0.02*(end[0]-100)
        self.position[1] = self.position[1]+ 0.02*(end[1]-400)
        progress = progress + 0.02
        self.surface.fill('white')
        screen.blit(self.surface,self.position)
        return progress

#class to store the values of a polynomial
class Polynomial:
    def __init__(self, _a, _b, _c, _d, _e):
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.e = _e

#procedure to display the main menu
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

#procedure to display the modules menu
def modules():
    screen.fill('black')
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
                            polynomial()
                        case 9:
                            mainMenu()

        pygame.display.update()
        clock.tick(60)

#function to take inputs for triangles
def triangle():
    screen.fill('black')
    pygame.draw.line(screen,'cyan',(800,0),(800,800))

    buttons= [Button(50,50,'gray',(1100,700))]
    inputBoxes = [InputBox((920,60),'00'),InputBox((920,120),'00'),InputBox((920,180),'00'),InputBox((920,240),'00'),InputBox((920,300),'00'),InputBox((920,360),'00'),InputBox((920,420),'00'),InputBox((920,480),'00')]
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
                            data = [False,False,False,False,False,False,False,False]
                            values = 0
                            for i in range(len(inputBoxes)):
                                if inputBoxes[i].interpretedContents != 0:
                                    data[i] = True
                            for i in range(0,3):
                                if data[i]:
                                    values = values + 1
                            if values == 3:
                                drawTriangle(inputBoxes)
                            elif values == 2:
                                if data[7]:
                                    drawTriangle(inputBoxes)
                                for i in range(0,3):
                                    if not data[i] and data[i+3]:
                                        drawTriangle(inputBoxes)
                                    

        for i in range(len(inputBoxes)):
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            if inputBoxes[i].selected:
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                #check for numerical and arithmetic key entries
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

#function to draw a trianlge to the screen
def drawTriangle(inputBoxes):
    newCanvas = pygame.Surface((798,798))
    newCanvasRect = newCanvas.get_rect(center = (400,400))
    screen.blit(newCanvas,newCanvasRect)
    triangle = Triangle(inputBoxes[0],inputBoxes[1],inputBoxes[2],inputBoxes[3],inputBoxes[4],inputBoxes[5],inputBoxes[6],inputBoxes[7])
    lineNum = 1
    progress = 0
    drawn = False
    positioned = False
    scale = 600/triangle.a.length
    print(f'scale: {scale}')
    while not drawn and not positioned:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        match lineNum:
            case 1:
                if not drawn:
                    print(progress)
                    progress = triangle.a.drawLine(scale,progress)
                    if progress > 1:
                        drawn = True
                        progress = 0
                elif not positioned:
                    print(progress)
                    progress = triangle.a.moveLine([100,600],progress)
                    if progress > 1:
                        positioned = True
                        progress = 0


        pygame.display.update()
        clock.tick(60)

#function to find a missing length (a)
def length(a,b,c,A,B,C):
    #find a using the formula perimeter = a + b + c
    if b != 0 and c != 0 and perimeter != 0:
        a = perimeter-(b+c)
    #find a using the cosine rule (a^=b^+c^-2bccos(A))
    elif b != 0 and c != 0 and A != 0:
        a = math.sqrt(b**2+c**2-2*b*c*math.cos(math.radians(A)))
    #find a using the sine rule (a = b/sin(B)*sin(A))
    elif b != 0 and B != 0 and A != 0:
        a = b/math.sin(math.radians(B))*math.sin(math.radians(A))
    #find a using the sine rule (a = b/sin(B)*sin(A))
    elif c != 0 and C != 0 and A != 0:
        a = c/math.sin(math.radians(C))*math.sin(math.radians(A))
    #find a using the formula for area (area = 0.5absin(C)) rearranged to a = area/(0.5bsin(C))
    elif area != 0 and b != 0 and C != 0:
        a = area/(0.5*b*math.sin(math.radians(C)))
    #find a using the formula for area (area = 0.5acsin(B)) rearranged to a = area/(0.5csin(B))
    elif area != 0 and c != 0 and B != 0:
        a = area/(0.5*c*math.sin(math.radians(B)))
    #find a using my own formula (last resort) (a = a factor of ac(area/0.5sin(B)) which ads to (perimeter - b)
    elif b != 0 and B != 0 and area != 0 and perimeter != 0:
        #ac is a*c found using the formula for area of a triangle
        ac = int(area/(0.5*math.sin(math.radians(B))))
        #list for the factors of ac
        factors = []
        #loop to find all the factors of ac and append to factors
        for i in range (1,ac+1):
            if ac % i == 0:
                factors.append(i)
        #find how many factors there are
        length = len(factors)
        #loop for finding a pair of factors that add to make the perimeter - b
        for i in range(0,length):
            for x in range(0,length):
                if factors[i]+factors[x] == perimeter - b and factors[i]*factors[x] == ac:
                    a = factors[i]
                    c = factors[x]
    #find a using my own formula (last resort) (a = a factor of ab(area/0.5sin(C)) which ads to (perimeter - c)
    elif c != 0 and C != 0 and area != 0 and perimeter != 0:
        #ab is a*b found using the formula for area of a triangle
        ab = int(area/(0.5*math.sin(math.radians(C))))
        #list for the factors of ab
        factors = []
        #loop to find all the factors of ab and append to factors
        for i in range (1,ab+1):
            if ab % i == 0:
                factors.append(i)
        #find how many factors there are
        length = len(factors)
        #loop for finding a pair of factors that add to make the perimeter - c
        for i in range(0,length):
            for x in range(0,length):
                if factors[i]+factors[x] == perimeter - c and factors[i]*factors[x] == ab:
                    a = factors[i]
                    b = factors[x]
    #return the value of length a
    return a

#function to take inputs for a polynomial
def polynomial():
    screen.fill('black')
    pygame.draw.line(screen,'cyan',(800,0),(800,800))
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))
    x = font.render('x',False,'white')
    powers = [small_font.render('4',False,'white'),small_font.render('3',False,'white'),small_font.render('2',False,'white')]
    screen.blit(x,(1000,40))
    screen.blit(x,(1000,100))
    screen.blit(x,(1000,160))
    screen.blit(x,(1000,220))
    screen.blit(powers[0],(1018,39))
    screen.blit(powers[1],(1018,99))
    screen.blit(powers[2],(1018,159))

    buttons= [Button(50,50,'gray',(1100,700))]
    inputBoxes = [InputBox((920,60),'00'),InputBox((920,120),'00'),InputBox((920,180),'00'),InputBox((920,240),'00'),InputBox((920,300),'00')]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface,buttons[i].rect)
            if buttons[i].rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    print('plot')
                    plot(inputBoxes)

        for i in range(len(inputBoxes)):
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            if inputBoxes[i].selected:
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                #check for numerical and arithmetic key entries
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

#function to render a polynomial graph
def plot(inputBoxes):
    newCanvas = pygame.Surface((798,798))
    newCanvasRect = newCanvas.get_rect(center = (400,400))
    screen.blit(newCanvas,newCanvasRect)
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))

    polynomial = Polynomial(inputBoxes[0].interpretedContents,inputBoxes[1].interpretedContents,inputBoxes[2].interpretedContents,inputBoxes[3].interpretedContents,inputBoxes[4].interpretedContents)
    print(polynomial.a,polynomial.b,polynomial.c,polynomial.d,polynomial.e)
    plotted = False
    while not plotted:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        previous = polynomial.a*(-401)**4 + polynomial.b*(-401)**3 + polynomial.c*(-401)**2 + polynomial.d*(-401) + polynomial.e
        for x in range(-400,400):
            y = polynomial.a*(x**4) + polynomial.b*(x**3) + polynomial.c*(x**2) + polynomial.d*x + polynomial.e
            print(x,previous,y)
            print('')
            pygame.draw.line(screen,'pink',(x-1+400,400-previous),(x+400,400-y))
            previous = y
        plotted = True

        pygame.display.update()
        clock.tick(60)
    print(polynomial.a,polynomial.b,polynomial.c,polynomial.d,polynomial.e)

mainMenu()