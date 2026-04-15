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
    def __init__(self, _center,_contents):
        #attribute for the coordinates of the center of the input box
        self.center = _center
        #attribute to store the contents of the input box in string/uninterpreted form
        self.contents = _contents
        #attribute to store the interpreted value of the input box
        self.interpretedContents = 0
        #attribute to store the rendered text for pygame
        self.text = font.render(self.contents,False,'white')
        #attribute to store the image to be rendered
        self.image = 'project\images\inputBox.png'
        #attribute to store wether or not the input box is currently selected
        self.selected = False
        #attribute to store wether or not the input box is locked due to a recent key press
        self.locked = False
        #attribute to store the time since the last entry into the input box
        self.timer = 0
        #attribute to store wether or not the capacity of the input box has been reached
        self.full = False
        #attributes to store the height and width of the contents of input box
        self.height = 0
        self.width = 0
        #attribute to store the maximum height of the input box
        self.maxHeight = 150
        #initialising a pygame surface and rectangle for the input box
        self.surface = pygame.image.load(self.image)
        self.rect = self.surface.get_rect(center = self.center)

    #method to add a character to the user input
    def add(self,_character):
        #check if the input box is neither locked nor full
        if not self.locked and not self.full:
            #get the height and width of the new requested contents of the input box
            self.height, self.width = font.size(self.contents+ _character)
            #check if the new height of the new contents fit in the input box
            if self.height < self.maxHeight:
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
            self.surface = pygame.image.load(self.image)
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
            self.surface = pygame.image.load(self.image)
            self.text = font.render(self.contents,False,'white')

#subclass for a square input box without borders
class SquareInputBox(InputBox):
    def __init__(self,_center,_contents):
        #inherits the functions of the inputBox class
        super().__init__(_center,_contents)
        #override the surface and rectangle created by the superclass initialisation
        self.image = 'project\images\squareInputBox.png'
        self.surface = pygame.image.load(self.image)
        self.rect = self.surface.get_rect(center = self.center)
        screen.blit(self.surface,self.rect)
        #change the attribute relating to the size capacity for text
        self.maxHeight = 70

#class to hold all the data about a triangle: sides, angles, area, perimeter
class Triangle:
    def __init__(self, _a, _b, _c, _A, _B, _C, _area, _perimeter):
        #atributes to store sides a,b and c of the triangle
        self.a = Line(_a.interpretedContents)
        self.b = Line(_b.interpretedContents)
        self.c = Line(_c.interpretedContents)
        #attributes to store angles A,B and C of the triangle
        self.A = _A
        self.B = _B
        self.C = _C
        #attributes to store the area and perimeter of the triangle
        self.area = _area
        self.perimeter = _perimeter

#class for a solid button to initialise a button on the pygame display
class Button:
    def __init__(self, _height, _width, _colour, _center):
        #attributes for height and width of the button
        self.height = _height
        self.width = _width
        #attribute for the colour of the button
        self.colour = _colour
        #attribute for the coordinates of the center of the button
        self.center = _center
        #initialising a pygame surface and rectangle for the button
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill(self.colour)
        self.rect = self.surface.get_rect(center = self.center)

#class for an image button which serves the same purpose as a button but displays an image
class Image:
    def __init__(self, _path, _center):
        #attribute for the coordinates of the center of the button
        self.center = _center
        #initialising a pygame surface and rectangle for the button
        self.surface = pygame.image.load(_path)
        self.rect = self.surface.get_rect(center = self.center)

#class to store the values of a line in a triangle
class Line:
    def __init__(self,_length):
        #attributes to store the length and angle of the line relative to the positive x axis
        self.length = _length
        self.angle = 0
        self.surface = None
        self.position = [100,400]

    #method to progressively draw the line by repeatedly blitting a larger fraction fo the line each tick
    def drawLine(self,scale,progress):
        if self.surface == None:
            self.surface = pygame.Surface((1,1))
        #assign the fraction of the line depending on the progress
        self.surface = pygame.Surface((self.length*scale*progress,1))
        self.surface.fill('white')
        screen.blit(self.surface,self.position)
        progress = progress + 0.02
        return progress
    
    #method to move the line to its correct position
    def moveLine(self,end,progress):
        #remove the old render
        self.surface.fill('black')
        #blit blank
        screen.blit(self.surface,self.position)
        #update position
        self.position[0] = self.position[0]+ 0.02*(end[0]-100)
        self.position[1] = self.position[1]+ 0.02*(end[1]-400)
        #update progress
        progress = progress + 0.02
        #blit
        self.surface.fill('white')
        screen.blit(self.surface,self.position)
        return progress

#class to store the values of a polynomial
class Polynomial:
    def __init__(self, _a, _b, _c, _d, _e):
        #attributes to store coefficients a,b,c,d and e of x^4, x^3, x^2 x and x^0 respectively
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.e = _e

#class to store the properties of complex numbers
class ComplexNumber:
    def __init__(self):
        #attributes to store the coefficients a and b of the real and imaginary components of the complex number respectively
        self.a = 0
        self.b = 0
        self.mod = 0
        self.arg = 0

    #setter for the real coefficient
    def set_a(self,_a):
        self.a = _a

    #setter for the imaginary coefficient
    def set_b(self,_b):
        self.b = _b

    #setter for the modulus
    def set_mod(self,_mod):
        self.mod = _mod

    #setter for the argument
    def set_arg(self,_arg):
        self.arg = _arg

