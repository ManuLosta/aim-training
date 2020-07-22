# Imports
import pygame
import os
import math
import random
import sys
import time

# Setup Display
pygame.init()
WIDTH, HEIGHT = 1280, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Training")
ICON = pygame.image.load("imgs/target.png")
pygame.display.set_icon(ICON)

# Images
ICON_SMALL = pygame.transform.scale(ICON,(600, 600))
MANUAL_CURSOR = pygame.transform.scale(pygame.image.load("imgs/aim.png"), (30, 30)).convert_alpha()
MANUAL_CURSOR1 = pygame.transform.scale(pygame.image.load("imgs/aim1.png"), (40, 40)).convert_alpha()
MANUAL_CURSOR2 = pygame.transform.scale(pygame.image.load("imgs/aim2.png"), (150, 150)).convert_alpha()
MANUAL_CURSOR3 = pygame.transform.scale(pygame.image.load("imgs/aim3.png"), (150, 150)).convert_alpha()

# FONTS
FUENTE_PUNTUACION = pygame.font.SysFont('comicsans', 30)
FUENTE_MENU = pygame.font.SysFont('comicsansms', 50)
FUENTE_FINAL = pygame.font.SysFont('comicsansms', 50)
FUENTE_TIEMPO = pygame.font.SysFont('comicsansms', 100)
FUENTE_TITULO = pygame.font.SysFont('comicsansms', 70)

# Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)

# Variables
RADIO_EXTERIOR = 25
RADIO_MEDIO = 15
RADIO_INTERIOR = 3
crosshair = MANUAL_CURSOR

# Setup Game Loop
FPS = 60
clock = pygame.time.Clock()

# X y Y de los targets aleatorios
def aleatorio():
    global x, y

    x = random.randint(0 + RADIO_EXTERIOR, WIDTH - RADIO_EXTERIOR)
    y = random.randint(0 + RADIO_EXTERIOR, HEIGHT - RADIO_EXTERIOR)

# Menu System
def drawMenu():
    menu = True
    win.fill(BLANCO)
    #clock.tick(FPS)

    #Diseño
    win.blit(ICON_SMALL, (-300, -300))
    win.blit(ICON_SMALL, (WIDTH - 300,  HEIGHT - 300))

    # Título
    titleText = FUENTE_TITULO.render("AIM TRAINING", 1, NEGRO)
    win.blit(titleText, (int(WIDTH / 2 - titleText.get_width() /2), 10))

    # Opciones del Menu
    playText = FUENTE_MENU.render("JUGAR", 1, NEGRO)
    playText_x = WIDTH / 2 - playText.get_width() / 2
    playText_y = 250
    win.blit(playText, (int(playText_x), int(playText_y)))

    settingsText = FUENTE_MENU.render("OPCIONES", 1, NEGRO)
    settingsText_x = WIDTH / 2 - settingsText.get_width() / 2
    settingsText_y = 350
    win.blit(settingsText, (int(settingsText_x), int(settingsText_y)))

    quitText = FUENTE_MENU.render("SALIR", 1, NEGRO)
    quitText_x = WIDTH / 2 - quitText.get_width() / 2
    quitText_y = 550
    win.blit(quitText, (int(quitText_x), int(quitText_y)))

    pygame.display.update()

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                print(m_x, m_y)

                if m_x >= playText_x and m_x <= playText_x + playText.get_width() and m_y >= playText_y and m_y <= playText_y + playText.get_height():
                    selectMode()
                    #menu = False

                elif m_x >= settingsText_x and m_x <= settingsText_x + settingsText.get_width() and m_y >= settingsText_y and m_y <= settingsText_y + settingsText.get_height():
                    settings()

                elif m_x >= quitText_x and m_x <= quitText_x + quitText.get_width() and m_y >= quitText_y and m_y <= quitText_y + quitText.get_height():
                    pygame.quit()
                    quit()

