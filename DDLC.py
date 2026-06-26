import pygame
import sys
import random
pygame.init()

#Posição e velocidade dos objetos inicio
largura_Da_Tela = 1200
altura_Da_Tela = 600
caixa_x = 0
caixa_y = 0
posicao_x_Meme = 0
posicao_x = 0
posicao_y = 0
velocidade = 5
velocidade_Do_Andar = 50
#Posição e velocidade dos objetos fim

#Programa para criar a música inicio
musica = pygame.mixer.music.load("TrilhaSonoraUm.mp3")
pygame.mixer.music.play(-1)
repete_Musica = True
#Programa para criar a música fim

#Programa para atualizar trilha sonora inicio
musica_atual = ""

def tocar_musica(caminho_arquivo, loops=-1):
    global musica_atual
    # Só altera a música se ela for diferente da que já está tocando
    if musica_atual != caminho_arquivo:
        pygame.mixer.music.stop()          # Para a música anterior
        pygame.mixer.music.load(caminho_arquivo) # Carrega a nova
        pygame.mixer.music.play(loops)     # Toca em loop
        musica_atual = caminho_arquivo     # Atualiza o rastreamento
#Programa para atualizar trilha sonora fim

#Criando sons no botão inicio
somBotaoBrilhante = pygame.mixer.Sound("SomBotaoBrilhante.ogg")
somBotaoBrilhante.set_volume(0.5)
somBotaoSelecionado = pygame.mixer.Sound("SomSelecaoDeBotao.ogg")
somBotaoSelecionado.set_volume(0.5)
somEstalo = pygame.mixer.Sound("MonikaEstalo.mp3")
somEstalo.set_volume(100)
somRisada = pygame.mixer.Sound("MonikaRisada.ogg")
somRisada.set_volume(100)
somGlitch = pygame.mixer.Sound("MonikaGlitch.ogg")
somGlitch.set_volume(100)
#Criando sons no botão fim

#Programa para criar e fechar uma janela inicio
janela = pygame.display.set_mode((largura_Da_Tela, altura_Da_Tela))
pygame.display.set_caption("Projeto Doki Doki Literature Club UFRPE Python")
rodaFrames = pygame.time.Clock()

#Sistema de diálogo inicio
#Fazendo e posicionando a caixa de diálogo
caixaDeDialogo = pygame.image.load('caixa_De_Dialogo.png')
caixaDeDialogo = pygame.transform.scale(caixaDeDialogo, (largura_Da_Tela, altura_Da_Tela))

#Cores do texto
branco = (255,255,255)
preto = (0,0,0)

#Fontes dos textos
fonte = pygame.font.SysFont('Aller', 35)
fonteNome = pygame.font.SysFont('Riffic-Free-Medium-Bold', 35)

#Programa para criar o fundo inicio
fundo = pygame.image.load('ufrpe.jpeg')
fundo = pygame.transform.scale(fundo, (largura_Da_Tela, altura_Da_Tela))
#Programa para criar o fundo fim
fundoDois = pygame.image.load('UFRPE_Campo.png')
fundoDois = pygame.transform.scale(fundoDois, (largura_Da_Tela, altura_Da_Tela))
fundoTres = pygame.image.load('UFRPECaminhoCeagriDois.png')
fundoTres = pygame.transform.scale(fundoTres, (largura_Da_Tela, altura_Da_Tela))
fundoQuatro = pygame.image.load('UFRPE_Ceagri_Dois.jpg')
fundoQuatro = pygame.transform.scale(fundoQuatro, (largura_Da_Tela, altura_Da_Tela))
fundoCinco = pygame.image.load('UFRPE_Ceagri_Dois_Dentro.jpg')
fundoCinco = pygame.transform.scale(fundoCinco, (largura_Da_Tela, altura_Da_Tela))
fundoSeis = pygame.image.load('UFRPE_Ceagri_Dois_Dentro_Cima.jpg')
fundoSeis = pygame.transform.scale(fundoSeis, (largura_Da_Tela, altura_Da_Tela))
fundoSete = pygame.image.load('UFRPE_Ceagri_Dois_Sala.jpg')
fundoSete = pygame.transform.scale(fundoSete, (largura_Da_Tela, altura_Da_Tela))
fundoOito = pygame.image.load('UFRPE_Ceagri_Dois_Noite.jpg')
fundoOito = pygame.transform.scale(fundoOito, (largura_Da_Tela, altura_Da_Tela))
fundoNove = pygame.image.load('UFRPE_Ceagri_Dois_Portaria_Noite.jpg')
fundoNove = pygame.transform.scale(fundoNove, (largura_Da_Tela, altura_Da_Tela))
fundoDez = pygame.image.load('Apenas_Monika.png')
fundoDez = pygame.transform.scale(fundoDez, (largura_Da_Tela, altura_Da_Tela))
fundoOnze = pygame.image.load('Sala_Do_Clube.png')
fundoOnze = pygame.transform.scale(fundoOnze, (largura_Da_Tela, altura_Da_Tela))
fundoDoze = pygame.image.load('FinalBom.jpg')
fundoDoze = pygame.transform.scale(fundoDoze, (largura_Da_Tela, altura_Da_Tela))
fundoTreze = pygame.image.load('DokisFinalMeme.jpg')
fundoTreze = pygame.transform.scale(fundoTreze, (largura_Da_Tela, altura_Da_Tela))

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
personagem_Chamov = pygame.image.load('Chamov.png')
personagem_Chamov = pygame.transform.scale(personagem_Chamov, (300,300))
personagem_Assaltantes = pygame.image.load('Assaltantes.png')
personagem_Assaltantes = pygame.transform.scale(personagem_Assaltantes, (600,600))
personagem_MonikaOP = pygame.image.load('MonikaOP.png')
personagem_MonikaOP = pygame.transform.scale(personagem_MonikaOP, (600,600))
personagem_MonikaGlitch = pygame.image.load('Apenas_Monika_Glitch.png')
personagem_MonikaGlitch = pygame.transform.scale(personagem_MonikaGlitch, (largura_Da_Tela, altura_Da_Tela))

#Programa para criar imagens
pedra = pygame.image.load('pedra.PNG')
pedra = pygame.transform.scale(pedra, (300,300))
papel = pygame.image.load('papel.PNG')
papel = pygame.transform.scale(papel, (300,300))
tesoura = pygame.image.load('tesoura.PNG')
tesoura = pygame.transform.scale(tesoura, (300,300))
estaloMonika = pygame.image.load('EstaloMonika.png')
estaloMonika = pygame.transform.scale(estaloMonika, (150,150))
espelhoMonika = pygame.image.load('Espelho.png')
espelhoMonika = pygame.transform.scale(espelhoMonika, (933,600))

