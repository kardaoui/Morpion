import sys
import pygame
from pygame.locals import *
import pandas as pd
import Zone_jeu as z



class Jeu:
    def __init__(self):
        self.couleur = (100, 210, 200)
        self.size = ((600, 600))

        self.compteur=0
        self.recommencer=True

        self.joueur=None
        self.joueur_X="X"
        self.joueur_O="O"

    def fontion_principale(self):
        while self.recommencer:
            self.fenetre = pygame.display.set_mode(self.size)
            self.grille = z.Zone_jeu(self.fenetre)
            self.continuer = True
            self.fenetre.fill(self.couleur)
            while self.continuer:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()

                    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        position_souris = [i // 200 for i in pygame.mouse.get_pos()]
                        x, y = position_souris[0], position_souris[1]
                        if self.compteur % 2 == 0:
                            self.grille.valeur_case(x,y,self.joueur_X)
                            self.joueur=self.joueur_X
                        else:
                            self.grille.valeur_case(x,y,self.joueur_O)
                            self.joueur = self.joueur_O
                        self.compteur+=1
                        self.df_case = pd.DataFrame(self.grille.case)
                        print(self.df_case)
                        self.alignement()


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.continuer=False


                self.grille.afficher_lignes()
                self.grille.afficher_symboles()

                pygame.display.flip()

    def alignement(self): # verification de l'allignement des symboles

        # verification de l'allignement des symboles en colonne
        for i in range(0, 3):
            if self.df_case.loc[:, i:i].values.tolist().count([self.joueur]) == 3:
                print("ok", i, self.joueur)

        # verification de l'allignement des symboles en ligne
        for i in range(0, 3):
            if self.df_case.iloc[i].values.tolist().count(self.joueur) == 3:
                print("ok", i, self.joueur)



if __name__=="__main__":
    pygame.init()
    Jeu().fontion_principale()

