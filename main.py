def plus_grand(a: float, b: float) -> float:
    """
    Retourne le plus grand de deux nombres réels.

    :type b: float
    :param a: premier nombre réel
    :param b: deuxième nombre réel
    :return: le plus grand des deux nombres
    """
    if a > b:
        return a
    else:
        return b
print(plus_grand((5.4), 8.7))
def superieur_seuil(valeur: float, seuil: float = 10) -> bool:
    """
    Indique si une valeur est supérieure à un seuil.

    :param valeur: valeur à tester
    :param seuil: seuil de comparaison, 10 par défaut
    :return: True si la valeur est supérieure au seuil, False sinon
    """
    return valeur > seuil
print(superieur_seuil(5.4, 8.7))
print(superieur_seuil(15))       # True
print(superieur_seuil(8))        # False
print(superieur_seuil(15, 20))   # False
def plus_grand_liste(valeurs: list[float]) -> float:
    """
    Retourne la plus grande valeur d'une liste.

    :param valeurs: liste de valeurs réelles
    :return: la plus grande valeur
    """
    return max(valeurs)
print(plus_grand_liste([5.4, 8.7, 3.2, 12.5]))
def nombre_inferieur(valeurs: list[float], seuil: float = 3) -> int:
    """
    Retourne le nombre de valeurs inférieures à un seuil.

    :param valeurs: liste de valeurs réelles
    :param seuil: seuil de comparaison, 3 par défaut
    :return: nombre de valeurs inférieures au seuil
    """
    return sum(valeur < seuil for valeur in valeurs)
print(nombre_inferieur([1, 2, 4, 5, 2.5]))
print(nombre_inferieur([1, 2, 4, 5, 2.5], 5))
def afficher_dictionnaire(donnees: dict, texte: str) -> None:
    """
    Affiche l'ensemble des données d'un dictionnaire.

    :param donnees: dictionnaire à afficher
    :param texte: chaîne de caractères affichée avant chaque donnée
    :return: None
    """
    for cle, valeur in donnees.items():
        print(texte, cle, ":", valeur)
donnees = {"nom": "Youssef", "age": 19, "ville": "Colmar"}

afficher_dictionnaire(donnees, "Info :")
class Tasse:
    matiere: str = "céramique"

    def __init__(self, couleur: str, contenance: int, marque: str):
        """
        Initialise une tasse.

        :param couleur: couleur de la tasse
        :param contenance: contenance de la tasse en ml
        :param marque: marque de la tasse
        """
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
tasse1 = Tasse("blanche", 250, "IKEA")

print(tasse1.couleur)
print(tasse1.contenance)
print(tasse1.marque)
print(tasse1.matiere)
class Tasse:
    matiere: str = "céramique"

    def __init__(self, couleur: str, contenance: int, marque: str):
        """
        Initialise une tasse.

        :param couleur: couleur de la tasse
        :param contenance: contenance de la tasse en ml
        :param marque: marque de la tasse
        """
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self) -> str:
        """
        Retourne une description de la tasse.

        :return: chaîne de caractères décrivant la tasse
        """
        return f"La tasse de matière {self.matiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml"
tasse1 = Tasse("bleu", 50, "duralex")

print(tasse1)