#Sistema de diálogos início
dialogos = [
    {"nome": "Estudante", "texto": "Eu estava andando por aí na Rural e de repente \
encontrei as\nfamosas garotas, Monika, Yuri, Sayori e Natsuki.","Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Estudante", "texto": "Sayori, a garota animada que tem olhos azuis,\
      \nYuri a garota misteriosa com cabelos roxos, Natsuki a\
      \nbaixinha entusiasta de mangá de cabelo rosa, e claro...","Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Estudante", "texto": "A garota mais popular de olhos verdes, Monika.\
      \nMas pera... Elas não são personagens de um jogo?", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Ehh...", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Então... De repente chegamos\
 por aqui e estamos perdidas.", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Você é um estudante daqui?", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Estudante", "texto": "Sim, eu sou um estudante \
daqui. Eu estava indo para a minha\
\nsala revisar os assuntos de Matemática Discreta II, mas me\
\nencantei com a beleza de todas vocês.", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Que meigo!", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Yuri", "texto": "Ehh... Ehh...", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Sayori", "texto": "Ahn?", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Natsuki", "texto": "Credo!", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Bem... Nós estávamos no Clube de Literatura e de repente,\
    \nfomos teleportadas para cá, você sabe dizer se tem alguma\
    \nsaída?", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Estudante", "texto": "Meninas, eu sou só um estudante comum e vocês apareceram\
    \ndo nada, infelizmente eu não posso ajudar muito vocês.", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Natsuki", "texto": "Monika, acho que não vamos conseguir nada pedindo ajuda\
     \na um inútil desses. Eu vou procuarar a saída sozinha!", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Yuri", "texto": "E... Eu vou dar uma explorada no local caso encontre alguma\
    \npista do que aconteceu, eu aviso a vocês.", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Sayori", "texto": "Eu vou procurar algo para comer, tô com mó fome!", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Monika", "texto": "Certo, pessoal... Vou explorar o local também. E quanto a\
    \nvocê, caso ache algo que aconteceu, seremos muito gratas!", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True},
    {"nome": "Estudante", "texto": "En... Entendido! Farei o meu melhor! Mas terei prova de\
    \nDiscreta hoje, talvez eu vá revisar os assuntos para tirar uma\
    \nboa nota, mas prometo avisar caso encontre algo.", "Monika": True, \
     "Yuri": True, "Sayori": True, "Natsuki": True}
]

dialogosDois = [
    {"nome": "Estudante", "texto": "Cara... isso foi muito repentino, mas darei uma volta\
     \nantes de revisar os assuntos.", "Botoes": False},
    {"nome": "Estudante", "texto": "Para onde eu devo seguir?", "Botoes": True}
]

dialogosTresOpcional = [
    {"nome": "???", "texto": "Ahh, olá moço! Eu me chamo Chamov, eu sou um aventureiro\
    \ne tava comprando algumas maçãs, quando de repente eu parei\
    \naqui! Muito louco né?", "Chamov": True},
    {"nome": "Estudante", "texto": "É... É!!! (o que está acontecendo aqui? primeiro as garotas de\
     \nDoki Doki, agora esse cachorro falante. Esse lugar está uma\
    \nloucura)", "Chamov": True},
    {"nome": "Chamov", "texto": "De qualquer forma, eu darei um jeito de voltar para casa. Eu\
     \nsou o maior explorador do mundo!! Tome uma maçã de\
    \npresente por ter falado comigo, você me parece faminto.", "Chamov": True},
    {"nome": "Estudante", "texto": "Ahh! Muito obrigado! (ele acertou em cheio)", "Chamov": True}
]

dialogosQuatroOpcional = [
    {"nome": "Natsuki", "texto": "Eae, encontrou algo?", "Natsuki": True},
    {"nome": "Estudante", "texto": "Nada ainda.", "Natsuki": True},
    {"nome": "Natsuki", "texto": "É mais inútil do que imaginei.", "Natsuki": True},
    {"nome": "Estudante", "texto": "Ei! Não seja tão cruel! Você também não encontrou nada\
     \naposto que você nem ganharia de mim no pedra, papel\
     \ne tesoura!", "Natsuki": True},
    {"nome": "Natsuki", "texto": "AGH!! Isso pode ser até verdade, mas perder para você no\
    \npedra, papel e tesoura para alguém como você? Jamais!", "Natsuki": True},
    {"nome": "Estudante", "texto": "É o que veremos! Bora jogar?", "Natsuki": True},
    {"nome": "Natsuki", "texto": "Vamos! Só não vá chorar depois que perder hein?\
     \nOutra coisa, se empatar, eu ganho também!", "Natsuki": True},
    {"nome": "Estudante", "texto": "Isso não me parece justo...", "Natsuki": True},
    {"nome": "Natsuki", "texto": "Mas foi você quem me desafiou. \
     \nSe você se garante tanto, isso não será um problema! Vamos!", "Natsuki": True}
]

dialogosCincoOpcional = [
    {"nome": "Estudante", "texto": "Aperte 1 para pedra, 2 para papel e 3 para tesoura.", "Natsuki": True}
]

dialogosSeisOpcional = [
    {"nome": "Natsuki", "texto": "Parece que alguém perdeu hahaha!", "Natsuki": True},
    {"nome": "Natsuki", "texto": "Tente novamente na próxima vez, perdedor.", "Natsuki": True}
]

dialogosSeteOpcional = [
    {"nome": "Natsuki", "texto": "Vai tentar novamente a sorte?", "Natsuki": True},
    {"nome": "Natsuki", "texto": "Heheh, se insiste tanto em ser humilhado por mim\
     \nentão não irei negar seu desafio!", "Natsuki": True}
]

dialogosOitoOpcional = [
    {"nome": "Natsuki", "texto": "UGH! ISSO FOI GOLPE DE SORTE!", "Natsuki": True},
    {"nome": "Estudante", "texto": "Aceite logo que eu ganhei.", "Natsuki": True},
    {"nome": "Natsuki", "texto": "Tá bem, tá bem, você ganhou. Feliz agora?", "Natsuki": True},
    {"nome": "Natsuki", "texto": "Mas na próxima irei ganhar! Espere só por isso!", "Natsuki": True},
    {"nome": "Estudante", "texto": "Estarei no aguardo! Ha ha!", "Natsuki": True}
]

dialogosNove = [
    {"nome": "Estudante", "texto": "Recife tá tão quente esses dias, né? Ninguém aguenta... Será\
\nque continuo ou deveria voltar pra talvez falar com mais\nalguém?"}
]

dialogosDez = [
    {"nome": "Estudante", "texto": "Daqui a pouco tenho prova de discreta no andar de cima...\
     \ndevo ir para sala de estudos em frente ou fazer logo a prova?"}
]

dialogosOnze = [
    {"nome": "Estudante", "texto": "Vejo dois rostos familiares em minha frente, Sayori e Yuri,\
     \ndeveria falar com elas enquanto a prova não começa."}
]

dialogosDozeOpcional = [
    {"nome": "Estudante", "texto": "O que vocês estão fazendo aqui?", "Sayori": True, "Yuri": True},
    {"nome": "Yuri", "texto": "Nada demais... estava apenas apreciando um bom livro.", "Sayori": True, "Yuri": True},
    {"nome": "Sayori", "texto": "*Nhac* *Nhac* E eu só to acompanhando ela mesmo.", "Sayori": True, "Yuri": True},
    {"nome": "Estudante", "texto": "Sayori você sequer sabe se pode comer aqui nessa sala?", "Sayori": True, "Yuri": True},
    {"nome": "Sayori", "texto": "Não, mas eu to com fome.", "Sayori": True, "Yuri": True},
    {"nome": "Yuri", "texto": "Suponho que não tenha problema nisso.", "Sayori": True, "Yuri": True},
    {"nome": "Yuri", "texto": "Então, o que te traz aqui?", "Sayori": True, "Yuri": True},
    {"nome": "Estudante", "texto": "Vim aqui revisar os assuntos de matemática discreta.", "Sayori": True, "Yuri": True},
    {"nome": "Sayori", "texto": "Isso é pra fazer conta de matemática escondido é?", "Sayori": True, "Yuri": True},
    {"nome": "Estudante", "texto": "Não Sayori... É matemática de detetive.", "Sayori": True, "Yuri": True},
    {"nome": "Sayori", "texto": "Uaauuuuu!", "Sayori": True, "Yuri": True},
    {"nome": "Yuri", "texto": "Se importaria se ajudarmos você a estudar?", "Sayori": True, "Yuri": True},
    {"nome": "Estudante", "texto": "De forma alguma, isso seria de grande ajuda!", "Sayori": True, "Yuri": True},
    {"nome": "Estudante", "texto": "Assim, Yuri e Sayori me ajudaram a revisar para o teste.", "Sayori": True, "Yuri": True}

]

