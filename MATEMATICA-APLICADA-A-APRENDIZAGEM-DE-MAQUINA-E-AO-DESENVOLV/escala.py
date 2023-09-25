import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Escalando Objeto')

white = (255, 255, 255)
red = (255, 0, 0)

obj_x = 400
obj_y = 300
obj_width = 80
obj_height = 30
scale_factor = 1 


pivot_x = 300
pivot_y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
 
    new_width = int(obj_width * scale_factor)
    new_height = int(obj_height * scale_factor)

    scaled_x = pivot_x - (new_width - obj_width) / 2
    scaled_y = pivot_y - (new_height - obj_height) / 2

    pygame.draw.rect(screen, red, (scaled_x, scaled_y, new_width, new_height))

    pygame.display.flip()

pygame.quit()
sys.exit()
