import sys
import pygame
from pygame.locals import *
import pandas as pd
import Zone_jeu as z


class Jeu:
    def __init__(self):
        pygame.init()
        self.couleur = (100, 210, 200)
        self.size = ((600, 600))

        self.compteur = 0
        self.recommencer = True

        self.joueur = None
        self.joueur_X = "X"
        self.joueur_O = "O"

    def fontion_principale(self):
        while self.recommencer:
            self.fenetre = pygame.display.set_mode(self.size)
            self.grille = z.Zone_jeu(self.fenetre)

            self.continuer = True
            self.fenetre.fill(self.couleur)

            self.gagnant = None

            while self.continuer:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()

                    if self.gagnant is None:
                        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                            position_souris = [i // 200 for i in pygame.mouse.get_pos()]
                            x, y = position_souris[0], position_souris[1]
                            if self.compteur % 2 == 0:
                                self.case = self.grille.valeur_case(x, y, self.joueur_X)
                                self.joueur = self.joueur_X
                            else:
                                self.case = self.grille.valeur_case(x, y, self.joueur_O)
                                self.joueur = self.joueur_O
                            self.compteur += 1

                        #self.alignement()
                        # print(self.grille.case)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.continuer = False


                self.grille.afficher_lignes()
                self.grille.afficher_symboles()
                self.df_case = self.to_dataframe()
                self.alignement()

                pygame.display.flip()

    def alignement(self):  # verification de l'allignement des symboles

        # verification de l'allignement des symboles (lignes et colonnes)
        for i in range(0, 3):

            if self.df_case.iloc[i].values.tolist().count(self.joueur) == 3 or self.df_case.loc[:,
                                                                               i:i].values.tolist().count(
                    [self.joueur]) == 3:
                self.gagnant = self.joueur

        # verification de l'allignement des symboles pour les 2 diagonals

        if self.df_case.iat[0, 0] == self.df_case.iat[1, 1] == self.df_case.iat[2, 2] == self.joueur or \
                self.df_case.iat[0, 2] == self.df_case.iat[1, 1] == self.df_case.iat[2, 0] == self.joueur:
            self.gagnant = self.joueur


    def to_dataframe(self):
        self.df_case = pd.DataFrame(self.grille.case)
        return self.df_case