dialogosTrezeOpcional = [
    {"nome": "Sayori e Yuri", "texto": "Boa prova!!", "Sayori": True, "Yuri": True}
]

dialogosCatorzeFinalRuim = [
    {"nome": "Estudante", "texto": "Finalmente acabei a prova de Matemática\
     \nDiscreta II, agora é só descansar...", "Assaltantes": False, "Monika": False, "MonikaOP": False},
    {"nome": "Assaltantes", "texto": "PARADO! ISSO É UM ASSALTO!\
      \nBORA PASSANDO TUDO DE VALOR AÍ!", "Assaltantes": True, "Monika": False, "MonikaOP": False},
    {"nome": "Estudante", "texto": "Mas eu não tenho nada além de caderno\
     \nou caneta!", "Assaltantes": True, "Monika": False, "MonikaOP": False},
     {"nome": "Assaltantes", "texto": "E ESSE NEGÓCIO TECNOLÓGICO ROSA?\
     \nPASSA LOGO!", "Assaltantes": True, "Monika": False, "MonikaOP": False},
     {"nome": "Estudante", "texto": "Que negócio tecnológico rosa?", "Assaltantes": True, "Monika": False, "MonikaOP": False},
     {"nome": "Estudante", "texto": "MAS O Q-", "Assaltantes": True, "Monika": False, "MonikaOP": False},
     {"nome": "", "texto": "", "Assaltantes": False, "Monika": True, "MonikaOP": False},
     {"nome": "", "texto": "", "Assaltantes": False, "Monika": False, "MonikaOP": True}
]

dialogosQuinzeFinalRuim = [
    {"nome": "", "texto": "", "MonikaGlitch": False},
    {"nome": "", "texto": "", "MonikaGlitch": True}
]

dialogosDezeseisFinalBom = [
    {"nome": "Estudante", "texto": "Finalmente acabei a prova de Matemática\
     \nDiscreta II, agora é só descansar...", "Assaltantes": False,\
     "Monika": False, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False},
     {"nome": "Assaltantes", "texto": "PARADO! ISSO É UM ASSALTO!\
      \nBORA PASSANDO TUDO DE VALOR AÍ!", "Assaltantes": True, "Monika": False, "MonikaOP": False\
      , "Yuri": False, "Sayori": False, "Natsuki": False},
       {"nome": "Estudante", "texto": "Não é possivel, nem depois de fazer essa prova eu tenho paz...", "Assaltantes": True,\
     "Monika": False, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False},
     {"nome": "Estudante", "texto": "AHHHHHHHHHHHHH!!!", "Assaltantes": True,\
     "Monika": False, "MonikaOP": True, "Yuri": False, "Sayori": False, "Natsuki": False}
]

dialogosDezeseteFinalBom = [
    {"nome": "Estudante", "texto": "Quando menos percebi, estava de volta no clube de literatura.",\
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Monika", "texto": "Ei Acorda!", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Sayori", "texto": "Será que ele tá bem?", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Natsuki", "texto": "Esse idiota só me faz ficar preocupada.", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Yuri", "texto": "(Olhando preocupada)", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Estudante", "texto": "Pessoal? Isso era tudo um sonho?", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Monika", "texto": "Sim, você tava dormindo o tempo todo.", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Estudante", "texto": "Mas e a prova? E... eu nem falei com aquele cachorro estranho.", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Monika", "texto": "Levanta! O festival já vai começar!",\
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Estudante", "texto": "Beleza, Vamos lá, pessoal!", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "Devs", "texto": "FINAL BOM ALCANÇADO! OBRIGADO POR JOGAR!", \
     "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True},
     {"nome": "", "texto": "", \
     "Monika": False, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False}
]

dialogosDezoitoFinalBomMeme = [
    {"nome": "Estudante", "texto": "Finalmente acabei a prova de Matemática\
     \nDiscreta II, agora é só descansar...", "Assaltantes": False,\
    "Monika": False, "MonikaOP": False, "Chamov": False},
    {"nome": "Assaltantes", "texto": "PARADO! ISSO É UM ASSALTO!\
      \nBORA PASSANDO TUDO DE VALOR AÍ!", "Assaltantes": True,\
    "Monika": False, "MonikaOP": False, "Chamov": False},
    {"nome": "Chamov", "texto": "Não vou deixar que façam isso com meu amigo!", "Assaltantes": True,\
    "Monika": False, "MonikaOP": False, "Chamov": True},
    {"nome": "Estudante", "texto": "Chamov! Você veio me ajudar!", "Assaltantes": True,\
    "Monika": False, "MonikaOP": False, "Chamov": True},
    {"nome": "Chamov", "texto": "Pode deixar comigo, ainda te devo muitas maçãs!", "Assaltantes": True,\
    "Monika": False, "MonikaOP": False, "Chamov": True},
    {"nome": "", "texto": "(No mesmo instate que Chamov foi pra cima dos Assaltantes...)", "Assaltantes": True,\
    "Monika": False, "MonikaOP": True, "Chamov": True},

    
]