#class to store the elements of a matrix
class Matrix:
    def __init__(self,_m,_n,_a,_b,_c,_d,_e,_f,_g,_h,_i):
        #attributes to store teh number of columns and rows
        self.m = _m
        self.n = _n

    #setter for element a
    def setA(self,_a):
        self.a = _a

    #setter for element b
    def setB(self,_b):
        self.b = _b

    #setter for element c
    def setC(self,_c):
        self.c = _c

    #setter for element d
    def setD(self,_d):
        self.d = _d

    #setter for element e
    def setE(self,_e):
        self.e = _e

    #setter for element f
    def setF(self,_f):
        self.f = _f

    #setter for element g
    def setG(self,_g):
        self.g = _g

    #setter for element h
    def setH(self,_h):
        self.h = _h

    #setter for element i
    def setI(self,_i):
        self.i = _i

#class to store the equation of a vector
class Vector:
    def __init__(self,_a,_b,_c,_d,_colour):
        #attributes to store elements a and b which correspond to the x and y values of the position vector
        self.a = _a
        self.b = _b
        #attributes to store elements c and d which correspond to the x and y values of the direction vector
        self.c = _c
        self.d = _d
        self.colour = _colour

#procedure to display the main menu
def mainMenu():
    screen.fill('black')
    buttons = [Image('project/images/options.png',(500,400)),Image('project/images/modules.png',(600,400)),Image('project/images/saves.png',(700,400))]
    #buttons = [Image('project\\images\options.png',(500,400)),Image('project\\images\modules.png',(600,400)),Image('project\\images\saves.png',(700,400))]

    while True:
        #check for the user quitting the program
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
                    #match case to check which button in the buttons list the user has pressed
                    match i:
                        case 0:
                            settings()
                        case 1:
                            modules()
                        case 2:
                            print('saves')

        #update the screen
        pygame.display.update()
        clock.tick(60)

#procedure to display the modules menu
def modules():
    #fill the screen black to remove the previous screen
    screen.fill('black')
    #matrix of buttons each corresponding to one module, and the last button directs the user back to the main menu
    buttons = [Image('project/images/triangle.png',(300,200)),Image('project/images/polynomial.png',(600,200)),Image('project/images/argand.png',(900,200)),
               Image('project/images/matrix.png',(300,400)),Image('project/images/vector.png',(600,400)),Image('project/images/linear.png',(900,400)),
               Image('project/images/unit.png',(300,600)),Image('project/images/blank.png',(600,600)),Image('project/images/blank.png',(900,600)),
               Image('project/images/back.png',(1000,700))]
    
    #buffer time to prevent the user from instantly clicking on the module which lies in the same area as the button for modules from the main menu
    pygame.display.update()
    time.sleep(0.2)

    while True:
        #check for the user quitting the program
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
                    #match case to allow each button to direct the user to a different maths module
                    match i:
                        #if user clicks triangle module
                        case 0:
                            triangle()
                        #if user clicks polynomial module
                        case 1:
                            polynomial()
                        #if user clicks argand module
                        case 2:
                            argand()
                        #if user clicks matrix module
                        case 3:
                            matrix()
                        #if user clicks vectors module
                        case 4:
                            vectors()
                        #if user clicks back
                        case 9:
                            mainMenu()

        pygame.display.update()
        clock.tick(60)

#procedure to display the settings menu
def settings():
    #fill the screen black to remove the previous screen
    screen.fill('black')
    #matrix of buttons each corresponding to one module, and the last button directs the user back to the main menu
    buttons = [Image('project/images/back.png',(1000,700))]
    
    x = font.render('No settings available',False,'white')
    screen.blit(x,(450,100))

    #buffer time to prevent the user from instantly clicking on the module which lies in the same area as the button for modules from the main menu
    pygame.display.update()
    time.sleep(0.2)

    while True:
        #check for the user quitting the program
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
                    #match case to allow each button to direct the user to a different maths module
                    match i:
                        case 0:
                            mainMenu()

        pygame.display.update()
        clock.tick(60)

