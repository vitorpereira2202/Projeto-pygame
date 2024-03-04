from cores import *
import pygame
import random

pygame.init()

largura_tela, altura_tela = (800, 600)
tela = pygame.display.set_mode((largura_tela, altura_tela))
nome = pygame.display.set_caption('FAZ O QUADRADIN, E JOGA DE LADIN')

def cria_quadrados (n, larg, alt, espaco) : 
    if n <= 0 :
        return []
    
    cores = [(rosa), (verde), (amarelo), (azul), (magenta), (vermelho), (laranja), (roxo)]
    cores *= 2
    
    
    random.shuffle(cores)

    lista_quadrados = []
    cores_use = {}
    cor_sorteada = None
   

    for i in range(n) :
        for f in range(n) :
            x = (largura_tela - larg * n - espaco * (n - 1)) // 2 + f * (larg + espaco)
            y = (altura_tela - alt * n - espaco * (n - 1)) // 2.1 + i * (alt + espaco)
            cor_sorteada = None
            while True :
                cor_sorteada = random.choice(cores)
                if cor_sorteada in cores_use and cores_use[cor_sorteada] < 2:
                    cores_use[cor_sorteada] += 1
                    break
                elif cor_sorteada not in cores_use :
                    cores_use[cor_sorteada] = 1
                    break
            par = {'cor': branco, 'cor_sorteada': cor_sorteada, 'rect': pygame.Rect(x, y, larg, alt)}
            lista_quadrados.append(par)
    return lista_quadrados

def desenha_quadrados (tela, jogo) :
    for par in jogo :
        cor = par['cor']
        rect = par['rect']
        pygame.draw.rect(tela, cor, rect)

def verifica_clique (posicao, jogo) :
    for par in jogo :
        rect = par['rect']
        if rect.collidepoint(posicao) :
            if par['cor'] == branco :
                par['cor'] = par['cor_sorteada']
            else :
                par['cor'] = branco

larg_quadrado = 60
altura_quadrado = 60
n = 4
espaco_quadrados = 10

jogo = cria_quadrados(n, larg_quadrado, altura_quadrado, espaco_quadrados)

largura_tela = larg_quadrado * n
altura_tela = altura_quadrado * n

game = True
while game :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                pos_mouse = pygame.mouse.get_pos()
                verifica_clique(pos_mouse, jogo)
        

    
    tela.fill(preto)
    desenha_quadrados(tela, jogo)

    pygame.display.update()
