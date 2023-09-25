import pygame
import sys
import math

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rotação de Objeto')

white = (255, 255, 255)
red = (255, 0, 0)

obj_x = 400
obj_y = 300
obj_width = 25
obj_height = 25
angle = 0 
rotation_speed = 1 

def rotate_point(point, angle, pivot):
    x, y = point
    px, py = pivot
    rotated_x = math.cos(math.radians(angle)) * (x - px) - math.sin(math.radians(angle)) * (y - py) + px
    rotated_y = math.sin(math.radians(angle)) * (x - px) + math.cos(math.radians(angle)) * (y - py) + py
    return rotated_x, rotated_y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(white)

    rotated_point = rotate_point((obj_x, obj_y), angle, (obj_x + obj_width / 2, obj_y + obj_height / 2))
    angle += rotation_speed

    pygame.draw.rect(screen, red, (rotated_point[0], rotated_point[1], obj_width, obj_height))

    pygame.display.flip()
pygame.quit()
sys.exit()
