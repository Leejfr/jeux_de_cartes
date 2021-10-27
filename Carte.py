import random

class ValueException(BaseException):
    pass

class EnsignException(BaseException):
    pass

class Carte:
    """
    Classe permettant de définir une carte
    """
    VALEURS_CARTE = ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]
    ENSEIGNES_CARTE = ["coeur", "carreau", "pique", "trèfle"]
    
    def __init__(self) -> None:
        self.__init__(random.choice(self.VALEURS_CARTE), random.choice(self.ENSEIGNES_CARTE))
    
    def __init__(self, valeur, enseigne) -> None:
        """
        Créer une carte à partir de sa valeur et de son enseigne

        Args:
            valeur (string): valeur de la carte entre as, 2, 3 ... 10, valet, dame et roi
            enseigne ([type]): enseigne de la carte entre coeur / carreau / pique / trèfle
        
        Raises:
            ValueException: valeur non connue
            EnsignException: enseigne non connue
        """
        try:
            if valeur not in self.VALEURS_CARTE: raise ValueException
            if enseigne not in self.ENSEIGNES_CARTE: raise EnsignException
        except ValueException:
            raise ValueError("Valeur de la carte incorrecte")
        except EnsignException:
            raise ValueError("Enseigne de la carte incorrecte")
        finally:
            self.valeur = valeur
            self.enseigne = enseigne
            
    def __str__(self) -> str:
        """
        Surcharge la fonction print

        Returns:
            str: {valeur} de {enseigne}
        """
        return f"{self.valeur} de {self.enseigne}"
    
    # def __repr__(self) -> str:
    #     return self
        
    @property
    def couleur(self):
        """
        Affiche la couleur de la carte
        """
        if self.enseigne in ["coeur","carreau"]:
            return "rouge"
        else:
            return "noir"
            
            
        
        
        