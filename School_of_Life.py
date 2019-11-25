
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:10:01 2019

@author: RafaelzZ
"""

#A classe aparenta estar dando certo


#import imageio
import os
import pygame
import json
#import time
#import sys
#import winsound
import random

tbt = 35

#path = "D:\Training\Making_Gifs\Images"

font_name = pygame.font.match_font('arial')

#def carrega_texto(text, size, x, y , frequency, duration, cenario)

#Aqui sera designado os atributos diferenciativos
forca = 0
intel = 0
caris = 0

atributos = [forca, intel, caris]


RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (0,0,0)
BLACK = (255,255,255)
def draw_text(surf, text, size, x, y, frequency, duration, cor):
#    i = 0
    for letras in text:
#        sys.stdout.write(letras)
#        sys.stdout.flush()
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(letras, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.midtop =  (x,y)
        surf.blit(text_surface, text_rect)
        #winsound.PlaySound("footstep_2", winsound.SND_FILENAME)
        x = x + 8
        y = y
        
def draw_number(surf, number, size, x, y, frequency, duration, cor):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(str(number), True, cor)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
#img_dir  = os.path.join(os.path.dirname(__file__), 'Images')

#Treinando como se abre arquivos
batman = os.listdir('Images')

#print(batman)
#print('abcdef'.endswith('def'))

# função que zera todas as variaveis ao ser chamda com True (utilizada para reiniciar o jogo)
# função que chama o jogo da cobrinha e quando acaba volta o funcionamento normal do jogo

lista = []
lis_capa = []
lis_0butão = []
lis_pause = []
lis_texto = []
lis_dois = []
lis_três = []
lis_total = []
lis_paused = []
lis_random = []
for nomes in batman:
    if nomes.endswith('png'):
        lista.append(nomes)
    if nomes.startswith('capa'):
        lis_capa.append(nomes)
    if nomes.startswith('sem'):
        lis_0butão.append(nomes)
    if nomes.startswith('pause'):
        lis_pause.append(nomes)
    if nomes.startswith('txt'):
        lis_texto.append(nomes)
    if nomes.startswith('2'):
        lis_dois.append(nomes)                  
    if nomes.startswith('3'):
        lis_três.append(nomes)
    if nomes.startswith('paused'):
        lis_paused.append(nomes)
    if nomes.startswith('random'):
        lis_random.append(nomes)
    
    if nomes not in lis_capa and nomes not in lis_paused:
        lis_total.append(nomes)
#print(lista)
#print(lista_2)
#print(lista_3)
print(lis_capa)
print(lis_total)

WIDTH = 888
HEIGHT = 505
HEIGHT_2 = 120
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
img_str  = os.path.join(os.path.dirname(__file__), 'Images')

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New_Game")
clock = pygame.time.Clock()
img_dir = os.path.join(os.path.dirname(__file__), 'Images')
print(img_dir)

#for arquivos in img_dir:
#    print(arquivos)

all_sprites = pygame.sprite.Group()
    
#Abrindo o arquivo json que depois será utilizado no jogo

#Está acontecendo algum problema na hora de processar o arquivo json e abrí-lo
with open ("My_Json.json") as file:
    arquivo_json = json.load(file)
#    print("batata")
    
    
lista_forca = []
lista_intel = []
lista_caris = []

for cenas in arquivo_json:
    if cenas.startswith("Acad"):
        lista_forca.append(cenas)
    elif cenas.startswith("Est"):
        lista_intel.append(cenas)
    elif cenas.startswith("Pas"):
        lista_caris.append(cenas)
        
    


# Acho que a classe está correta, agora só falta ativala
# O problema é como fazer isso, talvez primeiro deve-se procurar qual o group a qual ela pertence
class Botão(pygame.sprite.Sprite):
    def __init__(self, valor_3, valor_4, H, W, Alteracao_1, Alteracao_2, imagem):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        botão = pygame.image.load(os.path.join(img_str, imagem)).convert()
        self.image = botão
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(botão, (valor_3, valor_4))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = W/Alteracao_1
        self.rect.bottom = H - Alteracao_2
        print(self.rect)
        
        
#class Caixa_Texto(pygame.sprite.Sprite):
#    def __init__(self, val):
#        
#        #Construtor de classe pai (Sprite)
#        pygame.sprite.Sprite.__init__(self)
#        
#        #Carregando a imagem de fundo
#        caixa_texto = pygame.image.load(os.path.join(img_str, "text.png"))
#        self.image = caixa_texto
#        
#        #Diminuindo o tamanho da imagem
#        self.image = pygame.transform.scale(caixa_texto, ( valor_3, valor_4))

botão_teste = Botão(tbt,tbt,HEIGHT,WIDTH,1.18,5,"botão.png")
botão_teste_2 = Botão(tbt,tbt,HEIGHT,WIDTH,1.18,45,"botão.png")
botão_teste_3 = Botão(tbt,tbt,HEIGHT,WIDTH,1.18,85,"botão.png")

botão_teste_4 = Botão(tbt,tbt,HEIGHT,WIDTH,1.35,35,"botão.png")
botão_teste_5 = Botão(tbt,tbt,HEIGHT,WIDTH,6,35,"botão.png")

caixa_texto = Botão(WIDTH,125,HEIGHT,WIDTH,2,0,"text.png")
botão_pause = Botão(tbt,tbt,HEIGHT,WIDTH,48,462,"Pause2.png")

back_to_game = Botão(150, 85, 150, 450, 1, 0, "paused_Back_to_Game.png")
creditos = Botão(200, 35, 500, 100, 1, 0, "paused_Credits.png")
nome_do_jogo = Botão(75, 35, 35, 35, 1, 0, "paused_Nome_do_Jogo.png")
restart_game = Botão(150, 85, 250, 450, 1, 0, "paused_Restart_Game.png")
slav_bros = Botão(75, 35, 35, 850, 1, 0, "paused_Slav_Bros.png")

rect_3 = pygame.Rect((735,465),(tbt,tbt))
rect_2 = pygame.Rect((735,425),(tbt,tbt))
rect_1 = pygame.Rect((735,385),(tbt,tbt))

rect_5 = pygame.Rect((640,435),(tbt,tbt))
rect_4 = pygame.Rect((131,435),(tbt,tbt))

rect_pause = pygame.Rect((1,8),(tbt,tbt))
#print(rect_pause)

back_to_game_rect = pygame.Rect((375,67),(150,85))
creditos_rect = pygame.Rect((0,465),(200,35))
nome_do_jogo_rect = pygame.Rect((-2,0),(75,35))
restart_game_rect = pygame.Rect((375, 165), (150,85))
slav_bros_rect = pygame.Rect((813,0),(75,36))

um_botão = pygame.sprite.Group()
dois_botões = pygame.sprite.Group()
três_botões = pygame.sprite.Group()

desenho_caixa = pygame.sprite.Group()
pause = pygame.sprite.Group()
menu_pause = pygame.sprite.Group()

um_botão.add(botão_teste)
dois_botões.add(botão_teste_4, botão_teste_5)
três_botões.add(botão_teste, botão_teste_2, botão_teste_3)
desenho_caixa.add(caixa_texto)
pause.add(botão_pause)
menu_pause.add(back_to_game, creditos, nome_do_jogo,  restart_game, slav_bros)




screen.fill(WHITE)

caminho_2_sortido = ["caminho_1", "caminho_2"]
caminho_3_sortido = ["caminho_1", "caminho_2", "caminho_3"]

imagens_dic = {}
for imagens in lista:
    load = pygame.image.load(os.path.join(imagens)).convert()
    imagens_dic[imagens] = load
    
#print(imagens_dic)

cenario = "Inicio"
#cenario_atual = ""
cenario_anterior = ""
cenario_antes_pause = ""
text = ""
indice_texto = 0
indice_texto_2 = 0
indice_texto_3 = 0
indice_texto_4 = 0
#contador_clicks = 0
lista_positioning = []
#print(assets)

contador = 0
soma = 0
game_loop = True
while game_loop == True:
    cenario_anterior = cenario
    
    
    atributos = [forca, intel, caris]
    
    if arquivo_json[cenario]["imagem"] == "capa2.png":
        forca = 0
        intel = 0
        caris = 0
    
#    i = 0
#    while i < 2:
#        print(i)
#        i = i + 1
    
    #Problemas no backgame
    
#    cenario_antes = arquivo_json[cenario]["cenario_anterior"]
#    print(cenario_antes)
#    print(rect)
#    pygame.draw.rect(screen, BLACK, ())
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
#        print(pygame.mouse.get_pressed())
#        if cenario["imagem"] in lis_capa:
#            if pygame.mouse.get_pressed() == (1,0,0):
#                cenario = arquivo_json[cenario]["caminho_unico"]

        if arquivo_json[cenario]["imagem"] in lis_capa:
            if pygame.mouse.get_pressed() == (1,0,0):
                cenario = arquivo_json[cenario]["caminho_unico"]
                
        if arquivo_json[cenario]["imagem"] in lis_texto:
            if pygame.mouse.get_pressed() == (1,0,0):
                cenario = arquivo_json[cenario]["caminho_unico"]
    
        if arquivo_json[cenario]["imagem"] == "Prova2.png":
            if pygame.mouse.get_pressed() == (1,0,0):
                if arquivo_json[cenario]["imagem"] == "Prova2.png":
                    if intel <= 2 or forca < 2:
                        cenario = arquivo_json[cenario]["caminho_1"]
                    elif intel > 2 and forca > 2:
                        cenario = arquivo_json[cenario]["caminho_2"]
                    elif intel > 4 and forca > 2:
                        cenario = arquivo_json[cenario]["caminho_3"]
                        
        if arquivo_json[cenario]["imagem"] in lis_random:
                sorteio = random.choice(caminho_3_sortido)
                print(sorteio)
                cenario = arquivo_json[cenario][sorteio]
                
        if arquivo_json[cenario]["imagem"] in lis_dois:
            if pygame.mouse.get_pressed() == (1,0,0):
#                print(pygame.mouse.get_pos())
                if rect_4.collidepoint(pygame.mouse.get_pos()):
                    if arquivo_json[cenario]["caminho_1"] in lista_intel:
                        intel = intel + 1
                        if forca > 0:
                            forca = forca - 1
                    cenario = arquivo_json[cenario]["caminho_1"]
                elif rect_5.collidepoint(pygame.mouse.get_pos()):
                    cenario = arquivo_json[cenario]["caminho_2"]
                
        if arquivo_json[cenario]["imagem"] in lis_três:
            if pygame.mouse.get_pressed() == (1,0,0):
#                print(pygame.mouse.get_pos())
                if rect_1.collidepoint(pygame.mouse.get_pos()):
                    if arquivo_json[cenario]["caminho_1"] in lista_forca:
                        forca = forca + 1
                    cenario = arquivo_json[cenario]["caminho_1"]
#                    print("Abacate")
                elif rect_2.collidepoint(pygame.mouse.get_pos()):
                    if arquivo_json[cenario]["caminho_2"] in lista_intel:
                        intel = intel + 2
                    cenario = arquivo_json[cenario]["caminho_2"]
#                    print("Feijão")
                elif rect_3.collidepoint(pygame.mouse.get_pos()):
                    if arquivo_json[cenario]["caminho_3"] in lista_caris:
                        caris = caris + 1
                    cenario = arquivo_json[cenario]["caminho_3"]
#                    print("Arroz")
    #            print("Bazinga!")
        if arquivo_json[cenario]["imagem"] in lis_total:
            if pygame.mouse.get_pressed() == (1,0,0):
                if rect_pause.collidepoint(pygame.mouse.get_pos()):
                    cenario_antes_pause = cenario
                    cenario = arquivo_json[cenario]["pause"]
                
        
        if arquivo_json[cenario]["imagem"] == "paused_menu_teste.png":
            if pygame.mouse.get_pressed() == (1,0,0):
                if restart_game_rect.collidepoint(pygame.mouse.get_pos()):
                    cenario = arquivo_json[cenario]["restart_game"]
                if back_to_game_rect.collidepoint(pygame.mouse.get_pos()):
                    print(cenario_antes_pause)
                    cenario = cenario_antes_pause
#                    cenario = arquivo_json[cenario_anterior]["imagem"]
                print(pygame.mouse.get_pos())
        
                    
        if event.type == pygame.QUIT:
            game_loop = False
    print(cenario_antes_pause)        
    imagem_fundo = arquivo_json[cenario]["imagem"]
#    print(imagem_fundo)
#    print(type(imagem_fundo))
#    background = pygame.image.load(os.path.join(imagem_fundo)).convert()
    background = imagens_dic[imagem_fundo]
    background_rect = background.get_rect()      
    reindera_imagem = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
#    all_sprites.update()
    screen.blit(reindera_imagem, background_rect)
    if imagem_fundo in lis_texto:
        desenho_caixa.draw(screen)
        pause.draw(screen)
    if imagem_fundo in lis_pause:
        pause.draw(screen)
    if imagem_fundo in lis_dois:
        desenho_caixa.draw(screen)
        dois_botões.draw(screen)
        pause.draw(screen)
    if imagem_fundo in lis_três:
        desenho_caixa.draw(screen)
        três_botões.draw(screen)
        pause.draw(screen)
    if imagem_fundo in lis_paused:
        menu_pause.draw(screen)

    titulo = arquivo_json[cenario]["titulo"]
    text = arquivo_json[cenario]["descricao"]
    text_2 = arquivo_json[cenario]["descricao_2"]
    text_3 = arquivo_json[cenario]["descricao_3"]
    text_4 = arquivo_json[cenario]["descricao_4"]
    
    
    caracteres_especiais = "! @ # $ _ +"
    print(caracteres_especiais)
    filtro = caracteres_especiais.split()
    print(filtro)
    
    if arquivo_json[cenario]["imagem"] in lis_três:
        caminho_1 = arquivo_json[cenario]["caminho_1"]
        print(type(caminho_1))
        caminho_2 = arquivo_json[cenario]["caminho_2"]
        caminho_3 = arquivo_json[cenario]["caminho_3"]
        for caracter in caminho_1:
            if caracter in filtro:
                caminho_1_filtrado = caminho_1.replace("_", " ")
            else:
                caminho_1_filtrado = caminho_1
        for caracter in caminho_2:
            if caracter in filtro:
                caminho_2_filtrado = caminho_2.replace("_", " ")
            else:
                caminho_2_filtrado = caminho_2
        for caracter in caminho_3:
            if caracter in filtro:
                caminho_3_filtrado = caminho_3.replace("_", " ")
            else:
                caminho_3_filtrado = caminho_3

#        print(caminho_1_filtrado)
#        print(caminho_2_filtrado)
#        print(caminho_3_filtrado)
        
    if arquivo_json[cenario]["imagem"] in lis_dois:
        caminho_1 = arquivo_json[cenario]["caminho_1"]
        caminho_2 = arquivo_json[cenario]["caminho_2"]
            
        for caracter in caminho_1:
            if caracter in filtro:
                caminho_1_filtrado = caminho_1.replace("_", " ")
            else:
                caminho_1_filtrado = caminho_1
        for caracter in caminho_2:
            if caracter in filtro:
                caminho_2_filtrado = caminho_2.replace("_", " ")
            else:
                caminho_2_filtrado = caminho_2.replace("_", " ")
        
#        print(caminho_1_filtrado)
#        print(caminho_2_filtrado)
        
    indice_texto += 1
    indice_texto_2 += 1
    indice_texto_3 += 1
    indice_texto_4 += 1
    
    tamanho_1 = len(text)
    tamanho_2 = len(text_2)
    tamanho_3 = len(text_3)
    tamanho_4 = len(text_4)
    
    tamanhos = [tamanho_1, tamanho_2, tamanho_3, tamanho_4]
    if indice_texto > max(tamanhos):
        indice_texto = len(text)
        indice_texto_2 = len(text_2)
        indice_texto_3 = len(text_3)
        indice_texto_4 = len(text_4)
    if cenario != cenario_anterior:
        indice_texto = 0
        indice_texto_2 = 0
        indice_texto_3 = 0
        indice_texto_4 = 0
    
    if arquivo_json[cenario]["imagem"] in lis_três:
        draw_text(screen,caminho_1_filtrado,18, 777, 395, 200, 300, BLACK)
        draw_text(screen,caminho_2_filtrado,18, 777, 430, 200, 300, BLACK)
        draw_text(screen,caminho_3_filtrado,18, 777, 470, 200, 300, BLACK)
        
    if arquivo_json[cenario]["imagem"] in lis_dois:
        draw_text(screen,caminho_1_filtrado,18, 171, 440, 200, 300, BLACK)
        draw_text(screen,caminho_2_filtrado,18, 683, 440, 200, 300, BLACK)
    
    draw_text(screen,titulo,18,WIDTH/2 - 80, HEIGHT/2 - 250 , 200, 300, RED)
    draw_text(screen,text[: indice_texto],18,WIDTH/2 - 400, HEIGHT/2 + 150, 200, 300, BLACK)
    draw_text(screen,text_2[: indice_texto], 18, WIDTH/2 - 400, HEIGHT/2 + 168, 200, 300, BLACK)
    draw_text(screen,text_3[: indice_texto_2], 18, WIDTH/2 - 400, HEIGHT/2 + 186, 200, 300, BLACK)
    draw_text(screen, text_4[: indice_texto_3], 18, WIDTH/2 - 400, HEIGHT/2 + 202, 200, 300, BLACK)
    
    draw_text(screen, "FORÇA", 18, WIDTH/2 + 350, 0, 200, 300, RED)
    draw_text(screen, "INTEL", 18, WIDTH/2 + 350, 0 + 20, 200, 300, RED)
    draw_text(screen, "CARIS", 18, WIDTH/2 + 350, 0 + 40, 200, 300, RED)
    
    draw_number(screen, forca, 18, WIDTH/2 + 395, 0, 200, 300, RED)
    draw_number(screen, intel, 18, WIDTH/2 + 395, 0 + 20, 200, 300, RED)
    draw_number(screen, caris, 18, WIDTH/2 + 395, 0 + 40, 200, 300, RED)
    
#    draw_text(screen, atributos, 18, WIDTH/2 - 300, HEIGHT/2 + 60, 200, 300, YELLOW)
    
    if arquivo_json[cenario] == "Inicio":
        forca = intel = caris = 0
        
    #draw_text pro titulo
    #draw_text pra cada caminho
    pygame.display.flip()
#    print(background_rect)
pygame.quit()