#function to take inputs for triangles
def triangle():
    #fill the screen black to remove the previous screen
    screen.fill('black')
    pygame.draw.line(screen,'cyan',(800,0),(800,800))

    #a button to start the calculation and a button to go back to the modules page
    buttons= [Button(50,50,'gray',(875,750)),Image('project/images/back.png',(1100,750))]
    #input boxes to take inputs for each of the attributes of the triangle
    inputBoxes = [InputBox((920,60),'00'),InputBox((920,120),'00'),InputBox((920,180),'00'),InputBox((920,240),'00'),InputBox((920,300),'00'),InputBox((920,360),'00'),InputBox((920,420),'00'),InputBox((920,480),'00')]
    while True:
        #check for the user quitting the program
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
                        #check for the user clicking to render the triangle
                        case 0:
                            #list to track which data has been entered by the user
                            data = [False,False,False,False,False,False,False,False]
                            values = 0
                            #update the data list according to user inputs
                            for i in range(len(inputBoxes)):
                                if inputBoxes[i].interpretedContents != 0:
                                    data[i] = True
                            #count the number of data items the user has inputted
                            for i in range(0,3):
                                if data[i]:
                                    values = values + 1
                            #decide wether or not the algorithm can be carried out based on the number of data items
                            if values == 3:
                                drawTriangle(inputBoxes)
                            #check for specific scenarios
                            elif values == 2:
                                if data[7]:
                                    drawTriangle(inputBoxes)
                                for i in range(0,3):
                                    if not data[i] and data[i+3]:
                                        drawTriangle(inputBoxes)
                        #check for the user pressing the back button
                        case 1:
                            modules()
                                    
        #check for user inputs in the input boxes
        for i in range(len(inputBoxes)):
            #update the input boxes
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            #check if the input box is already selected
            if inputBoxes[i].selected:
                #check in the input box is currently locked
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    #if the input box is locked, update its timer
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                #check for numerical and arithmetic key entries
                else:
                    #check for the user clicking of the input box
                    if not inputBoxes[i].rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            inputBoxes[i].selected = False
                    #store the user inputs in the keys list
                    keys = pygame.key.get_pressed()
                    #if the user enters 0
                    if keys[pygame.K_0]:
                        inputBoxes[i].add('0')
                        inputBoxes[i].locked = True
                    #if the user enters 1
                    if keys[pygame.K_1]:
                        inputBoxes[i].add('1')
                        inputBoxes[i].locked = True
                    #if the user enters 2
                    if keys[pygame.K_2]:
                        inputBoxes[i].add('2')
                        inputBoxes[i].locked = True
                    #if the user enters 3
                    if keys[pygame.K_3]:
                        inputBoxes[i].add('3')
                        inputBoxes[i].locked = True
                    #if the user enters 4
                    if keys[pygame.K_4]:
                        inputBoxes[i].add('4')
                        inputBoxes[i].locked = True
                    #if the user enters 5
                    if keys[pygame.K_5]:
                        inputBoxes[i].add('5')
                        inputBoxes[i].locked = True
                    #if the user enters 6
                    if keys[pygame.K_6]:
                        inputBoxes[i].add('6')
                        inputBoxes[i].locked = True
                    #if the user enters 7
                    if keys[pygame.K_7]:
                        inputBoxes[i].add('7')
                        inputBoxes[i].locked = True
                    #if the user enters 8
                    if keys[pygame.K_8]:
                        inputBoxes[i].add('8')
                        inputBoxes[i].locked = True
                    #if the user enters 9
                    if keys[pygame.K_9]:
                        inputBoxes[i].add('9')
                        inputBoxes[i].locked = True
                    #if the user enters +
                    if keys[pygame.K_PLUS]:
                        inputBoxes[i].add('+')
                        inputBoxes[i].locked = True
                    #if the user enters -
                    if keys[pygame.K_MINUS]:
                        inputBoxes[i].add('-')
                        inputBoxes[i].locked = True
                    #if the user enters *
                    if keys[pygame.K_ASTERISK]:
                        inputBoxes[i].add('*')
                        inputBoxes[i].locked = True
                    #if the user enters /
                    if keys[pygame.K_SLASH]:
                        inputBoxes[i].add('/')
                        inputBoxes[i].locked = True
                    #if the user enters backspace key
                    if keys[pygame.K_BACKSPACE]:
                        inputBoxes[i].delete()
                        inputBoxes[i].locked = True
                    #if the user enters return key
                    if keys[pygame.K_RETURN]:
                        inputBoxes[i].calculate()
                        inputBoxes[i].locked = True
            #check if the user is clicking on to the input box
            else:
                if inputBoxes[i].rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        inputBoxes[i].selected = True

        pygame.display.update()
        clock.tick(60)

