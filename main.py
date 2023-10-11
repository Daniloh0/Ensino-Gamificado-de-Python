import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Teste')
fps = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

while True:
    #event loop, checa todos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # termina while para que o codigo não continue

    # desenha na tela (main surface) a surface (test_surface) na posição x0 y0
    screen.blit(test_surface, (0,0))

    #desenha todos elementos e atualiza tudo
    pygame.display.update()
    # limita jogo a 60 fps
    fps.tick(60)