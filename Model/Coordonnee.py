# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(ligne:int,col:int)->tuple:
    if type(ligne) != int or type(col) != int:
        raise TypeError("Le numéro de ligne type_du_premier_paramètre ou le numéro de colonne type_du_second_paramètre ne sont pas des entiers")
    if ligne < 0 or col < 0:
        raise ValueError("Le numéro de ligne (valeur_de_la_ligne) ou de colonne (valeur_de_la_colonne) ne sont pas positifs")
    return (ligne,col)

def getLigneCoordonnee(coordonee:tuple)->int:
    if not type_coordonnee(coordonee):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordonee[0]


def getColonneCoordonnee(coordonee:tuple)->int:
    if not type_coordonnee(coordonee):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordonee[1]