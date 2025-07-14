import pygame
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Polynomial Function Plotter")
clock = pygame.time.Clock()

def polynomial(x):
    # Polynomial equation y = 0.01x^3 - 0.2x^2 + x + 10
    return 0.01 * x**3 - 0.2 * x**2 + x + 10

def plot_polynomial(screen, color, width):
    # The range of x values in screen pixels
    screen_width, screen_height = screen.get_size()
    x_min, x_max = -400, 400  # Range of x for the polynomial
    y_min, y_max = -100, 100  # Manually chosen range for y values (to fit the screen)

    # Map the polynomial from the mathematical domain to the pixel domain
    for x in range(x_min, x_max):
        # Calculate y value based on the polynomial
        y = polynomial(x)

        # Scale x and y to fit within the screen bounds
        screen_x = int(np.interp(x, [x_min, x_max], [0, screen_width]))
        screen_y = int(np.interp(y, [y_min, y_max], [screen_height, 0]))

        # Draw the point on the screen
        pygame.draw.circle(screen, color, (screen_x, screen_y), width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    plot_polynomial(screen, (0, 0, 255), 2)  # Plot the polynomial in blue

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
