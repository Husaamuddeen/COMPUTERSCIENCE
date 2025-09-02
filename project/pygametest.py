import pygame
from sys import exit

#initialise pygame screen
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('graphs')
clock = pygame.time.Clock()

#set default font
font = pygame.font.Font(None,50)

desktop = pygame.image.load('project/images/desktop.png').convert()
text = font.render('mathsmathsmathsmathsmathsmathsmathsmathsmathsmaths', False, 'black')


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
    screen.blit(desktop,(0,0))
    screen.blit(text,(0,500))
    screen.blit(button,buttonrec)

    #check for mouse collisions and mouse presses
    mouse_pos = pygame.mouse.get_pos()
    if buttonrec.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed()[0]:
            print('maths')

    pygame.display.update()
    clock.tick(60)