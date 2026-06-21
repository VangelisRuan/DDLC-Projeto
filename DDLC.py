import pygame
pygame.init()

#Programa para criar uma janela inicio

janela = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

#Programa para criar uma janela final

pygame.quit()