#function to draw a trianlge to the screen
def drawTriangle(inputBoxes):
    #blit a new object to clear the screen of previous renders
    newCanvas = pygame.Surface((798,798))
    newCanvasRect = newCanvas.get_rect(center = (400,400))
    screen.blit(newCanvas,newCanvasRect)
    #instantiate triangle object with the inputted values passed in as arguments
    triangle = Triangle(inputBoxes[0],inputBoxes[1],inputBoxes[2],inputBoxes[3],inputBoxes[4],inputBoxes[5],inputBoxes[6],inputBoxes[7])
    #variable to track the number of lines rendered
    lineNum = 1
    #variable to track the progress of the rendering of a single line
    progress = 0
    #variables to track if a line is finishd
    drawn = False
    positioned = False
    #variable to store the scale that the triangle will be timesed by to fill the screen
    scale = 1
    if triangle.a.length != 0:
        scale = 600/triangle.a.length
    print(f'scale: {scale}')
    #loop to animately draw the line
    while not drawn and not positioned:
        #check for the user quitting the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        match lineNum:
            #check which line is being rendered
            case 1:
                if not drawn:
                    print(progress)
                    #use the triangle method draw line to draw the line at the level of progress denoted
                    progress = triangle.a.drawLine(scale,progress)
                    if progress > 1:
                        drawn = True
                        progress = 0
                elif not positioned:
                    #use the triangle method move line to move the line at the level of progress denoted
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
    #fill the screen black to clear previous renders
    screen.fill('black')
    #draw graph axes
    pygame.draw.line(screen,'cyan',(800,0),(800,800))
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))
    x = font.render('x',False,'white')
    #add text to show polynomial terms
    powers = [small_font.render('4',False,'white'),small_font.render('3',False,'white'),small_font.render('2',False,'white')]
    screen.blit(x,(1000,40))
    screen.blit(x,(1000,100))
    screen.blit(x,(1000,160))
    screen.blit(x,(1000,220))
    #blit terms
    screen.blit(powers[0],(1018,39))
    screen.blit(powers[1],(1018,99))
    screen.blit(powers[2],(1018,159))

    #lists to store the button and inputbox objects
    buttons= [Button(50,50,'gray',(875,750)),Image('project/images/back.png',(1100,750))]
    inputBoxes = [InputBox((920,60),'00'),InputBox((920,120),'00'),InputBox((920,180),'00'),InputBox((920,240),'00'),InputBox((920,300),'00')]
    while True:
        #check for the user quitting the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #check the mouse position to check against buttons
        mouse_pos = pygame.mouse.get_pos()
        #update buttons and check if they are being pressed
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface,buttons[i].rect)
            if buttons[i].rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        #check if the user pressed render
                        case 0:
                            plot(inputBoxes)
                        #check if the user pressed back
                        case 1:
                            modules()

        #check for user inputs in the input boxes
        for i in range(len(inputBoxes)):
            #update the input boxes
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            #check if the input box is already selected
            if inputBoxes[i].selected:
                #check in the input box is currently locked
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    #if the input box is locked, update its timer
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                #check for numerical and arithmetic key entries
                else:
                    #check for the user clicking of the input box
                    if not inputBoxes[i].rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            inputBoxes[i].selected = False
                    #store the user inputs in the keys list
                    keys = pygame.key.get_pressed()
                    #if the user enters 0
                    if keys[pygame.K_0]:
                        inputBoxes[i].add('0')
                        inputBoxes[i].locked = True
                    #if the user enters 1
                    if keys[pygame.K_1]:
                        inputBoxes[i].add('1')
                        inputBoxes[i].locked = True
                    #if the user enters 2
                    if keys[pygame.K_2]:
                        inputBoxes[i].add('2')
                        inputBoxes[i].locked = True
                    #if the user enters 3
                    if keys[pygame.K_3]:
                        inputBoxes[i].add('3')
                        inputBoxes[i].locked = True
                    #if the user enters 4
                    if keys[pygame.K_4]:
                        inputBoxes[i].add('4')
                        inputBoxes[i].locked = True
                    #if the user enters 5
                    if keys[pygame.K_5]:
                        inputBoxes[i].add('5')
                        inputBoxes[i].locked = True
                    #if the user enters 6
                    if keys[pygame.K_6]:
                        inputBoxes[i].add('6')
                        inputBoxes[i].locked = True
                    #if the user enters 7
                    if keys[pygame.K_7]:
                        inputBoxes[i].add('7')
                        inputBoxes[i].locked = True
                    #if the user enters 8
                    if keys[pygame.K_8]:
                        inputBoxes[i].add('8')
                        inputBoxes[i].locked = True
                    #if the user enters 9
                    if keys[pygame.K_9]:
                        inputBoxes[i].add('9')
                        inputBoxes[i].locked = True
                    #if the user enters +
                    if keys[pygame.K_PLUS]:
                        inputBoxes[i].add('+')
                        inputBoxes[i].locked = True
                    #if the user enters -
                    if keys[pygame.K_MINUS]:
                        inputBoxes[i].add('-')
                        inputBoxes[i].locked = True
                    #if the user enters *
                    if keys[pygame.K_ASTERISK]:
                        inputBoxes[i].add('*')
                        inputBoxes[i].locked = True
                    #if the user enters /
                    if keys[pygame.K_SLASH]:
                        inputBoxes[i].add('/')
                        inputBoxes[i].locked = True
                    #if the user enters backspace key
                    if keys[pygame.K_BACKSPACE]:
                        inputBoxes[i].delete()
                        inputBoxes[i].locked = True
                    #if the user enters return key
                    if keys[pygame.K_RETURN]:
                        inputBoxes[i].calculate()
                        inputBoxes[i].locked = True
            #check if the user is clicking on to the input box
            else:
                if inputBoxes[i].rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        inputBoxes[i].selected = True

        pygame.display.update()
        clock.tick(60)

#function to render a polynomial graph
def plot(inputBoxes):
    #fill the graph black to remove previous renders
    newCanvas = pygame.Surface((798,798))
    newCanvasRect = newCanvas.get_rect(center = (400,400))
    screen.blit(newCanvas,newCanvasRect)
    #redraw the axes
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))

    #instantiate polynomial object using inputs passed in
    polynomial = Polynomial(inputBoxes[0].interpretedContents,inputBoxes[1].interpretedContents,inputBoxes[2].interpretedContents,inputBoxes[3].interpretedContents,inputBoxes[4].interpretedContents)
    #check if the polynomial is degree 4
    if polynomial.a == 0:
        #check if the polynomial is degree 3
        if polynomial.b == 0:
            #check if the polynomial is degree 2
            if polynomial.c == 0:
                #check if the polynomial is degree 1
                if polynomial.d == 0:
                    #no solutions for x
                    x1 = False
                    x2 = False
                    x3 = False
                    x4 = False
                else:
                    #use x = -y/m
                    x1 = -(polynomial.e)/(polynomial.d)
                    x2 = False
                    x3 = False
                    x4 = False
            else:
                #use quadratic formula to find 2 solutions for x
                x1 = (-(polynomial.d)+math.sqrt((polynomial.d)**2-4*polynomial.c*polynomial.e))/(2*polynomial.c)
                x2 = (-(polynomial.d)-math.sqrt((polynomial.d)**2-4*polynomial.c*polynomial.e))/(2*polynomial.c)
                x3 = False
                x4 = False
    #y intercept is always e coefficient
    y1 = polynomial.e

    #variable to track wether or not the render is finished
    plotted = False
    while not plotted:
        #check for the user quitting the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        #variable to store the value of y for the previous value of x
        previous = polynomial.a*(-401)**4 + polynomial.b*(-401)**3 + polynomial.c*(-401)**2 + polynomial.d*(-401) + polynomial.e
        #for loop which draws a straight line between the previous and current point on the graph
        for x in range(-400,400):
            time.sleep(0.001)
            pygame.display.update()
            #calculate new value for y
            y = polynomial.a*(x**4) + polynomial.b*(x**3) + polynomial.c*(x**2) + polynomial.d*x + polynomial.e
            #range check to prevent errors by rendering off screen
            if (400-previous) <= 800 and (400-y) <= 800 and (400-previous) >= 0 and (400-y) >= 0:
                pygame.draw.line(screen,'pink',((x-1+400),(400-previous)),((x+400),(400-y)))
            #update the previous variable
            previous = y
        #update plotted variable
        plotted = True
        #print intercepts if existant
        if x1 != False:
            print('('+str(x1)+',0)')
        if x2 != False:
            print('('+str(x2)+',0)')
        print('(0,'+str(y1)+')')
        pygame.display.update()
        clock.tick(60)

