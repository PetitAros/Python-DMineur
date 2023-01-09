# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(contenu:int)->bool:
    return type(contenu) == int and ((contenu >= 0 and contenu <= 8) or contenu == const.ID_MINE)


def construireCellule(contenu:int=0,visibilite:bool=False)->dict:
    if not isContenuCorrect(contenu):
        raise ValueError("construireCellule : le contenu valeur_du_contenu n’est pas correct")
    if type(visibilite) != bool:
        raise TypeError("construireCellule : le second paramètre (type_du_paramètre) n’est pas un booléen")
    return {const.CONTENU:contenu,const.VISIBLE:visibilite}

