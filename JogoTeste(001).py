# Descricao: Meu primeiro jogo a ser desenvolvido na linguagem Python. Estou muito feliz:
# Sobre o Jogo: Born to die - Uma tartaruga marinha inicia a primeira e pior trajetória em sua vida:
# Chegar ao mar aberto antes de ser devorada.
# Status do Projeto: Em andamento.
# É possível movimentar - se livremente na área estática do game.
# Será preciso definir limite de movimento para o personagem jogável.
# Ainda é preciso calcular e inserir o registro de danos sofridos e lançar uma resposta ao usário
# em uma barra de HP.
# Estabelecer o sistema de reinício da partida após a morte e resetar os inimigos e progresso do jogo.
# Contabilizar o valor a ser obtido para finalizar o game.
# Obs: O projeto criado faz parte de um rascunho para um jogo principal, ainda sendo desenvolvido
# por enquanto em um roteiro.
# Dia 1:
import pygame
from random import randint

#A biblioteca acima random randint foi adicionada para
#que os inimigos aparecam aleatoriamente.

pygame.init()
x = 664
y = 300
pos_x = 420
pos_y = 0
pos_xuca = 100
pos_yuca = 0
pos_xat  = 710
pos_yat  = 0
pos_xreal = 500
pos_yreal = 0
velocidade = 30
velreiv = 17
veluca  = 3
velat   = 12
velreal = 7

# Velocidade define quantos pixels nossa figura ira percorrer quando ordenarmos seu movimento,
# seja para o lado, baixo cima etc.

fundo = pygame.image.load('Cenario.png')
tartaruga = pygame.image.load('tart2.png')
reiv = pygame.image.load('reiv.png')
uca = pygame.image.load('uca.png')
at = pygame.image.load('at.png')
real = pygame.image.load('real.png')

# Os comandos acima inserem
# os cenarios e personagem jogavel no jogo.
# Precisam ter o mesmo nome aqui e na pasta.

janela = pygame.display.set_mode((1328,576))
# No comando acima definimos o tamanho do jogo na tela,
# aqui, com essa linha de comando, ao executar, a tela aparece e some rapidamente.
pygame.display.set_caption('Jogo 1 do Python')
# No comando digitado dou ordem ao sistema para escrever
# o nome do jogo na barra superior da tela do mesmo ao rodar.

janela_aberta = True
# Comando boleano para que o comando de janela aberta no jogo seja verdade, para nao fechar em seguida.
# Abaixo temos um comando em while que permitira a janela aberta,
# com comando de quit (clicando no x na tela), para ter opcao de fechar o jogo.
while janela_aberta :
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade

#Abaixo definimos uma condicao para que os objetos
#deem respawn no jogo, sempre aparecendo na tela.
    if (pos_y > 582):
        pos_y = 0
        pos_x = randint(0,1328)
# Abaixo vamos definir a velocidade dos inimigos e
# padrao de movimento.
    pos_y += velreiv
    if (pos_yuca > 582):
        pos_yuca = 0
        pos_xuca = randint(0,1328)
    pos_yuca += veluca
    if (pos_yat > 582):
        pos_yat = 0
        pos_xat = randint(0,1328)
    pos_yat += velat
    if (pos_yreal > 582):
        pos_yreal = 0
        pos_xreal = randint(0,1328)
    pos_yreal += velreal

#Abaixo vamos alterar a janela.fill para
# janela.blit para alterar a imagem de fundo do jogo.
    janela.blit(fundo,(0,0))
# Acima definimos os comandos de movimentos e na ultima linha (janela.fill(()) definimos que a imagem
# nao deixara um borrao de cores para tras ao se movimentar.
# Lembrete: Para o objeto ter movimento continuo ao pressionar um botao,
# todas as ordems devem estar fora da indetacao de if event.time senao o comando so movimenta
# pressionando uma vez por aperto de botao.
# Abaixo vamos definir as propriedades do objeto principal, formato(draw.circle), cores (0,255,0)
# e dimensoes na tela (400,300) 50 de diametro.

    janela.blit(tartaruga,(x,y))
#Acima alteramos no segundo dia de trabalho o formato.
#de circulo para tartaruguinha.
#De pygame.draw.circle(janela, (0,255,0),(x,y),50)
#mudamos para janela.blit(tartaruga,(x,y))
    janela.blit(reiv,(pos_x,pos_y))
    janela.blit(uca,(pos_xuca,pos_yuca))
    janela.blit(at,(pos_xat,pos_yat))
    janela.blit(real,(pos_xreal,pos_yreal))
    pygame.display.update()
pygame.quit()
