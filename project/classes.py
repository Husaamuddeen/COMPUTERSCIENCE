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