def selectMode():
    global mode
    selectMode = True
    win.fill(BLANCO)

    #Diseño
    win.blit(ICON_SMALL, (-300, -300))
    win.blit(ICON_SMALL, (WIDTH - 300,  HEIGHT - 300))

     # Opciones del Menu 2
    normalModeText = FUENTE_MENU.render("NORMAL", 1, NEGRO)
    normalModeText_x = WIDTH / 2 - normalModeText.get_width() / 2
    normalModeText_y = 150
    win.blit(normalModeText, (int(normalModeText_x), int(normalModeText_y)))

    hpsModeText = FUENTE_MENU.render("HITS POR SEGUNDO", 1, NEGRO)
    hpsModeText_x = WIDTH / 2 - hpsModeText.get_width() / 2
    hpsModeText_y = 250
    win.blit(hpsModeText, (int(hpsModeText_x), int(hpsModeText_y)))

    quitText = FUENTE_MENU.render("SALIR", 1, NEGRO)
    quitText_x = WIDTH / 2 - quitText.get_width() / 2
    quitText_y = 400
    win.blit(quitText, (int(quitText_x), int(quitText_y)))

    pygame.display.update()

    while selectMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                print(m_x, m_y)

                if m_x >= normalModeText_x and m_x <= normalModeText_x + normalModeText.get_width() and m_y >= normalModeText_y and m_y <= normalModeText_y + normalModeText.get_height():
                    mode = 1
                    aleatorio()
                    start()

                elif m_x >= hpsModeText_x and m_x <= hpsModeText_x + hpsModeText.get_width() and m_y >= hpsModeText_y and m_y <= hpsModeText_y + hpsModeText.get_height():
                    mode = 2
                    aleatorio()
                    start()

                elif m_x >= quitText_x and m_x <= quitText_x + quitText.get_width() and m_y >= quitText_y and m_y <= quitText_y + quitText.get_height():
                    pygame.quit()
                    quit()

def start():
    start = True
    startTime = time.time()
    while start:
        tiempo = 3
        endTime = time.time()
        seconds = (endTime - startTime)
        secondsLeft = round(tiempo - seconds)
        win.fill(BLANCO)
        tiempoText = FUENTE_TIEMPO.render(str(secondsLeft), 1, NEGRO)
        win.blit(tiempoText, (int(WIDTH / 2 - tiempoText.get_width() / 2), int(HEIGHT / 2 - tiempoText.get_height() / 2)))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if secondsLeft == 0:
            if mode == 1:
                game()
            elif mode == 2:
                hpsGame()

        clock.tick(FPS)

# Normal Mode Game Loop
def game():
    global puntuacion
    run = True
    puntuacion = 0
    pygame.mouse.set_visible(False)
    startTime = time.time()

    while run:
        clock.tick(FPS)
        win.fill(BLANCO)

        # Dibujar Diana
        pygame.draw.circle(win, ROJO, (x, y), RADIO_EXTERIOR, 3)
        pygame.draw.circle(win, ROJO, (x, y), RADIO_MEDIO, 3)
        pygame.draw.circle(win, ROJO, (x, y), RADIO_INTERIOR, 3)

        # Crosshair
        mousePos_x, mousePos_y = pygame.mouse.get_pos()
        win.blit(crosshair, (mousePos_x - crosshair.get_width() / 2, mousePos_y - crosshair.get_height() / 2))

        # Dibujar Puntuacion
        punText = FUENTE_PUNTUACION.render("PUNTUACIÓN: " + str(puntuacion), 1, NEGRO)
        win.blit(punText, (10, 10))

        # Dibujar Tiempo restante
        tiempo = 30
        endTime = time.time()
        seconds = (endTime - startTime)
        secondsLeft = tiempo - seconds

        if secondsLeft >= 10:
            secondsLeft = round(secondsLeft)

        else:
            secondsLeft = round(secondsLeft, 2)

        timeText = FUENTE_PUNTUACION.render("TIEMPO: " + str(secondsLeft), 1, NEGRO)
        win.blit(timeText, (WIDTH - 10 - timeText.get_width(), 10))

        if round(secondsLeft) == 0:
            endMenu()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                print(dis)

                if  RADIO_EXTERIOR > dis > RADIO_MEDIO:
                    puntuacion = puntuacion + 1
                    print(puntuacion)
                    aleatorio()

                elif RADIO_MEDIO > dis > RADIO_INTERIOR:
                    puntuacion = puntuacion + 5
                    print(puntuacion)
                    aleatorio()

                elif dis < RADIO_INTERIOR:
                    puntuacion = puntuacion + 10
                    print(puntuacion)
                    aleatorio()

                elif dis > RADIO_EXTERIOR:
                    puntuacion = puntuacion - 1