#function to plot argand diagrams
def argand():
    #fill the screen black to remove previous images
    screen.fill('black')
    #draw graph axes
    pygame.draw.line(screen,'cyan',(800,0),(800,800))
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))
    #render complex number shell
    screen.blit(font.render('+',False,'white'),(1000,40))
    screen.blit(font.render(' i',False,'white'),(1000,100))
    screen.blit(font.render('= modulus',False,'white'),(1000,160))
    screen.blit(font.render('= argument',False,'white'),(1000,220))

    #lists to store the button and input box objects
    buttons= [Button(50,50,'gray',(875,750)),Image('project/images/back.png',(1100,750))]
    inputBoxes = [InputBox((920,60),'00'),InputBox((920,120),'00'),InputBox((920,180),'00'),InputBox((920,240),'00')]
    while True:
        #check for the user quitting the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #take the mouse position to check against the buttons
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface,buttons[i].rect)
            if buttons[i].rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        #check if the user is clicking render
                        case 0:
                            plotI(inputBoxes)
                        #check if the user is clicking back
                        case 1:
                            modules()

        #check for user inputs in the input boxes
        for i in range(len(inputBoxes)):
            #update the input boxes
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            #check if the input box is already selected
            if inputBoxes[i].selected:
                #check in the input box is currently locked
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    #if the input box is locked, update its timer
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                #check for numerical and arithmetic key entries
                else:
                    #check for the user clicking of the input box
                    if not inputBoxes[i].rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            inputBoxes[i].selected = False
                    #store the user inputs in the keys list
                    keys = pygame.key.get_pressed()
                    #if the user enters 0
                    if keys[pygame.K_0]:
                        inputBoxes[i].add('0')
                        inputBoxes[i].locked = True
                    #if the user enters 1
                    if keys[pygame.K_1]:
                        inputBoxes[i].add('1')
                        inputBoxes[i].locked = True
                    #if the user enters 2
                    if keys[pygame.K_2]:
                        inputBoxes[i].add('2')
                        inputBoxes[i].locked = True
                    #if the user enters 3
                    if keys[pygame.K_3]:
                        inputBoxes[i].add('3')
                        inputBoxes[i].locked = True
                    #if the user enters 4
                    if keys[pygame.K_4]:
                        inputBoxes[i].add('4')
                        inputBoxes[i].locked = True
                    #if the user enters 5
                    if keys[pygame.K_5]:
                        inputBoxes[i].add('5')
                        inputBoxes[i].locked = True
                    #if the user enters 6
                    if keys[pygame.K_6]:
                        inputBoxes[i].add('6')
                        inputBoxes[i].locked = True
                    #if the user enters 7
                    if keys[pygame.K_7]:
                        inputBoxes[i].add('7')
                        inputBoxes[i].locked = True
                    #if the user enters 8
                    if keys[pygame.K_8]:
                        inputBoxes[i].add('8')
                        inputBoxes[i].locked = True
                    #if the user enters 9
                    if keys[pygame.K_9]:
                        inputBoxes[i].add('9')
                        inputBoxes[i].locked = True
                    #if the user enters +
                    if keys[pygame.K_PLUS]:
                        inputBoxes[i].add('+')
                        inputBoxes[i].locked = True
                    #if the user enters -
                    if keys[pygame.K_MINUS]:
                        inputBoxes[i].add('-')
                        inputBoxes[i].locked = True
                    #if the user enters *
                    if keys[pygame.K_ASTERISK]:
                        inputBoxes[i].add('*')
                        inputBoxes[i].locked = True
                    #if the user enters /
                    if keys[pygame.K_SLASH]:
                        inputBoxes[i].add('/')
                        inputBoxes[i].locked = True
                    #if the user enters backspace key
                    if keys[pygame.K_BACKSPACE]:
                        inputBoxes[i].delete()
                        inputBoxes[i].locked = True
                    #if the user enters return key
                    if keys[pygame.K_RETURN]:
                        inputBoxes[i].calculate()
                        inputBoxes[i].locked = True
            #check if the user is clicking on to the input box
            else:
                if inputBoxes[i].rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        inputBoxes[i].selected = True

        pygame.display.update()
        clock.tick(60)

