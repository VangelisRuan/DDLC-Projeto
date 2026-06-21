import pygame
pygame.init()

#Posição e velocidade dos objetos inicio
x = 150
y = 0
caixa_x = 0
caixa_y = 0
posicao_x = 0
posicao_y = 0
velocidade = 5
velocidade_Do_Andar = 50
#Posição e velocidade dos objetos fim

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
personagem_Monika = pygame.image.load('Monika_Teste_2.png')
personagem_Monika = pygame.transform.scale(personagem_Monika, (600,600))
#Programa para criar o personagem fim

personagem_Yuri = pygame.image.load('Yuri_Teste.png')
personagem_Yuri = pygame.transform.scale(personagem_Yuri, (600,600))
personagem_Sayori = pygame.image.load('Sayori_Teste.png')
personagem_Sayori = pygame.transform.scale(personagem_Sayori, (600,600))
personagem_Natsuki = pygame.image.load('Natsuki_Teste.png')
personagem_Natsuki = pygame.transform.scale(personagem_Natsuki, (600,600))

caixaDeDialogo = pygame.image.load('caixa_De_Dialogo.png')
caixaDeDialogo = pygame.transform.scale(caixaDeDialogo, (1200,600))

#Programa para criar e fechar uma janela inicio

janela = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Projeto Doki Doki Literature Club UFRPE Python")

janela_aberta = True
while janela_aberta:
#Comando para limitar o número de frames por segundo inicio
    #pygame.time.delay(50)
#Comando para limitar o número de frames por segundo fim

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

#Programa para personagem sumir quando chegar no final da tela inicio
    if (posicao_x >= 1500):
        posicao_x = 0
#Programa para personagem sumir quando chegar no final da tela fim

#Comando para o personagem andar inicio 
    #posicao_x += velocidade_Do_Andar
#Comando para o personagem andar fim

#Colacar e atualizar a janela de fundo para não ficar desenhando durante a atualização do objeto inicio
    #janela.fill((0,0,0))
    janela.blit(fundo, (0,0))
#Colocar e atualizar a janela de fundo para não ficar desenhando durante a atualização do objeto fim

#Programa de desenho inicio
    #pygame.draw.circle(janela, (0,255,0), (x,y), 50)
#Aparecendo a Monika inicio
    janela.blit(personagem_Monika, (x,y))
    janela.blit(personagem_Yuri, (posicao_x + 425,posicao_y))
    janela.blit(personagem_Sayori, (posicao_x + 675,posicao_y))
    janela.blit(personagem_Natsuki, (posicao_x - 125,posicao_y))
    janela.blit(caixaDeDialogo, (caixa_x,caixa_y))
    pygame.display.update()
#Aparecendo a Monika fim
#Programa de desenho fim

pygame.quit()

#Programa para criar e fechar uma janela final p2
