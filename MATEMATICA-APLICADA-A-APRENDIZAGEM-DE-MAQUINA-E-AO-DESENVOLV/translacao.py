import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela de exibição
largura, altura = 200, 200
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Translação de Objeto')

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Posição inicial do objeto
objeto_x, objeto_y = largura // 2, altura // 2

# Tamanho do objeto
objeto_largura, objeto_altura = 25, 25

# Deslocamento (translação)
deslocamento_x, deslocamento_y = 25, 25

executando = True

while executando:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      executando = False

  # Atualiza a posição do objeto
  objeto_x += deslocamento_x
  objeto_y += deslocamento_y

  # Limpa a tela
  janela.fill(branco)

  # Desenha o objeto na nova posição
  pygame.draw.rect(janela, vermelho,
                   (objeto_x, objeto_y, objeto_largura, objeto_altura))

  # Atualiza a tela
  pygame.display.flip()

  # Controla a taxa de atualização
  pygame.time.delay(100)

pygame.quit()
sys.exit()
