import pygame
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