#function to plot complex numbers
def plotI(inputBoxes):
    #blit the screen black to remove previous renders
    newCanvas = pygame.Surface((798,798))
    newCanvasRect = newCanvas.get_rect(center = (400,400))
    screen.blit(newCanvas,newCanvasRect)
    #draw the graph axes again
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))

    #instantiate the complex number object and set its attributes (I used setters instead of assigning on instatiation as it is unknown which values the user will enter)
    complexNumber = ComplexNumber()
    #set a
    complexNumber.set_a(inputBoxes[0].interpretedContents)
    #set b
    complexNumber.set_b(inputBoxes[1].interpretedContents)
    #set mod
    complexNumber.set_mod(inputBoxes[2].interpretedContents)
    #set arg
    complexNumber.set_arg(inputBoxes[3].interpretedContents)

    #algorithm to calculate the missing attributes of the complex number object
    #check if the user entered the full cartesian form
    if complexNumber.a != 0 and complexNumber.b != 0:
        if complexNumber.a > 0:
            #if the number is in the first quadrant
            if complexNumber.b > 0:
                complexNumber.arg = math.atan(complexNumber.b/complexNumber.a)
            #if the number is in the fourth quadrant
            else:
                complexNumber.arg = math.atan(complexNumber.b/complexNumber.a)
        else:
            #if the number is in the second quadrant
            if complexNumber.b > 0:
                complexNumber.arg = 0 - math.atan(complexNumber.b/complexNumber.a)
            #if the number is in the third quadrant
            else:
                complexNumber.arg = math.atan(complexNumber.b/complexNumber.a) - math.pi
    #if the user entered half cartesian and half modarg
    elif complexNumber.a != 0 and complexNumber.arg != 0:
        if complexNumber.arg > 0:
            #if the number is in the second quadrant
            if complexNumber.arg > (math.pi/2):
                complexNumber.b = (complexNumber.a/math.tan(complexNumber.arg-math.pi/2))
            #if the number is in the first quadrant
            else:
                complexNumber.b = (complexNumber.a*math.tan(complexNumber.arg))
        else:
            #if the number is in the third quadrant
            if complexNumber.arg < (0-math.pi/2):
                complexNumber.b = (complexNumber.a/math.tan(0-complexNumber.arg-math.pi/2))
            #if the number is in the fourth quadrant
            else:
                complexNumber.b = (complexNumber.a*math.tan(0-complexNumber.arg))
    #if the user entered half cartesian and half modarg
    elif complexNumber.b != 0 and complexNumber.arg != 0:
        if complexNumber.arg > 0:
            #if the number is in the second quadrant
            if complexNumber.arg > (math.pi/2):
                complexNumber.a = (complexNumber.b*math.tan(complexNumber.arg-math.pi/2))
            #if the number is in the first quadrant
            else:
                complexNumber.a = (complexNumber.b/math.tan(complexNumber.arg))
        else:
            #if the number is in the third quadrant
            if complexNumber.arg < (0-math.pi/2):
                complexNumber.a = (complexNumber.b*math.tan(0-complexNumber.arg-math.pi/2))
            #if the number is in the fourth quadrant
            else:
                complexNumber.a = (complexNumber.b/math.tan(0-complexNumber.arg))
    #if the user entered modarg form
    elif complexNumber.mod != 0 and complexNumber.arg != 0:
        if complexNumber.arg > 0:
            #if the number is in the second quadrant
            if complexNumber.arg > (math.pi/2):
                complexNumber.a = (complexNumber.mod*math.sin(complexNumber.arg-math.pi/2))
            #if the number is in the first quadrant
            else:
                complexNumber.a = (complexNumber.mod*math.cos(complexNumber.arg))
        else:
            #if the number is in the third quadrant
            if complexNumber.arg < (0-math.pi/2):
                complexNumber.a = (complexNumber.mod*math.sin(0-complexNumber.arg-math.pi/2))
            #if the number is in the fourth quadrant
            else:
                complexNumber.a = (complexNumber.mod*math.cos(0-complexNumber.arg))

        #calculate b with pythagoras
        complexNumber.b = math.sqrt(complexNumber.mod**2-complexNumber.a**2)
    #calculate mod with pythagoras
    complexNumber.mod = math.sqrt(complexNumber.a**2+complexNumber.b**2)

    attributes = [complexNumber.a,complexNumber.b,complexNumber.mod,complexNumber.arg]
    #refresh input boxes with complete values
    for i in range(0,4):
        inputBoxes[i].interpretedContents = attributes[i]
        inputBoxes[i].contents = str(round(attributes[i],4))
        inputBoxes[i].surface.fill('black')
        screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
        inputBoxes[i].surface = pygame.image.load('project\images\inputBox.png')
        inputBoxes[i].text = font.render(inputBoxes[i].contents,False,'white')

    #draw the modules from the origin to the number
    pygame.draw.line(screen,'white',(400,400),(400+complexNumber.a,400-complexNumber.b))
    #draw the angle
    angleRect = pygame.Rect(370,370,60,60)
    pygame.draw.arc(screen,'white',angleRect,0,complexNumber.arg)
    pygame.display.update()
    clock.tick(60)

