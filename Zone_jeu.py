import pygame


class Zone_jeu:
    def __init__(self,fenetre):
        self.fenetre=fenetre
        self.lignes = [((200, 0), (200, 600)),
                      ((400, 0), (400, 600)),
                      ((0, 200), (600, 200)),
                      ((0, 400), (600, 400))
                      ]
        self.case=[[0 for i in range(0, 3)] for j in range(0, 3)]

    def afficher_lignes(self):
        for ligne in self.lignes:
            pygame.draw.line(self.fenetre, (0, 0, 0), ligne[0], ligne[1], 4)


    def afficher_symboles(self):
        for x, ligne in enumerate(self.case):
            for y, colonne in enumerate(ligne):
                if self.case[y][x] == "X":
                    # dessin de la croix pour le joueur X
                    pygame.draw.line(self.fenetre, (255, 0, 0), (x * 200, y * 200),
                                     ((x * 200) + 200, (y * 200) + 200), 10)
                    pygame.draw.line(self.fenetre, (255, 0, 0), ((x * 200) + 200, (y * 200)),
                                     ((x * 200), (y * 200) + 200), 10)

                elif self.case[y][x] == "O":
                    # dessin de la croix pour le joueur
                    pygame.draw.circle(self.fenetre, (255, 0, 0), ((x * 200) + 100, (y * 200) + 100), 100, 10)



    def valeur_case(self, x, y, valeur):
        if self.case[y][x] == 0:
            self.case[y][x] = valeur


if __name__=="__main__":
    Zone_jeu()