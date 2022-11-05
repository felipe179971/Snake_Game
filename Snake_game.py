#Biblioteca fasd
import pygame
from pygame.locals import *
from sys import exit
#Inicializar todas as funcoes e bibliotecas do pygame
pygame.init()
#Criando tela#####################################################
largura=640;altura=480
x=largura/2;y=0 #controle do movimento do retangulo
relogio=pygame.time.Clock() #velocidade do jogo via 'frames'
tela=pygame.display.set_mode((largura,altura))#(largura,altura)
#Titulo da tela
pygame.display.set_caption("Snake Game")
#Icone do jogo
img=pygame.image.load('Extra/Snake_ico.png')
pygame.display.set_icon(img)
#Loop principal do jogo##########################################
while True:
    #Loop de checagem dos eventos
    for event in pygame.event.get():
        relogio.tick(100)#velocidade do jogo via 'frames'
        tela.fill((0, 0, 0))  # "limpando" a tela para o retangulo andar
        #Fechar janela
        if event.type==QUIT:
            pygame.quit()
            exit()
        #Desenhando os objetos
        ##Retangulo
        pygame.draw.rect(tela,(232,36,36),(x,y,40,50)) #local,(cor),(posicao,largura,altura)
        if y>=altura:
            y=0
        y=y+1
        ###Circulo
        #pygame.draw.circle(tela,(42,72,223),(300,260),40) #local,(cor),(posicao,posicao),radio)
        ###Linha
        #pygame.draw.line(tela,(223,211,42),(390,0),(390,600),1)#local,(cor),(inicio,fim x),(inicio,fim y),espessura
    #Atualizar a tela a cada loop principal
    pygame.display.update()