#function to take inputs for a matrix
def matrix():
    screen.fill('black')
    #split the screen into matrix and options
    pygame.draw.line(screen,'cyan',(800,0),(800,800))

    #matrix shell
    pygame.draw.line(screen,'white',(200,240),(200,560))
    pygame.draw.line(screen,'white',(230,200),(200,240))
    pygame.draw.line(screen,'white',(200,560),(230,600))

    pygame.draw.line(screen,'white',(600,240),(600,560))
    pygame.draw.line(screen,'white',(570,200),(600,240))
    pygame.draw.line(screen,'white',(600,560),(570,600))

    #number lines
    pygame.draw.line(screen,'white',(240,340),(320,340))
    pygame.draw.line(screen,'white',(240,440),(320,440))
    pygame.draw.line(screen,'white',(240,540),(320,540))
    pygame.draw.line(screen,'white',(360,340),(440,340))
    pygame.draw.line(screen,'white',(360,440),(440,440))
    pygame.draw.line(screen,'white',(360,540),(440,540))
    pygame.draw.line(screen,'white',(480,340),(560,340))
    pygame.draw.line(screen,'white',(480,440),(560,440))
    pygame.draw.line(screen,'white',(480,540),(560,540))

    #lists to store the button and input box objects
    buttons= [Button(50,150,'gray',(900,100)),Button(50,50,'gray',(1010,100)),Button(50,50,'gray',(1070,100)),Button(50,150,'gray',(900,200)),Button(50,50,'gray',(1010,200)),Button(50,50,'gray',(1070,200)),Button(50,150,'gray',(900,600)),Button(50,150,'gray',(900,700)),Image('project/images/back.png',(1100,750))]
    inputBoxes = [SquareInputBox((280,312),''),SquareInputBox((400,312),''),SquareInputBox((520,312),''),
                  SquareInputBox((280,412),''),SquareInputBox((400,412),''),SquareInputBox((520,412),''),
                  SquareInputBox((280,512),''),SquareInputBox((400,512),''),SquareInputBox((520,512),'')]

    while True:
        #check for the user quitting the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #get mouse position to check agains buttons
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface,buttons[i].rect)
            if buttons[i].rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        #if the user clicks render
                        case 0:
                            plot(inputBoxes)
                        #if the user clicks back
                        case 8:
                            modules()

        #check for user inputs in the input boxes
        for i in range(len(inputBoxes)):
            #update the input boxes
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            #check if the input box is already selected
            if inputBoxes[i].selected:
                #check in the input box is currently locked
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    #if the input box is locked, update its timer
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                #check for numerical and arithmetic key entries
                else:
                    #check for the user clicking of the input box
                    if not inputBoxes[i].rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            inputBoxes[i].selected = False
                    #store the user inputs in the keys list
                    keys = pygame.key.get_pressed()
                    #if the user enters 0
                    if keys[pygame.K_0]:
                        inputBoxes[i].add('0')
                        inputBoxes[i].locked = True
                    #if the user enters 1
                    if keys[pygame.K_1]:
                        inputBoxes[i].add('1')
                        inputBoxes[i].locked = True
                    #if the user enters 2
                    if keys[pygame.K_2]:
                        inputBoxes[i].add('2')
                        inputBoxes[i].locked = True
                    #if the user enters 3
                    if keys[pygame.K_3]:
                        inputBoxes[i].add('3')
                        inputBoxes[i].locked = True
                    #if the user enters 4
                    if keys[pygame.K_4]:
                        inputBoxes[i].add('4')
                        inputBoxes[i].locked = True
                    #if the user enters 5
                    if keys[pygame.K_5]:
                        inputBoxes[i].add('5')
                        inputBoxes[i].locked = True
                    #if the user enters 6
                    if keys[pygame.K_6]:
                        inputBoxes[i].add('6')
                        inputBoxes[i].locked = True
                    #if the user enters 7
                    if keys[pygame.K_7]:
                        inputBoxes[i].add('7')
                        inputBoxes[i].locked = True
                    #if the user enters 8
                    if keys[pygame.K_8]:
                        inputBoxes[i].add('8')
                        inputBoxes[i].locked = True
                    #if the user enters 9
                    if keys[pygame.K_9]:
                        inputBoxes[i].add('9')
                        inputBoxes[i].locked = True
                    #if the user enters +
                    if keys[pygame.K_PLUS]:
                        inputBoxes[i].add('+')
                        inputBoxes[i].locked = True
                    #if the user enters -
                    if keys[pygame.K_MINUS]:
                        inputBoxes[i].add('-')
                        inputBoxes[i].locked = True
                    #if the user enters *
                    if keys[pygame.K_ASTERISK]:
                        inputBoxes[i].add('*')
                        inputBoxes[i].locked = True
                    #if the user enters /
                    if keys[pygame.K_SLASH]:
                        inputBoxes[i].add('/')
                        inputBoxes[i].locked = True
                    #if the user enters backspace key
                    if keys[pygame.K_BACKSPACE]:
                        inputBoxes[i].delete()
                        inputBoxes[i].locked = True
                    #if the user enters return key
                    if keys[pygame.K_RETURN]:
                        inputBoxes[i].calculate()
                        inputBoxes[i].locked = True
            #check if the user is clicking on to the input box
            else:
                if inputBoxes[i].rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        inputBoxes[i].selected = True

        pygame.display.update()
        clock.tick(60)

