import pygame
from sys import exit

#initialise pygame screen
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('graphs')
clock = pygame.time.Clock()

#set default font
font = pygame.font.Font(None,50)
a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
if a >= b:
    if a >= c:
        longest = a
    else:
        longest = c
else:
    if b >= c:
        longest = b
        

button = pygame.Surface(((100,100)))
button.fill('Blue')
buttonrec = button.get_rect(center = (50,50))
print(buttonrec)
#main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #update surfaces
    screen.blit(button,buttonrec)

    #check for mouse collisions and mouse presses
    mouse_pos = pygame.mouse.get_pos()
    if buttonrec.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed()[0]:
            print('maths')

    pygame.display.update()
    clock.tick(60)