def hpsGame():
    global hps
    run = True
    puntuacion = 0
    pygame.mouse.set_visible(False)
    startTime = time.time()  # resetea el timer  ---- NO SACAR ----

    while run:
        clock.tick(FPS)
        win.fill(BLANCO)

        # Dibujar Diana
        pygame.draw.circle(win, ROJO, (x, y), RADIO_EXTERIOR, 3)
        pygame.draw.circle(win, ROJO, (x, y), RADIO_MEDIO, 3)
        pygame.draw.circle(win, ROJO, (x, y), RADIO_INTERIOR, 3)

        # Crosshair
        mousePos_x, mousePos_y = pygame.mouse.get_pos()
        win.blit( crosshair, (mousePos_x - crosshair.get_width() / 2, mousePos_y - crosshair.get_height() / 2))

        tiempo = 30
        endTime = time.time()
        seconds = (endTime - startTime)
        secondsLeft = tiempo - seconds

        # Dibujar Puntuacion
        hps = round(puntuacion / seconds, 2)
        punText = FUENTE_PUNTUACION.render("HITS POR SEGUNDO: " + str(hps), 1, NEGRO)
        win.blit(punText, (10, 10))

        if secondsLeft >= 10:
            secondsLeft = round(secondsLeft)

        else:
            secondsLeft = round(secondsLeft, 2)

        timeText = FUENTE_PUNTUACION.render("TIEMPO: " + str(secondsLeft), 1, NEGRO)
        win.blit(timeText, (WIDTH - 10 - timeText.get_width(), 10))

        if round(secondsLeft) == 0:
            endMenu()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                print(dis)

                if  dis <= RADIO_EXTERIOR:
                    aleatorio()
                    puntuacion = puntuacion + 1


def endMenu():
    end = True
    win.fill(BLANCO)
    pygame.mouse.set_visible(True)

    # Mostrar Puntuación y menú
    if mode == 1:
        puntText2 = FUENTE_FINAL.render("PUNTUACIÓN: " + str(puntuacion), 1, NEGRO)

    elif mode == 2:
        puntText2 = FUENTE_FINAL.render("PUNTUACIÓN: " + str(hps), 1, NEGRO)

    win.blit(puntText2, (int(WIDTH / 2 - puntText2.get_width() / 2), 100))

    quitText = FUENTE_MENU.render("SALIR", 1, NEGRO)
    quitText_x = WIDTH / 2 - quitText.get_width() / 2
    quitText_y = 450
    win.blit(quitText, (int(quitText_x), int(quitText_y)))

    playagainText = FUENTE_MENU.render("JUGAR DE NUEVO", 1, NEGRO)
    playagainText_x = WIDTH / 2 - playagainText.get_width() / 2
    playagainText_y = 250
    win.blit(playagainText, (int(playagainText_x), int(playagainText_y)))

    mainmenuText = FUENTE_MENU.render("MENÚ PRINCIPAL", 1, NEGRO)
    mainmenuText_x = WIDTH / 2 - mainmenuText.get_width() / 2
    mainmenuText_y = 350
    win.blit(mainmenuText, (int(mainmenuText_x), int(mainmenuText_y)))

    pygame.display.update()
    m_x, m_y = pygame.mouse.get_pos()

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()

                if m_x >= playagainText_x and m_x <= playagainText_x + playagainText.get_width() and m_y >= playagainText_y and m_y <= playagainText_y + playagainText.get_height():
                    game()

                elif m_x >= mainmenuText_x and m_x <= mainmenuText_x + mainmenuText.get_width() and m_y >= mainmenuText_y and m_y <= mainmenuText_y + mainmenuText.get_height():
                    drawMenu()

                elif m_x >= quitText_x and m_x <= quitText_x + quitText.get_width() and m_y >= quitText_y and m_y <= quitText_y + quitText.get_height():
                    pygame.quit()
                    quit()

def settings():
    global crosshair
    win.fill(BLANCO)

    #Diseño
    win.blit(ICON_SMALL, (-300, -300))
    win.blit(ICON_SMALL, (WIDTH - 300,  HEIGHT - 300))

    crosshairText = FUENTE_MENU.render("MIRA", 1, NEGRO)
    win.blit(crosshairText, (int(WIDTH / 2 - crosshairText.get_width() / 2), 100))

    win.blit(MANUAL_CURSOR, (int(WIDTH / 2 - MANUAL_CURSOR.get_width() / 2) , 200))
    win.blit(MANUAL_CURSOR1, (int(WIDTH / 2 - MANUAL_CURSOR.get_width() / 2) , 200))
    win.blit(MANUAL_CURSOR2, (int(WIDTH / 2 - MANUAL_CURSOR.get_width() / 2) , 200))
    win.blit(MANUAL_CURSOR3, (int(WIDTH / 2 - MANUAL_CURSOR.get_width() / 2) , 200))

    pygame.display.update()

drawMenu()

pygame.quit()