dialogosDezenoveFinalBomMeme = [
    {"nome": "Estudante", "texto": "O que aconteceu?",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Chamov", "texto": "Eu... estou vivo?",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Natsuki", "texto": "Claro que tá, seu bixinho felpudo!",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Sayori", "texto": "Bem vindo de volta, garoto!",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Estudante", "texto": "De volta?", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Natsuki", "texto": "Claro né, seu bobão! Você é um dos\
     \nnossos e faz parte do nosso Clube de Literatura, não lembra?",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Sayori", "texto": "Que bom que você tá bem, aquele lanche tava tão bom!", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Sayori", "texto": "Que cachorrinho bonitinho!", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Yuri", "texto": "Fico feliz em ver vocês.", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Bem vindo ao Clube de literatura, Chamov! E bem vindo de\
    \nvolta Estudante.", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Chamov", "texto": "Mas eu nem te disse meu nome...",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Estudante", "texto": "PERA AÍ! PERA AÍ! PERA AÍ! QUE CONVERSA É ESSA QUE\
    \nSOU UM DE VOCÊS? EU SOU UM ESTUDANTE DA UFRPE,\
     \nNÃO UM MEMBRO DO CLUBE DE LITERATURA!",
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Estudante", "texto": "VOCÊS SÃO DE UM JOGO!",
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Estudante", "texto": "E COMO A MONIKA SABIA O NOME DO CHAMOV\
     \nSEM ELE NUNCA TER DITO O NOME DELE PRA ELA?\
     \nE O MAIS IMPORTANTE, COMO VIEMOS PARA AQUI???",
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Acalme-se, por favor...",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Eu devo uma bela explicação para todos vocês...",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Então dois bobinhos colocaram a gente no mundo real\
     \npor algum motivo, além de ter alterado todas as nossas\
     \nmemórias incluindo as suas.", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Só que isso não durou muito tempo para mim e recuperei\
     \nminhas funções para mexer nos arquivos do jogo, teleportei\
     \ntodos vocês e consegui restaurar as memórias da maioria.",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Mas por algum motivo, não obtive sucesso na\
     \nrecuperação de suas memórias, meu querido membro.\
     \nMas... Se não acredita em mim, vou provar para você.",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Estudante", "texto": "CARACA!! EU REALMENTE SOU UM DE VOCÊS!",\
    "Monika": False, "MonikaOP": True, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Natsuki", "texto": "Satisfeito agora, bocó?",\
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Além disso, eles colocaram até você, Chamov!\
     \nVocê pertence a outra série.", \
    "Monika": False, "MonikaOP": True, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Chamov", "texto": "Como isso pôde acontecer...?", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Quem sabe? Talvez você fosse a chave para isso.", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Estudante", "texto": "Então, o chamov vai ter que ficar aqui com a gente?", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Monika", "texto": "Bem, se ele quiser...", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Chamov", "texto": "Eu não me importaria! Muito obrigado, pessoal!", \
    "Monika": True, "MonikaOP": False, "Yuri": True, "Sayori": True, "Natsuki": True, "Chamov": True},
    {"nome": "Estudante", "texto": "Assim, todos saem da sala e vão para o festival,\
     \nmenos a Monika.", \
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False},
    {"nome": "Monika", "texto": "Bem, pelo menos todos estão bem.", \
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False},
    {"nome": "Monika", "texto": "E você ai atrás da tela jogando esse jogo.", \
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False},
    {"nome": "Monika", "texto": "Obrigada por passar um tempo com todos nós, mesmo que\
    \nseja bem breve.", \
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False},
    {"nome": "Monika", "texto": "Parabéns por alcançar o final verdadeiro.", \
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False},
    {"nome": "Monika", "texto": "Obrigado por jogar!",\
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False},
    {"nome": "", "texto": "",\
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False},
    {"nome": "", "texto": "",\
    "Monika": True, "MonikaOP": False, "Yuri": False, "Sayori": False, "Natsuki": False, "Chamov": False}
]

indiceDialogo = 0
cenaAtiva = 1

def desenhar_caixa_de_dialogo(nome, texto):
    #Renderiza a caixa de diálogo
    janela.blit(caixaDeDialogo, (posicao_x_Meme + caixa_x, caixa_y))
    
    #Deslocamentos para o contorno
    deslocamentos = [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0),
        (-1,  1), (0,  1), (1,  1)
    ]
    
    #Renderiza o contorno do nome do personagem
    for dx, dy in deslocamentos:
        surfContorno = fonte.render(nome, True, (255, 20, 147)) # Cor Rosa Escuro
        rectContorno = surfContorno.get_rect(center=(posicao_x_Meme + 327 + dx, 457 + dy))
        janela.blit(surfContorno, rectContorno)

    #Renderiza o texto principal em cima do nome do personagem
    surfPrincipal = fonte.render(nome, True, branco)
    rectPrincipal = surfPrincipal.get_rect(center=(posicao_x_Meme + 327, 457))
    janela.blit(surfPrincipal, rectPrincipal)

    #Renderiza o contorno da fala do personagem
    for dx, dy in deslocamentos:
        surfContorno = fonte.render(texto, True, preto)
        rectContorno = surfContorno.get_rect(topleft=(posicao_x_Meme + 235 + dx, 485 + dy))
        janela.blit(surfContorno, rectContorno)

    #Renderiza o texto principal em cima da fala do personagem
    surfPrincipal = fonte.render(texto, True, branco)
    rectPrincipal = surfPrincipal.get_rect(topleft=(posicao_x_Meme + 235, 485))
    janela.blit(surfPrincipal, rectPrincipal)

#Sistema de diálogos fim

chamovNormal = pygame.image.load("Chamov.png").convert_alpha()
chamovNormal = pygame.transform.scale(chamovNormal, (100, 100))
chamovBrilhante = pygame.image.load("ChamovBrilhante.png").convert_alpha()
chamovBrilhante = pygame.transform.scale(chamovBrilhante, (100, 100))
sayoriEYuri = pygame.image.load("SayoriEYuri.png").convert_alpha()
sayoriEYuri = pygame.transform.scale(sayoriEYuri, (350, 350))
sayoriEYuriBrilhante = pygame.image.load("SayoriEYuriBrilhante.png").convert_alpha()
sayoriEYuriBrilhante = pygame.transform.scale(sayoriEYuriBrilhante, (350, 350))
setaDireita = pygame.image.load("BotaoSetaDireita.png").convert_alpha()
setaDireita = pygame.transform.scale(setaDireita, (100, 100))
setaDireitaBrilhante = pygame.image.load("BotaoSetaDireitaBrilhante.png").convert_alpha()
setaDireitaBrilhante = pygame.transform.scale(setaDireitaBrilhante, (100, 100))
#Muda a rotação do botão
#setaDireita = pygame.transform.rotate(setaDireita, 180)
#setaDireitaBrilhante = pygame.transform.rotate(setaDireitaBrilhante, 180)
setaDiagonalCimaDireita = pygame.image.load("BotaoSetaDiagonalCimaDireita.png").convert_alpha()
setaDiagonalCimaDireita = pygame.transform.scale(setaDiagonalCimaDireita, (100, 100))
setaDiagonalCimaDireitaBrilhante = pygame.image.load("BotaoSetaDiagonalCimaDireitaBrilhante.png").convert_alpha()
setaDiagonalCimaDireitaBrilhante = pygame.transform.scale(setaDiagonalCimaDireitaBrilhante, (100, 100))
setaDiagonalCimaEsquerda = pygame.image.load("BotaoSetaDiagonalCimaEsquerda.png").convert_alpha()
setaDiagonalCimaEsquerda = pygame.transform.scale(setaDiagonalCimaEsquerda, (100, 100))
setaDiagonalCimaEsquerdaBrilhante = pygame.image.load("BotaoSetaDiagonalCimaEsquerdaBrilhante.png").convert_alpha()
setaDiagonalCimaEsquerdaBrilhante = pygame.transform.scale(setaDiagonalCimaEsquerdaBrilhante, (100, 100))
setaCima = pygame.image.load("BotaoSetaCima.png").convert_alpha()
setaCima = pygame.transform.scale(setaCima, (100, 100))
setaCimaBrilhante = pygame.image.load("BotaoSetaCimaBrilhante.png").convert_alpha()
setaCimaBrilhante = pygame.transform.scale(setaCimaBrilhante, (100, 100))
setaEsquerda = pygame.image.load("BotaoSetaEsquerda.png").convert_alpha()
setaEsquerda = pygame.transform.scale(setaEsquerda, (100, 100))
setaEsquerdaBrilhante = pygame.image.load("BotaoSetaEsquerdaBrilhante.png").convert_alpha()
setaEsquerdaBrilhante = pygame.transform.scale(setaEsquerdaBrilhante, (100, 100))
setaDiagonalBaixoEsquerda = pygame.image.load("BotaoSetaDiagonalBaixoEsquerda.png").convert_alpha()
setaDiagonalBaixoEsquerda = pygame.transform.scale(setaDiagonalBaixoEsquerda, (100, 100))
setaDiagonalBaixoEsquerdaBrilhante = pygame.image.load("BotaoSetaDiagonalBaixoEsquerdaBrilhante.png").convert_alpha()
setaDiagonalBaixoEsquerdaBrilhante = pygame.transform.scale(setaDiagonalBaixoEsquerdaBrilhante, (100, 100))
setaDiagonalBaixoDireita = pygame.image.load("BotaoSetaDiagonalBaixoDireita.png").convert_alpha()
setaDiagonalBaixoDireita = pygame.transform.scale(setaDiagonalBaixoDireita, (100, 100))
setaDiagonalBaixoDireitaBrilhante = pygame.image.load("BotaoSetaDiagonalBaixoDireitaBrilhante.png").convert_alpha()
setaDiagonalBaixoDireitaBrilhante = pygame.transform.scale(setaDiagonalBaixoDireitaBrilhante, (100, 100))
setaBaixo = pygame.image.load("BotaoSetaBaixo.png").convert_alpha()
setaBaixo = pygame.transform.scale(setaBaixo, (100, 100))
setaBaixoBrilhante = pygame.image.load("BotaoSetaBaixoBrilhante.png").convert_alpha()
setaBaixoBrilhante = pygame.transform.scale(setaBaixoBrilhante, (100, 100))

