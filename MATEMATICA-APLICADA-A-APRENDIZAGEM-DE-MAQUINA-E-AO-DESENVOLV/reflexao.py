import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Reflexão de Objeto')

# Cores
white = (255, 255, 255)
red = (255, 0, 0)

# Parâmetros do objeto
obj_x = 300
obj_y = 300
obj_width = 80
obj_height = 30

# Direção da reflexão (vertical ou horizontal)
reflect_vertical = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpa a tela
    screen.fill(white)

    # Calcula a posição do objeto refletido
    if reflect_vertical:
        reflected_y = height - obj_y - obj_height
    else:
        reflected_x = width - obj_x - obj_width

    # Desenha o objeto original
    pygame.draw.rect(screen, red, (obj_x, obj_y, obj_width, obj_height))

    # Desenha o objeto refletido
    if reflect_vertical:
        pygame.draw.rect(screen, red, (obj_x, reflected_y, obj_width, obj_height))
    else:
        pygame.draw.rect(screen, red, (reflected_x, obj_y, obj_width, obj_height))

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()