from cores import *
import pygame
import random

class Tela_jogo :

    pygame.init()

    def inicializa (self) :
        self.largura_tela, self.altura_tela = (800, 600)
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        self.nome = pygame.display.set_caption('FAZ O QUADRADIN, E JOGA DE LADIN')
        self.som_errou = pygame.mixer.Sound('codigo/sons/nice-meme.wav')
        self.som_acertou = pygame.mixer.Sound('codigo/sons/oof-sound-effect-hd-homemadesoundeffects.wav')
        pygame.font.init()
        self.fonte_segundos = pygame.font.Font(None, 40)
        self.tempo = pygame.time.get_ticks()
        self.assets = {'errou' : False, 'contador' : 0}
        self.n =4
        self.larg_quadrado = 60
        self.altura_quadrado = 60
        self.espaco_quadrados = 10
        self.jogo = tela_jogo.cria_quadrados(self.n, self.larg_quadrado, self.altura_quadrado, self.espaco_quadrados)
    


        return self.tela

    

    def cria_quadrados (self,n, larg, alt, espaco) : 
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
                x = (self.largura_tela - larg * n - espaco * (n - 1)) // 2 + f * (larg + espaco)
                y = (self.altura_tela - alt * n - espaco * (n - 1)) // 2.1 + i * (alt + espaco)
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


    def eventos (self) :
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN :
                if self.assets['errou'] == False :
                    if event.button == 1:
                        pos_mouse = pygame.mouse.get_pos()
                        self.verifica_clique(pos_mouse, self.jogo, self.assets)
        return True





    def desenha_quadrados (self, tela, jogo) :
        for par in jogo :
            cor = par['cor']
            rect = par['rect']
            pygame.draw.rect(tela, cor, rect)

    def verifica_clique (self, posicao, jogo, assets) :
        for par in jogo :
            rect = par['rect']
            if rect.collidepoint(posicao) :
                if par['cor'] == branco :
                    par['cor'] = par['cor_sorteada']
                else :
                    par['cor'] = branco
                quadrados_usados = [quad for quad in jogo if quad['cor'] != branco]
                if len(quadrados_usados) == 2 :
                    if quadrados_usados[0]['cor_sorteada'] == quadrados_usados[1]['cor_sorteada'] :
                        jogo.remove(quadrados_usados[0])
                        jogo.remove(quadrados_usados[1])
                        self.som_errou.play()
                    else :
                        self.assets['errou'] = True
                        self.assets['contador'] = 1000
                        self.som_acertou.play()
    

    def reinicia_quadrados (self, assets, jogo) :
        if self.assets['errou'] == True :
            self.assets['contador'] -= 1
            if self.assets['contador'] == 0 :
                self.assets['errou'] = False
                for par in jogo :
                    par['cor'] = branco
    
    def desenha (self) :
        self.tempo_atual = pygame.time.get_ticks()
        self.tela.fill(preto)
        self.reinicia_quadrados(self.assets, self.jogo)
        self.desenha_quadrados(self.tela, self.jogo)
        tempo_final = (self.tempo_atual - self.tempo) // 1000
        texto_segundos = self.fonte_segundos.render(f'Tempo: {tempo_final}', True, branco)
        self.tela.blit(texto_segundos, (10, 10))
        pygame.display.update()



    




tela_jogo = Tela_jogo()
tela_jogo.inicializa()



largura_tela = tela_jogo.larg_quadrado * tela_jogo.n
altura_tela = tela_jogo.altura_quadrado * tela_jogo.n

game = True

while game :
    game = tela_jogo.eventos()
   
        
        
    tela_jogo.desenha()
    if not tela_jogo.jogo :
        game = False