#Retangulo para seleção do botão
botaoChamov = chamovNormal.get_rect()
#Muda a posição do botão
botaoChamov.topleft = (3000, 3000)

botaoSayoriEYuri = sayoriEYuri.get_rect()
botaoSayoriEYuri.topleft = (3000, 3000)

botaoSetaUm = setaDireita.get_rect()
botaoSetaUm.topleft = (3000, 3000)

botaoSetaDois = setaDiagonalCimaDireita.get_rect()
botaoSetaDois.topleft = (3000, 3000)

botaoSetaTres = setaDiagonalBaixoEsquerda.get_rect()
botaoSetaTres.topleft = (3000, 3000)

botaoSetaQuatro = setaDiagonalCimaEsquerda.get_rect()
botaoSetaQuatro.topleft = (3000, 3000)

botaoSetaCinco = setaBaixo.get_rect()
botaoSetaCinco.topleft = (3000, 3000)

botaoSetaSeis = setaDiagonalCimaEsquerda.get_rect()
botaoSetaSeis.topleft = (3000, 3000)

botaoSetaSete = setaDiagonalCimaDireita.get_rect()
botaoSetaSete.topleft = (3000, 3000)

botaoSetaOito = setaBaixo.get_rect()
botaoSetaOito.topleft = (3000, 3000)

#Variaveis do Pedra, Papel e Tesoura
texto_jogador = "Você: ?"
texto_computador = "Natsuki: ?"
texto_resultado = "Aperte 1, 2 ou 3 para jogar!"

# Lista de opções para o computador escolher
opcoes = ["Pedra", "Papel", "Tesoura"]

imagensDoPPT = {
    "Pedra": pedra,
    "Papel": papel,
    "Tesoura": tesoura
}

exibirJogador = None
exibirNatsuki = None

#Loop do jogo inicio
janela_aberta = True

falouComOChamov = False
falouComANatsuki = False
ganhouDaNatsuki = False
falouComASayoriEYuri = False

somJaTocou = False
somJaTocouDois = False
somJaTocouTres = False
somJaTocouQuatro = False
somJaTocouCinco = False
somJaTocouSeis = False
somJaTocouSete = False
somJaTocouOito = False
somJaTocouNove = False
somJaTocouDez = False
somJaTocouEstalo = False
somJaTocouRisada = False
somJaTocouGlitch = False

contadorDeFrames = 0

while janela_aberta:

#Colacar e atualizar a janela de fundo para não ficar desenhando durante a atualização do objeto inicio
    #janela.fill((0,0,0))
    janela.blit(fundo, (0,0))
#Colocar e atualizar a janela de fundo para não ficar desenhando durante a atualização do objeto fim

    #Posição do mouse atual
    posicaoMouse = pygame.mouse.get_pos()
    
#Define qual cena será utilizada
    if cenaAtiva == 1:
        listaAtual = dialogos
        cena_atual = listaAtual[indiceDialogo]

#Aparecendo as personagens inicio
#Mostra o objeto desejado caso ele seja True durante o diálogo
#Quanto antes o janela.blit, mais atrás a imagem fica, ou seja, a última imagem a ser desenhada fica na frente das outras
        if cena_atual["Natsuki"]:
        # Posiciona o personagem centralizado horizontalmente e apoiado na caixa de texto
            janela.blit(personagem_Natsuki, (posicao_x - 125, posicao_y)) #-125 com todas juntas

        if cena_atual["Sayori"]:
            janela.blit(personagem_Sayori, (posicao_x + 675, posicao_y)) #675 com todas juntas

        if cena_atual["Yuri"]:
            janela.blit(personagem_Yuri, (posicao_x + 425, posicao_y)) #425 com todas juntas

        if cena_atual["Monika"]:
            janela.blit(personagem_Monika, (posicao_x + 150, posicao_y)) #150 com todas juntas
