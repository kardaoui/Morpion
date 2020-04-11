# Creation du je du Morpion grace au module pygame
import sys
#pygame importation du module
import pygame
from pygame.locals import *

# initialisation de pygame
pygame.init()

recommencer = True
while recommencer:
    # creation de la fenetre du jeu
    fenetre = pygame.display.set_mode((600, 600))
    fenetre.fill((100, 210, 200))
    # creation de deux ligne pour representer la grille de jeu
    lines = [((200, 0), (200, 600)),
             ((400, 0), (400, 600)),
             ((0, 200), (600, 200)),
             ((0, 400), (600, 400))
             ]
    for line in lines:
        pygame.draw.line(fenetre, (0, 0, 0), line[0], line[1], 4)

        # creation de la grille sous forme de tableau de 3 dimenssions

    grille = [[0 for i in range(0, 3)] for j in range(0, 3)]

    # boucle infinie du jeu

    compteur = 0
    continuer = True
    while continuer is True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            # recuperer la position de la sourie quand on fait un clik droit
            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                position_mouse = [i // 200 for i in pygame.mouse.get_pos()]
                x = position_mouse[0]
                y = position_mouse[1]
                player = 0
                if grille[x][y] == 0:
                    if compteur % 2 == 0:
                        grille[x][y] = 'X'
                        player = "X"
                    else:
                        grille[x][y] = 'O'
                        player = "O"
                    for i in grille:
                        for j in i:
                            if j == "X" and player == "X":
                                # dessin de la croix pour le joueur X
                                pygame.draw.line(fenetre, (255, 0, 0), (x * 200, y * 200),
                                                 ((x * 200) + 200, (y * 200) + 200), 10)
                                pygame.draw.line(fenetre, (255, 0, 0), ((x * 200) + 200, (y * 200)),
                                                 ((x * 200), (y * 200) + 200), 10)
                            elif j == "O" and player == "O":
                                # dessin de la croix pour le joueur O
                                pygame.draw.circle(fenetre, (255, 0, 0), ((x * 200) + 100, (y * 200) + 100), 100, 10)
                            compteur += 1

            if event.type==KEYDOWN and event.key==K_SPACE:
                continuer=False

        pygame.display.flip()
        continue
