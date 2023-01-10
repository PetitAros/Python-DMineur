# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(lignes:int,colonnes:int)->list:
    if lignes <= 0 or colonnes <= 0:
        raise ValueError("construireGrilleDemineur : Le nombre de lignes (valeur_du_premier_paramètre) ou de colonnes (valeur_du_second_paramètre) est négatif ou nul.")
    if type(lignes) != int or type(colonnes) != int:
        raise TypeError("construireGrilleDemineur : Le nombre de liges (type_du_premier_paramètre) ou de colonnes (type_du_second_paramètre) n’est pas un entier.")
    res = []
    for i in range(lignes):
        res.append([])
        for j in range(colonnes):
            res[i].append(construireCellule())
    return res


def getNbLignesGrilleDemineur(grille:list)->int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)

def getNbColonnesGrilleDemineur(grille:list)->int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])


def isCoordonneeCorrecte(grille:list,coord:tuple)->bool:
    if  not (type_grille_demineur(grille) and type_coordonnee(coord)):
        raise TypeError("isCoordoneeCorrect : un des paramètres n'est pas du bon type")
    return getLigneCoordonnee(coord) < getNbLignesGrilleDemineur(grille) and getColonneCoordonnee(coord) < getNbColonnesGrilleDemineur(grille)


def getCelluleGrilleDemineur(grille:list,coord:tuple)->dict:
    if not (type_grille_demineur(grille) and type_coordonnee(coord)):
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)]


