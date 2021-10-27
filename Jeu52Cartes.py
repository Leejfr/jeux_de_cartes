from Carte import Carte

import random

class Jeu52Cartes:
    """
    Classe permettant de créer un jeu de 52 cartes et de jouer avec
    """
    def __init__(self) -> None:
        """
        Construit le jeu de 52 cartes
        """
        self.liste_cartes = []
        for enseigne in Carte.ENSEIGNES_CARTE:
            for valeur in Carte.VALEURS_CARTE:
                self.liste_cartes.append(Carte(valeur, enseigne))
                
    def __str__(self) -> str:
        """
        Affiche les cartes dans le jeu
        """
        output = ",".join([ str(carte) for carte in self.liste_cartes ])
        #print(output)
        return output
    
    def __len__(self):
        """
        Retourne le nombre de cartes restant dans le jeu

        """
        return len(self.liste_cartes)
        
    def piocher(self):
        """
        Pioche une carte dans le jeu

        Returns:
            (Carte): carte retirée du jeu
        """
        return self.liste_cartes.pop(random.randint(0,len(self.liste_cartes)))
    
    def melanger(self):
        """
        Mélange le jeu
        """
        random.shuffle(self.liste_cartes)
        
    def __contains__(self, element):
        if element in self.liste_cartes:
            return True
        else:
            return False
    
    