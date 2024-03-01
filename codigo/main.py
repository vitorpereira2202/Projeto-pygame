from cores import *
import pygame
import random

pygame.init()

largura, altura = (800, 600)
tela = pygame.display.set_mode((largura, altura))
nome = pygame.display.set_caption('FAZ O QUADRADIN, E JOGA DE LADIN')



game = True
while game :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            quit()
        


    tela.fill(preto)

    pygame.display.update()