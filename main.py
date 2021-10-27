from Carte import Carte
from Jeu52Cartes import Jeu52Cartes

if __name__ == "__main__":
    jeu = Jeu52Cartes()
    str(jeu)
    jeu.melanger()
    str(jeu)
    
    carte = jeu.piocher()
    carte
    
    str(jeu)