#function to take inputs for vectors
def vectors():
    screen.fill('black')
    pygame.draw.line(screen,'cyan',(800,0),(800,800))
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))
    #lambda image
    lambdaImage = pygame.image.load('project\images\lambda.png')
    #addition sign
    x = font.render('+',False,'white')
    #shell for vector a
    #left side of position vector
    pygame.draw.line(screen,'white',(860,50),(850,70))
    pygame.draw.line(screen,'white',(850,70),(850,160))
    pygame.draw.line(screen,'white',(850,160),(860,180))
    #right side of position vector
    pygame.draw.line(screen,'white',(940,50),(950,70))
    pygame.draw.line(screen,'white',(950,70),(950,160))
    pygame.draw.line(screen,'white',(950,160),(940,180))
    #left side of direction vector
    pygame.draw.line(screen,'white',(1060,50),(1050,70))
    pygame.draw.line(screen,'white',(1050,70),(1050,160))
    pygame.draw.line(screen,'white',(1050,160),(1060,180))
    #right side of direction vector
    pygame.draw.line(screen,'white',(1140,50),(1150,70))
    pygame.draw.line(screen,'white',(1150,70),(1150,160))
    pygame.draw.line(screen,'white',(1150,160),(1140,180))
    lambda1Rect = lambdaImage.get_rect(center = (1020,110))
    screen.blit(x,(975,90))

    #shell for vector b
    #left side of position vector
    pygame.draw.line(screen,'white',(860,230),(850,250))
    pygame.draw.line(screen,'white',(850,250),(850,340))
    pygame.draw.line(screen,'white',(850,340),(860,360))
    #right side of position vector
    pygame.draw.line(screen,'white',(940,230),(950,250))
    pygame.draw.line(screen,'white',(950,250),(950,340))
    pygame.draw.line(screen,'white',(950,340),(940,360))
    #left side of direction vector
    pygame.draw.line(screen,'white',(1060,230),(1050,250))
    pygame.draw.line(screen,'white',(1050,250),(1050,340))
    pygame.draw.line(screen,'white',(1050,340),(1060,360))
    #right side of direction vector
    pygame.draw.line(screen,'white',(1140,230),(1150,250))
    pygame.draw.line(screen,'white',(1150,250),(1150,340))
    pygame.draw.line(screen,'white',(1150,340),(1140,360))
    #render lambdas
    lambda2Rect = lambdaImage.get_rect(center = (1020,290))
    screen.blit(x,(975,270))

    #lists to store the button and input box objects
    buttons= [Button(50,50,'gray',(1020,700)),Image('project/images/back.png',(1100,750))]
    inputBoxes = [SquareInputBox((900,100),'00'),SquareInputBox((900,150),'00'),SquareInputBox((1100,100),'00'),SquareInputBox((1100,150),'00'),
                  SquareInputBox((900,280),'00'),SquareInputBox((900,330),'00'),SquareInputBox((1100,280),'00'),SquareInputBox((1100,330),'00')]
    
    while True:
        #check for the user quitting the programe
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #blit lambdas to screen
        screen.blit(lambdaImage,lambda1Rect)
        screen.blit(lambdaImage,lambda2Rect)
        #fecth mouse position to check if the user is hovering over a button
        mouse_pos = pygame.mouse.get_pos()
        #for each button, blit to screen and check if the user is clicking it
        for i in range(len(buttons)):
            screen.blit(buttons[i].surface,buttons[i].rect)
            if buttons[i].rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    match i:
                        case 0:
                            print('plot')
                            plotI(inputBoxes)
                        case 1:
                            modules()

        #check for user inputs in the input boxes
        for i in range(len(inputBoxes)):
            #update the input boxes
            screen.blit(inputBoxes[i].surface,inputBoxes[i].rect)
            screen.blit(inputBoxes[i].text,inputBoxes[i].rect)
            #check if the input box is already selected
            if inputBoxes[i].selected:
                #check in the input box is currently locked
                if inputBoxes[i].locked:
                    inputBoxes[i].timer += 1
                    #if the input box is locked, update its timer
                    if inputBoxes[i].timer == 10:
                        inputBoxes[i].timer = 0
                        inputBoxes[i].locked = False
                #check for numerical and arithmetic key entries
                else:
                    #check for the user clicking of the input box
                    if not inputBoxes[i].rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            inputBoxes[i].selected = False
                    #store the user inputs in the keys list
                    keys = pygame.key.get_pressed()
                    #if the user enters 0
                    if keys[pygame.K_0]:
                        inputBoxes[i].add('0')
                        inputBoxes[i].locked = True
                    #if the user enters 1
                    if keys[pygame.K_1]:
                        inputBoxes[i].add('1')
                        inputBoxes[i].locked = True
                    #if the user enters 2
                    if keys[pygame.K_2]:
                        inputBoxes[i].add('2')
                        inputBoxes[i].locked = True
                    #if the user enters 3
                    if keys[pygame.K_3]:
                        inputBoxes[i].add('3')
                        inputBoxes[i].locked = True
                    #if the user enters 4
                    if keys[pygame.K_4]:
                        inputBoxes[i].add('4')
                        inputBoxes[i].locked = True
                    #if the user enters 5
                    if keys[pygame.K_5]:
                        inputBoxes[i].add('5')
                        inputBoxes[i].locked = True
                    #if the user enters 6
                    if keys[pygame.K_6]:
                        inputBoxes[i].add('6')
                        inputBoxes[i].locked = True
                    #if the user enters 7
                    if keys[pygame.K_7]:
                        inputBoxes[i].add('7')
                        inputBoxes[i].locked = True
                    #if the user enters 8
                    if keys[pygame.K_8]:
                        inputBoxes[i].add('8')
                        inputBoxes[i].locked = True
                    #if the user enters 9
                    if keys[pygame.K_9]:
                        inputBoxes[i].add('9')
                        inputBoxes[i].locked = True
                    #if the user enters +
                    if keys[pygame.K_PLUS]:
                        inputBoxes[i].add('+')
                        inputBoxes[i].locked = True
                    #if the user enters -
                    if keys[pygame.K_MINUS]:
                        inputBoxes[i].add('-')
                        inputBoxes[i].locked = True
                    #if the user enters *
                    if keys[pygame.K_ASTERISK]:
                        inputBoxes[i].add('*')
                        inputBoxes[i].locked = True
                    #if the user enters /
                    if keys[pygame.K_SLASH]:
                        inputBoxes[i].add('/')
                        inputBoxes[i].locked = True
                    #if the user enters backspace key
                    if keys[pygame.K_BACKSPACE]:
                        inputBoxes[i].delete()
                        inputBoxes[i].locked = True
                    #if the user enters return key
                    if keys[pygame.K_RETURN]:
                        inputBoxes[i].calculate()
                        inputBoxes[i].locked = True
            #check if the user is clicking on to the input box
            else:
                if inputBoxes[i].rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        inputBoxes[i].selected = True

        pygame.display.update()
        clock.tick(60)

#function to render vectors
def vectorRender(inputBoxes):
    newCanvas = pygame.Surface((798,798))
    newCanvasRect = newCanvas.get_rect(center = (400,400))
    screen.blit(newCanvas,newCanvasRect)
    pygame.draw.line(screen,'white',(400,0),(400,800))
    pygame.draw.line(screen,'white',(0,400),(800,400))

mainMenu()