#Aparecendo as personagens fim

    if cenaAtiva == 2:
        listaAtual = dialogosDois
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundo, (0,0))

        #Efeito do botão brilhando quando passa o mouse por cima
        if falouComOChamov == False:
            if cena_atual["Botoes"]:
                if botaoChamov.collidepoint(posicaoMouse):
                    imagemAtual = chamovBrilhante
                     #Só toca se ainda o mouse não tiver tocado
                    if not somJaTocou:
                        somBotaoBrilhante.play()
                        somJaTocou = True
                else:
                    imagemAtual = chamovNormal
                    somJaTocou = False #Quando o mouse sai, permite tocar de novo na próxima vez

                #Desenha o botão na tela
                #pygame.draw.rect(janela, cor_atual, chamovNormal)

                #Centraliza o texto no botão
                #texto_rect = texto_botao.get_rect(center=botaoSeta.center)
                janela.blit(imagemAtual, botaoChamov)
        
        else:
            botaoChamov.topleft = (3000, 3000)

        if ganhouDaNatsuki == False:
            if cena_atual["Botoes"]:
                if botaoSetaUm.collidepoint(posicaoMouse):
                    imagemAtualDois = setaDireitaBrilhante
                    if not somJaTocouDois:
                        somBotaoBrilhante.play()
                        somJaTocouDois = True
                else:
                    imagemAtualDois = setaDireita
                    somJaTocouDois = False
                janela.blit(imagemAtualDois, botaoSetaUm)
        else:
            botaoSetaUm.topleft = (3000, 3000)

        if cena_atual["Botoes"]:
            if botaoSetaDois.collidepoint(posicaoMouse):
                imagemAtualTres = setaDiagonalCimaDireitaBrilhante
                if not somJaTocouTres:
                    somBotaoBrilhante.play()
                    somJaTocouTres = True
            else:
                imagemAtualTres = setaDiagonalCimaDireita
                somJaTocouTres = False
            
            janela.blit(imagemAtualTres, botaoSetaDois)

    if cenaAtiva == 3:
        listaAtual = dialogosTresOpcional
        cena_atual = listaAtual[indiceDialogo]
        if cena_atual["Chamov"]:
            janela.blit(personagem_Chamov, (posicao_x + 450, posicao_y + 300))
        

    if cenaAtiva == 4:
        listaAtual = dialogosQuatroOpcional
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoDois, (0,0))
        falouComANatsuki = True
        if cena_atual["Natsuki"]:
            janela.blit(personagem_Natsuki, (posicao_x + 300, posicao_y))

    if cenaAtiva == 5:
        listaAtual = dialogosCincoOpcional
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoDois, (0,0))
        tocar_musica("TrilhaSonoraMiniGame.mp3")

        if cena_atual["Natsuki"]:
            janela.blit(personagem_Natsuki, (posicao_x + 300, posicao_y))

    if cenaAtiva == 6:
        listaAtual = dialogosSeisOpcional
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoDois, (0,0))
        if cena_atual["Natsuki"]:
            janela.blit(personagem_Natsuki, (posicao_x + 300, posicao_y))

        # Desenha as imagens na tela se o jogo já tiver começado
        if exibirJogador and exibirNatsuki:
            # Imagem do jogador no lado esquerdo
            janela.blit(imagensDoPPT[exibirJogador], (100, 150))
            # Imagem do computador no lado direito
            janela.blit(imagensDoPPT[exibirNatsuki], (800, 150))
    
    if cenaAtiva == 7:
        listaAtual = dialogosSeteOpcional
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoDois, (0,0))
        if cena_atual["Natsuki"]:
            janela.blit(personagem_Natsuki, (posicao_x + 300, posicao_y))

    if cenaAtiva == 8:
        listaAtual = dialogosOitoOpcional
        cena_atual = listaAtual[indiceDialogo]
        ganhouDaNatsuki = True
        janela.blit(fundoDois, (0,0))
        if cena_atual["Natsuki"]:
            janela.blit(personagem_Natsuki, (posicao_x + 300, posicao_y))

        if exibirJogador and exibirNatsuki:
            janela.blit(imagensDoPPT[exibirJogador], (100, 150))
            janela.blit(imagensDoPPT[exibirNatsuki], (800, 150))

    if cenaAtiva == 9:
        listaAtual = dialogosNove
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoTres, (0,0))
        botaoSetaTres.topleft = (100, 400)
        botaoSetaQuatro.topleft = (500, 250)

        if botaoSetaTres.collidepoint(posicaoMouse):
            imagemAtualQuatro = setaDiagonalBaixoEsquerdaBrilhante
            if not somJaTocouQuatro:
                somBotaoBrilhante.play()
                somJaTocouQuatro = True
        else:
            imagemAtualQuatro = setaDiagonalBaixoEsquerda
            somJaTocouQuatro = False
        janela.blit(imagemAtualQuatro, botaoSetaTres)

        if botaoSetaQuatro.collidepoint(posicaoMouse):
            imagemAtualCinco = setaDiagonalCimaEsquerdaBrilhante
            if not somJaTocouCinco:
                somBotaoBrilhante.play()
                somJaTocouCinco = True
        else:
            imagemAtualCinco = setaDiagonalCimaEsquerda
            somJaTocouCinco = False
            
        janela.blit(imagemAtualCinco, botaoSetaQuatro)

    if cenaAtiva == 10:
        listaAtual = dialogosDez
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoCinco, (0,0))
        botaoSetaCinco.topleft = (100, 475)
        botaoSetaSeis.topleft = (425, 300)
        botaoSetaSete.topleft = (575, 275)

        if botaoSetaCinco.collidepoint(posicaoMouse):
            imagemAtualSeis = setaBaixoBrilhante
            if not somJaTocouSeis:
                somBotaoBrilhante.play()
                somJaTocouSeis = True
        else:
            imagemAtualSeis = setaBaixo
            somJaTocouSeis = False
        janela.blit(imagemAtualSeis, botaoSetaCinco)

        if botaoSetaSeis.collidepoint(posicaoMouse):
            imagemAtualSete = setaDiagonalCimaEsquerdaBrilhante
            if not somJaTocouSete:
                somBotaoBrilhante.play()
                somJaTocouSete = True
        else:
            imagemAtualSete = setaDiagonalCimaEsquerda
            somJaTocouSete = False

        janela.blit(imagemAtualSete, botaoSetaSeis)

        if botaoSetaSete.collidepoint(posicaoMouse):
            imagemAtualOito = setaDiagonalCimaDireitaBrilhante
            if not somJaTocouOito:
                somBotaoBrilhante.play()
                somJaTocouOito = True
        else:
            imagemAtualOito = setaDiagonalCimaDireita
            somJaTocouOito = False
        janela.blit(imagemAtualOito, botaoSetaSete)

    if cenaAtiva == 11:
        listaAtual = dialogosOnze
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoSete, (0,0))
        botaoSetaOito.topleft = (1050, 475)
        botaoSayoriEYuri.topleft = (700, 150)

        if botaoSetaOito.collidepoint(posicaoMouse):
            imagemAtualNove = setaBaixoBrilhante
            if not somJaTocouNove:
                somBotaoBrilhante.play()
                somJaTocouNove = True
        else:
            imagemAtualNove = setaBaixo
            somJaTocouNove = False
        janela.blit(imagemAtualNove, botaoSetaOito)

        if botaoSayoriEYuri.collidepoint(posicaoMouse):
            imagemAtualDez = sayoriEYuriBrilhante
            if not somJaTocouDez:
                somBotaoBrilhante.play()
                somJaTocouDez = True
        else:
            imagemAtualDez = sayoriEYuri
            somJaTocouDez = False
        janela.blit(imagemAtualDez, botaoSayoriEYuri)

    if cenaAtiva == 12:
        listaAtual = dialogosDozeOpcional
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoSete, (0,0))
        botaoSetaOito.topleft = (3000, 3000)
        botaoSayoriEYuri.topleft = (3000, 3000)

        if cena_atual["Sayori"]:
            janela.blit(personagem_Sayori, (posicao_x + 100, posicao_y))

        if cena_atual["Yuri"]:
            janela.blit(personagem_Yuri, (posicao_x + 500, posicao_y))


    if cenaAtiva == 13:
        listaAtual = dialogosTrezeOpcional
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoSete, (0,0))
        botaoSayoriEYuri.topleft = (3000, 3000)

        if cena_atual["Sayori"]:
            janela.blit(personagem_Sayori, (posicao_x + 100, posicao_y))
        if cena_atual["Yuri"]:
            janela.blit(personagem_Yuri, (posicao_x + 500, posicao_y))

    if cenaAtiva == 14:
        listaAtual = dialogosCatorzeFinalRuim
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoNove, (0,0))

        if cena_atual["Monika"]:
            janela.blit(personagem_Monika, (posicao_x + 300, posicao_y))

        if cena_atual["MonikaOP"]:
            janela.blit(personagem_MonikaOP, (posicao_x + 300, posicao_y))
            janela.blit(estaloMonika, (posicao_x + 375, posicao_y + 150))
            if not somJaTocouEstalo:
                somEstalo.play()
                somJaTocouEstalo = True
            
        if cena_atual["Assaltantes"]:
            janela.blit(personagem_Assaltantes, (posicao_x_Meme + 300, posicao_y + 175))
            tocar_musica("MusicaSuspense.mp3")

        if indiceDialogo >= 5 and cenaAtiva == 14:
            #Comando para o personagem andar inicio 
            posicao_x_Meme -= velocidade_Do_Andar
            #Comando para o personagem andar fim

    if cenaAtiva == 15:
        listaAtual = dialogosQuinzeFinalRuim
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoDez, (0,0))
        tocar_musica("JustMonika.mp3")
        posicao_x_Meme -= velocidade_Do_Andar

        if cena_atual["MonikaGlitch"]:
            janela.blit(personagem_MonikaGlitch, (0, 0))
            if not somJaTocouRisada:
                somRisada.play()
                somJaTocouRisada = True
            #if not somJaTocouGlitch:
            #    somJaTocouGlitch = True


    if cenaAtiva == 16:
        listaAtual = dialogosDezeseisFinalBom
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoNove, (0,0))

        if cena_atual["Assaltantes"]:
            janela.blit(personagem_Assaltantes, (posicao_x_Meme + 300, posicao_y + 175))
            tocar_musica("MusicaSuspense.mp3")

        if cena_atual["MonikaOP"]:
            if not somJaTocouEstalo:
                somEstalo.play()
                somJaTocouEstalo = True

    if cenaAtiva == 17:
        listaAtual = dialogosDezeseteFinalBom
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoOnze, (0,0))
        tocar_musica("TrilhaSonoraDois.mp3")

        if cena_atual["Natsuki"]:
            janela.blit(personagem_Natsuki, (posicao_x - 125, posicao_y)) #-125 com todas juntas

        if cena_atual["Sayori"]:
            janela.blit(personagem_Sayori, (posicao_x + 675, posicao_y)) #675 com todas juntas

        if cena_atual["Yuri"]:
            janela.blit(personagem_Yuri, (posicao_x + 425, posicao_y)) #425 com todas juntas

        if cena_atual["Monika"]:
            janela.blit(personagem_Monika, (posicao_x + 150, posicao_y))

        if indiceDialogo == 10:
            janela.blit(fundoDoze, (0, 0))
            posicao_x = 3000

    if cenaAtiva == 18:
        listaAtual = dialogosDezoitoFinalBomMeme
        cena_atual = listaAtual[indiceDialogo]
        janela.blit(fundoNove, (0,0))

        if cena_atual["Assaltantes"]:
            janela.blit(personagem_Assaltantes, (posicao_x + 300, posicao_y + 175))
            tocar_musica("MusicaSuspense.mp3")
        if cena_atual["MonikaOP"]:
            if not somJaTocouEstalo:
                somEstalo.play()
                somJaTocouEstalo = True
        if cena_atual["Chamov"]:
            janela.blit(personagem_Chamov,(posicao_x + 100, posicao_y + 300))

        if indiceDialogo > 4 and cenaAtiva == 18: 
            posicao_x += velocidade_Do_Andar

    if cenaAtiva == 19:
        listaAtual = dialogosDezenoveFinalBomMeme
        cena_atual = listaAtual[indiceDialogo]
        posicao_x = 0
        janela.blit(fundoOnze, (0,0))
        tocar_musica("TrilhaSonoraDois.mp3")


        if cena_atual["Natsuki"]:
            janela.blit(personagem_Natsuki, (posicao_x - 125, posicao_y))

        if cena_atual["Sayori"]:
            janela.blit(personagem_Sayori, (posicao_x + 675, posicao_y))

        if cena_atual["Yuri"]:
            janela.blit(personagem_Yuri, (posicao_x + 425, posicao_y))

        if cena_atual["Monika"]:
            if indiceDialogo >= 27 and indiceDialogo < 33:
                janela.blit(personagem_Monika, (posicao_x + 300, posicao_y))
            else:
                janela.blit(personagem_Monika, (posicao_x + 150, posicao_y))

        if cena_atual["MonikaOP"]:
            janela.blit(personagem_MonikaOP, (posicao_x + 150, posicao_y))
            if not somJaTocouEstalo:
                somEstalo.play()
                somJaTocouEstalo = True
                tempoImagemMostrada = True
                
            if tempoImagemMostrada:
                janela.blit(estaloMonika, (posicao_x + 225, posicao_y + 150))

                contadorDeFrames += 1

                if contadorDeFrames >= 5:
                    tempoImagemMostrada = False
                    contadorDeFrames = 0

        
        if cena_atual["Chamov"]:
            janela.blit(personagem_Chamov, (posicao_x + 450, posicao_y + 300))
        
        if indiceDialogo == 18:
            somJaTocouEstalo = False

        if indiceDialogo >= 19 and indiceDialogo < 21:
            janela.blit(espelhoMonika, (posicao_x + 100, posicao_y))

        if indiceDialogo == 20:
            somJaTocouEstalo = False

        if indiceDialogo == 33:
            janela.blit(fundoTreze, (0, 0))
            posicao_x = 3000
            caixa_x = 3000


    # Desenha a interface de texto por cima de tudo
    desenhar_caixa_de_dialogo(cena_atual["nome"], cena_atual["texto"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            repete_Musica = False
#Programa para criar e fechar uma janela final

#Programa para executar comandos do mouse com o primero diálogo inicio
        avancarNaHistoria = False

        if cenaAtiva == 2 and indiceDialogo == 1:
            botaoChamov.topleft = (60, 350)
            botaoSetaUm.topleft = (1050, 250)
            botaoSetaDois.topleft = (750, 175)

        if cenaAtiva == 15 and indiceDialogo == 1:
            pygame.time.wait(1000)#Ou 200 para algo mais instantâneo
            janela_aberta = False
            repete_Musica = False

        if cenaAtiva == 14 and indiceDialogo == 7:
            pygame.time.wait(650)
            cenaAtiva = 15
            indiceDialogo = 0

        if cenaAtiva == 16 and indiceDialogo == 3:
            pygame.time.wait(650)
            cenaAtiva = 17
            indiceDialogo = 0

        if cenaAtiva == 17 and indiceDialogo == 11:
            janela_aberta = False
            repete_Musica = False

        if cenaAtiva == 18 and indiceDialogo == 5:
            pygame.time.wait(650)
            cenaAtiva = 19
            indiceDialogo = 0

        if cenaAtiva == 19 and indiceDialogo == 34:
            janela_aberta = False
            repete_Musica = False

        if cenaAtiva == 5:
            if event.type == pygame.KEYDOWN:
                jogou = False
                escolhaJogador = ""
                
                # Identifica qual tecla você apertou
                if event.key == pygame.K_1:
                    escolhaJogador = "Pedra"
                    jogou = True
                elif event.key == pygame.K_2:
                    escolhaJogador = "Papel"
                    jogou = True
                elif event.key == pygame.K_3:
                    escolhaJogador = "Tesoura"
                    jogou = True
                    
                # Se você jogou, o computador escolhe um e o jogo calcula o resultado
                if jogou:
                    escolhaComputador = random.choice(opcoes)
                    exibirJogador = escolhaJogador
                    exibirNatsuki = escolhaComputador
                    # Regras para ver quem ganhou
                    if escolhaJogador == escolhaComputador:
                        texto_resultado = "Empate!"
                        cenaAtiva = 6
                        indiceDialogo = 0
                    if (escolhaJogador == "Pedra" and escolhaComputador == "Tesoura") or \
                        (escolhaJogador == "Papel" and escolhaComputador == "Pedra") or \
                        (escolhaJogador == "Tesoura" and escolhaComputador == "Papel"):
                        texto_resultado = "Você Ganhou!"
                        cenaAtiva = 8
                        indiceDialogo = 0
                    else:
                        texto_resultado = "Você Perdeu!"
                        cenaAtiva = 6
                        indiceDialogo = 0

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # Avança a história com o clique esquerdo do mouse
            avancarNaHistoria = True
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            #y-= velocidade
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            #caixa_y = caixa_y - 1500
#Programa para executar comandos do mouse com o primero diálogo  fim

#Programa para executar comandos do teclado inicio
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        # Também avança com a barra de espaço
            avancarNaHistoria = True
#Programa para executar comandos do teclado fim

        if avancarNaHistoria:
            #Caso existam falas na cena atual, avança o indice
            if indiceDialogo < len(listaAtual) - 1:
                indiceDialogo += 1
            else:
                #Se a cena acabou mude para a próxima
                if cenaAtiva == 1:
                    cenaAtiva = 2
                    indiceDialogo = 0
                if cenaAtiva == 3:
                    cenaAtiva = 2
                    indiceDialogo = 1
                if cenaAtiva == 6:
                    tocar_musica("TrilhaSonoraUm.mp3")
                    cenaAtiva = 2
                    indiceDialogo = 1
                if cenaAtiva == 8:
                    tocar_musica("TrilhaSonoraUm.mp3")
                    cenaAtiva = 2
                    indiceDialogo = 1
                if cenaAtiva == 4 or cenaAtiva == 7:
                    cenaAtiva = 5
                    indiceDialogo = 0
                if cenaAtiva == 12 or cenaAtiva == 13:
                    cenaAtiva = 11
                    indiceDialogo = 0
                else:
                #Se as cenas acabaram, encerre o jogo
                    #janela_aberta = False
                        #Detectando o clique no botão inicio
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # Clique esquerdo do mouse
                            if botaoChamov.collidepoint(posicaoMouse):
                                if falouComOChamov == False:
                                    somBotaoSelecionado.play()
                                    falouComOChamov = True
                                    indiceDialogo = 0
                                    cenaAtiva = 3
                                else:
                                    botaoChamov.topleft = (3000, 3000)
                            if botaoSetaUm.collidepoint(posicaoMouse):
                                if ganhouDaNatsuki == False and falouComANatsuki == False:
                                    somBotaoSelecionado.play()
                                    botaoChamov.topleft = (3000, 3000)
                                    botaoSetaUm.topleft = (3000, 3000)
                                    botaoSetaDois.topleft = (3000, 3000)
                                    indiceDialogo = 0
                                    cenaAtiva = 4
                                elif ganhouDaNatsuki == False and falouComANatsuki == True:
                                    somBotaoSelecionado.play()
                                    botaoChamov.topleft = (3000, 3000)
                                    botaoSetaUm.topleft = (3000, 3000)
                                    botaoSetaDois.topleft = (3000, 3000)
                                    indiceDialogo = 0
                                    cenaAtiva = 7
                            if botaoSetaDois.collidepoint(posicaoMouse):
                                somBotaoSelecionado.play()
                                botaoChamov.topleft = (3000, 3000)
                                botaoSetaUm.topleft = (3000, 3000)
                                botaoSetaDois.topleft = (3000, 3000)
                                indiceDialogo = 0
                                cenaAtiva = 9
                            if botaoSetaTres.collidepoint(posicaoMouse):
                                somBotaoSelecionado.play()
                                botaoChamov.topleft = (60, 350)
                                botaoSetaUm.topleft = (1050, 250)
                                botaoSetaDois.topleft = (750, 175)
                                botaoSetaQuatro.topleft = (3000, 3000)
                                indiceDialogo = 1
                                cenaAtiva = 2
                            if botaoSetaQuatro.collidepoint(posicaoMouse):
                                somBotaoSelecionado.play()
                                botaoSetaTres.topleft = (3000, 3000)
                                botaoSetaQuatro.topleft = (3000, 3000)
                                indiceDialogo = 0
                                cenaAtiva = 10
                            if botaoSetaCinco.collidepoint(posicaoMouse):
                                somBotaoSelecionado.play()
                                botaoSetaCinco.topleft = (3000, 3000)
                                botaoSetaSeis.topleft = (3000, 3000)
                                botaoSetaSete.topleft = (3000, 3000)
                                indiceDialogo = 0
                                cenaAtiva = 9
                            if botaoSetaSeis.collidepoint(posicaoMouse):
                                if (ganhouDaNatsuki == True) and (falouComASayoriEYuri == True) and (falouComOChamov == False):
                                    somBotaoSelecionado.play()
                                    botaoSetaCinco.topleft = (3000, 3000)
                                    botaoSetaSeis.topleft = (3000, 3000)
                                    botaoSetaSete.topleft = (3000, 3000)
                                    indiceDialogo = 0
                                    cenaAtiva = 16
                                elif (ganhouDaNatsuki == True) and (falouComASayoriEYuri == True) and (falouComOChamov == True):
                                    somBotaoSelecionado.play()
                                    botaoSetaCinco.topleft = (3000, 3000)
                                    botaoSetaSeis.topleft = (3000, 3000)
                                    botaoSetaSete.topleft = (3000, 3000)
                                    indiceDialogo = 0
                                    cenaAtiva = 18
                                else:
                                    somBotaoSelecionado.play()
                                    botaoSetaCinco.topleft = (3000, 3000)
                                    botaoSetaSeis.topleft = (3000, 3000)
                                    botaoSetaSete.topleft = (3000, 3000)
                                    indiceDialogo = 0
                                    cenaAtiva = 14
                            if botaoSetaSete.collidepoint(posicaoMouse):
                                somBotaoSelecionado.play()
                                botaoSetaCinco.topleft = (3000, 3000)
                                botaoSetaSeis.topleft = (3000, 3000)
                                botaoSetaSete.topleft = (3000, 3000)
                                indiceDialogo = 0
                                cenaAtiva = 11
                            if botaoSetaOito.collidepoint(posicaoMouse):
                                somBotaoSelecionado.play()
                                botaoSetaOito.topleft = (3000, 3000)
                                botaoSayoriEYuri.topleft = (3000, 3000)
                                indiceDialogo = 0
                                cenaAtiva = 10
                            if botaoSayoriEYuri.collidepoint(posicaoMouse):
                                somBotaoSelecionado.play()
                                if falouComASayoriEYuri == False:
                                    falouComASayoriEYuri = True
                                    indiceDialogo = 0
                                    cenaAtiva = 12
                                else:
                                    indiceDialogo = 0
                                    cenaAtiva = 13
                                
                    # Aqui você pode chamar a função que inicia o jogo ou muda de tela
                    #Detectando o clique no botão fim

#Programa para personagem sumir quando chegar no final da tela inicio
    if (posicao_x_Meme <= -3000):
        posicao_x_Meme = -5000
#Programa para personagem sumir quando chegar no final da tela fim

#Programa de desenho inicio
    #pygame.draw.circle(janela, (0,255,0), (x,y), 50)
#Programa de desenho fim

    # Atualiza a tela
    pygame.display.flip()
    rodaFrames.tick(60) # Mantém o jogo a 60 Frames por Segundo

pygame.quit()