#Biblioteca fasd
import pygame
from pygame.locals import *
from sys import exit
from random import randint
#Inicializar todas as funcoes e bibliotecas do pygame
pygame.init()
#Criando tela#####################################################
largura=640;altura=480
x=largura/2;y=altura/2 #controle do movimento do retangulo
x_food=randint(40,600);y_food=randint(50,430) #posicao aleatoria da comida
relogio=pygame.time.Clock() #velocidade do jogo via 'frames'
tela=pygame.display.set_mode((largura,altura))#(largura,altura)
fonte=pygame.font.SysFont('arial',35,True,False)#Texto com o placar
pontos=0
#Titulo da tela
pygame.display.set_caption("Snake Game")
#Icone do jogo
img=pygame.image.load('Extra/Snake_ico_removebg.png')##
pygame.display.set_icon(img)
#Loop principal do jogo##########################################
while True:
    #Loop de checagem dos eventos
    for event in pygame.event.get():
        relogio.tick(100)#velocidade do jogo via 'frames'
        tela.fill((0, 0, 0))  # "limpando" a tela para o retangulo andar
        mensagem=f"Point: {pontos}" #placar
        texto_formatado=fonte.render(mensagem,True,(255,255,255))#true=nao pixelado
        #Fechar janela
        if event.type==QUIT:
            pygame.quit()
            exit()
        '''
        #Reconhecendo ações do teclado (estatico)
        if event.type==KEYDOWN:
            if event.key==K_a or event.key==K_LEFT:#if 'a' go to left
                x=x-20
            if event.key==K_d or event.key==K_RIGHT:#if 'd', go to right
                x=x+20
            if event.key==K_w or event.key==K_UP:#if 'w', go up
                y=y-20
            if event.key==K_s or event.key==K_DOWN:#if 's', go down
                y=y+20 '''
        #Reconhecendo ações do teclado (pressionado)
        if pygame.key.get_pressed()[K_a]:#if 'a' go to left
            x=x-20
        if pygame.key.get_pressed()[K_d]:#if 'd', go to right
            x=x+20
        if pygame.key.get_pressed()[K_w]:#if 'w', go up
            y=y-20
        if pygame.key.get_pressed()[K_s]:#if 's', go down
            y=y+20
        #Desenhando os objetos
        ##Retangulo
        snake=pygame.draw.rect(tela,(232,36,36),(x,y,40,40)) #local,(cor),(posicao,largura,altura)
        ###Circulo
        food=pygame.draw.circle(tela,(42,72,223),(x_food,y_food),20) #local,(cor),(posicao,posicao),radio)
        ###Linha
        #pygame.draw.line(tela,(223,211,42),(390,0),(390,600),1)#local,(cor),(inicio,fim x),(inicio,fim y),espessura
        #Eat the food
        if snake.colliderect(food):
            x_food=randint(40,600);y_food=randint(50,430) #posicao aleatoria da comida
            pontos=pontos+1 #se comer, ganha pontos
    #imprimindo o placar
    tela.blit(texto_formatado,(400,15))
    #Atualizar a tela a cada loop principal
    pygame.display.update()
