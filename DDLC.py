import pygame
pygame.init()

#Posição e velocidade dos objetos inicio
largura_Da_Tela = 1200
altura_Da_Tela = 600
caixa_x = 0
caixa_y = 0
posicao_x = 0
posicao_y = 0
velocidade = 5
velocidade_Do_Andar = 50
#Posição e velocidade dos objetos fim

#Programa para criar a música inicio
musica = pygame.mixer.music.load('Doki Doki Summertime OST - DDLC Jazz (improved) by Speißer(MP3_320K).mp3')
pygame.mixer.music.play(-1)
repete_Musica = True
#Programa para criar a música fim

#Programa para criar e fechar uma janela inicio

janela = pygame.display.set_mode((largura_Da_Tela, altura_Da_Tela))
pygame.display.set_caption("Projeto Doki Doki Literature Club UFRPE Python")
rodaFrames = pygame.time.Clock()

#Sistema de diálogo inicio
caixaDeDialogo = pygame.image.load('caixa_De_Dialogo.png')
caixaDeDialogo = pygame.transform.scale(caixaDeDialogo, (largura_Da_Tela, altura_Da_Tela))

#Cores do texto
branco = (255,255,255)

#Fonte do texto
fonte = pygame.font.SysFont('Aller', 35)
fonteNome = pygame.font.SysFont('Riffic-Free-Medium-Bold', 35)

#Programa para criar o fundo inicio
fundo = pygame.image.load('ufrpe.jpeg')
fundo = pygame.transform.scale(fundo, (largura_Da_Tela, altura_Da_Tela))
#Programa para criar o fundo fim

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

#Diálogos
dialogos = [
    {"nome": "Monika", "texto": "Ehh...", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Então... De repente chegamos\
 por aqui e estamos perdidas", "Monika": True, "Yuri": True,\
    "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Você é um estudante daqui?",\
    "Monika": True, "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Estudante", "texto": "Sim, eu sou um estudante \
daqui. Eu estava indo para a minha \n\
sala revisar os assuntos de Matemática Discreta II, mas me \n\
encantei com a beleza de todas vocês.", "Monika": True, \
    "Yuri": True, "Sayori": True, "Natsuki": True},
]

indiceDialogo = 0

def desenhar_caixa_de_dialogo(nome, texto):
    #Renderiza a caixa de diálogo
    janela.blit(caixaDeDialogo, (caixa_x, caixa_y))

    # Renderiza o Nome do Personagem
    texto_nome = fonteNome.render(nome, True, (255, 150, 193)) # Cor Rosa Claro
    janela.blit(texto_nome, (267, 445))
    
    # Renderiza a Fala do Personagem
    texto_fala = fonte.render(texto, True, branco)
    janela.blit(texto_fala, (235, 485))


#Sistema de diálogo fim

#Loop do jogo inicio
janela_aberta = True
while janela_aberta:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            repete_Musica = False

#Programa para criar e fechar uma janela final

#Programa para executar comandos do mouse com o dialogo inicio
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Avança a história com o clique esquerdo do mouse
            if indiceDialogo < len(dialogos) - 1:
                caixa_y = 0
                indiceDialogo += 1
            else:
                janela_aberta = False # Fecha o jogo ao acabar a história
                repete_Musica = False
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            #y-= velocidade
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            #caixa_y = caixa_y - 1500
#Programa para executar comandos do mouse fim

#Programa para executar comandos do teclado inicio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Também avança com a barra de espaço
                if indiceDialogo < len(dialogos) - 1:
                    indiceDialogo += 1
                else:
                    janela_aberta = False
                    repete_Musica = False
#Programa para executar comandos do teclado fim

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
#Programa de desenho fim

#Aparecendo as personagens inicio
#Quanto antes o janela.blit, mais atrás a imagem fica, ou seja, a última imagem a ser desenhada fica na frente das outras
    
#Aparecendo as personagens fim

# Desenha a caixa de diálogo se estiver ativa inicio
    cena_atual = dialogos[indiceDialogo]
    
    if cena_atual["Natsuki"]:
    # Posiciona o personagem centralizado horizontalmente e apoiado na caixa de texto
        janela.blit(personagem_Natsuki, (posicao_x - 125, posicao_y)) #-125 com todas juntas

    if cena_atual["Sayori"]:
    # Posiciona o personagem centralizado horizontalmente e apoiado na caixa de texto
        janela.blit(personagem_Sayori, (posicao_x + 675, posicao_y)) #675 com todas juntas

    if cena_atual["Yuri"]:
    # Posiciona o personagem centralizado horizontalmente e apoiado na caixa de texto
        janela.blit(personagem_Yuri, (posicao_x + 425, posicao_y)) #425 com todas juntas

    if cena_atual["Monika"]:
    # Posiciona o personagem centralizado horizontalmente e apoiado na caixa de texto
        janela.blit(personagem_Monika, (posicao_x + 150, posicao_y)) #150 com todas juntas

    # Desenha a interface de texto por cima de tudo
    desenhar_caixa_de_dialogo(cena_atual["nome"], cena_atual["texto"])

    

    # Atualiza a tela
    pygame.display.flip()
    rodaFrames.tick(60) # Mantém o jogo a 60 Frames por Segundo

# Desenha a caixa de diálogo se estiver ativa fim

#Programa para criar e fechar uma janela final p2

pygame.quit()