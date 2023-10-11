import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Teste')
fps = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/Snail/Snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 301))

player_surface = pygame.image.load('graphics/Player/PlayerWalk1.png').convert_alpha()
# cria retangulo com tamanho do surface do player
player_rect = player_surface.get_rect(midbottom = (80, 301))

while True:
    #event loop, checa todos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # termina while para que o codigo não continue

    # desenha na tela (main surface) a surface (test_surface)
    screen.blit(sky_surface, (0,0))
    # a ordem que as imagens são desenhadas define o Z.
    screen.blit(ground_surface, (0, 301))
    screen.blit(text_surface, (300, 50))


    if (snail_rect.right < 0):
        snail_rect.left= 800
    #Fundo obrigaorio porque ele apenas desenha na tela por cima do frame anterior
    screen.blit(snail_surface, snail_rect)
    snail_rect.left -= 2

    screen.blit(player_surface, player_rect)

    player_rect.left += 1

    #desenha todos elementos e atualiza tudo
    pygame.display.update()
    # limita jogo a 60 fps
    fps.tick(60)

    #Retorna True se teve colisão e False se não.
    if player_rect.colliderect(snail_rect):
        print('Collision')

    #Checa se o cursor está encostando no personagem e printa se está sendo clicado ou não.
    #Cada um dos tres campos é um botão do mouse.
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())