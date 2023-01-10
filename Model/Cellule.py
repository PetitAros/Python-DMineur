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


def construireCellule(contenu:int=0,visible:bool=False)->dict:
    if not isContenuCorrect(contenu):
        raise ValueError("construireCellule : le contenu valeur_du_contenu n’est pas correct")
    if type(visible) != bool:
        raise TypeError("construireCellule : le second paramètre (type_du_paramètre) n’est pas un booléen")
    return {const.CONTENU:contenu,const.VISIBLE:visible,const.ANNOTATION:None}


def getContenuCellule(cellule:dict)->int:
    if not type_cellule(cellule):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.CONTENU]


def isVisibleCellule(cellule:dict)->bool:
    if not type_cellule(cellule):
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.VISIBLE]


def setContenuCellule(cellule:dict,contenu:int)->None:
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if not isContenuCorrect(contenu):
        raise ValueError("setContenuCellule : la valeur du contenu (valeur_passée_en_paramètre) n’est pas correcte.")
    if not type_cellule(cellule):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    cellule[const.CONTENU] = contenu
    return None


def setVisibleCellule(cellule:dict,visibilite:bool)->None:
    if not type_cellule(cellule):
        raise TypeError("setVisibleCellule : Le premier paramètre n'est pas une cellule.")
    if type(visibilite) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen ")
    cellule[const.VISIBLE] = visibilite
    return None


def contientMineCellule(cellule:dict)->bool:
    if not type_cellule(cellule):
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.CONTENU] == const.ID_MINE


def isAnnotationCorrecte(annotation:str)->bool:
    return annotation in (None,const.DOUTE,const.FLAG)