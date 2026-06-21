import pygame
pygame.init()

#Posição e velocidade do objeto inicio
x = 450
y = 100
velocidade = 5
#Posição e velocidade do objeto fim

#Programa para criar o fundo inicio
fundo = pygame.image.load('ufrpe.jpeg')
fundo = pygame.transform.scale(fundo, (1200,600))
#Programa para criar o fundo fim

#Programa para criar a música inicio
musica = pygame.mixer.music.load('Doki Doki Summertime OST - DDLC Jazz (improved) by Speißer(MP3_320K).mp3')
pygame.mixer.music.play(-1)
repete_Musica = True
#Programa para criar a música fim

#Programa para criar o personagem inicio
personagem_Monika = pygame.image.load('Monika_Teste.png')
#Programa para criar o personagem fim

#Programa para criar e fechar uma janela inicio

janela = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Projeto Doki Doki Literature Club UFRPE Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            repete_Musica = False

#Programa para criar e fechar uma janela final p1

#Programa para executar comandos do mouse inicio
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              x-= velocidade
            if event.button == 2:
              y-= velocidade
            if event.button == 3:
              x+= velocidade    
            #Se eu quiser que o comando funcione várias vezes ao
            #Segurar o botão do mouse, eu preciso colocar o comando
            #Fora do loop principal
#Programa para executar comandos do mouse fim

#Colacar e atualizar a janela de fundo para não ficar desenhando durante a atualização do objeto inicio
    #janela.fill((0,0,0))
    janela.blit(fundo, (0,0))
#Colocar e atualizar a janela de fundo para não ficar desenhando durante a atualização do objeto fim

#Programa de desenho inicio
    #pygame.draw.circle(janela, (0,255,0), (x,y), 50)
#Aparecendo a Monika inicio
    janela.blit(personagem_Monika, (x,y))
    pygame.display.update()
#Aparecendo a Monika fim
#Programa de desenho fim

pygame.quit()

#Programa para criar e fechar uma janela final p2
