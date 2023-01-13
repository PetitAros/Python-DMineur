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


def getContenuGrilleDemineur(grille:list,coord:tuple)->int:
    return getContenuCellule(grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)])


def setContenuGrilleDemineur(grille:list,coord:tuple,contenu:int)->None:
    setContenuCellule(grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)],contenu)
    return None


def isVisibleGrilleDemineur(grille:list,coord:tuple)->bool:
    return isVisibleCellule(grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)])


def setVisibleGrilleDemineur(grille:list,coord:tuple,visibilite:bool)->None:
    setVisibleCellule(grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)],visibilite)
    return None


def contientMineGrilleDemineur(grille:list,coord:tuple)->bool:
    return contientMineCellule(grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)])


def getCoordonneeVoisinsGrilleDemineur(grille:list,coord:tuple)->list:
    if not(type_grille_demineur(grille) and type_coordonnee(coord)):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille")
    res = []
    ligne = getLigneCoordonnee(coord)
    col = getColonneCoordonnee(coord)
    coteGauche = col > 0
    coteHaut = ligne > 0
    coteBas = ligne < getNbLignesGrilleDemineur(grille) - 1
    coteDroit = col < getNbColonnesGrilleDemineur(grille) - 1
    if coteHaut:
        res.append((ligne-1,col))
    if coteGauche:
        res.append((ligne,col-1))
    if coteGauche and coteHaut:
        res.append((ligne-1,col-1))
    if coteBas:
        res.append((ligne+1,col))
    if coteDroit:
        res.append((ligne,col+1))
    if coteDroit and coteBas:
        res.append((ligne+1,col+1))
    if coteDroit and coteHaut:
        res.append((ligne-1,col+1))
    if coteGauche and coteBas:
        res.append((ligne+1,col-1))
    return res


def placerMinesGrilleDemineur(grille:list,nbMines:int,coord:tuple)->None:
    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n'est pas dans la grille. ")
    liste = []
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            liste.append(construireCoordonnee(i,j))
    if nbMines > len(liste)-1 or nbMines < 0:
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if coord in liste:
        liste.remove(coord)
    shuffle(liste)
    for i in range(nbMines):
        setContenuGrilleDemineur(grille,liste[i],const.ID_MINE)
    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille:list)->None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = construireCoordonnee(i,j)
            if not contientMineGrilleDemineur(grille,coord):
                val = 0
                voisins = getCoordonneeVoisinsGrilleDemineur(grille,coord)
                for voisin in voisins:
                    if contientMineGrilleDemineur(grille,voisin):
                        val += 1
                setContenuGrilleDemineur(grille,coord,val)
    return None


def getNbMinesGrilleDemineur(grille:list)->int:
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n'est pas une grille")
    count = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = construireCoordonnee(i,j)
            if contientMineGrilleDemineur(grille,coord):
                count += 1
    return count


def getAnnotationGrilleDemineur(grille:list,coord:tuple)->int:
    return grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)][const.ANNOTATION]


def getMinesRestantesGrilleDemineur(grille:list)->int:
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n'est pas une grille")
    count = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = construireCoordonnee(i,j)
            if getAnnotationGrilleDemineur(grille,coord) == const.FLAG:
                count += 1
    return getNbMinesGrilleDemineur(grille) - count


def gagneGrilleDemineur(grille:list)->bool:
    win = True
    i = 0
    while i < getNbLignesGrilleDemineur(grille) and win:
        j = 0
        while j < getNbColonnesGrilleDemineur(grille) and win:
            coord = construireCoordonnee(i,j)
            if (contientMineGrilleDemineur(grille,coord) and isVisibleGrilleDemineur(grille,coord)) or (not contientMineGrilleDemineur(grille,coord) and not isVisibleGrilleDemineur(grille,coord)) or (contientMineGrilleDemineur(grille,coord) and getAnnotationGrilleDemineur(grille,coord) != const.FLAG):
                win = False
            j += 1
        i += 1
    return win


def perduGrilleDemineur(grille:list)->bool:
    win = False
    i = 0
    while i < getNbLignesGrilleDemineur(grille) and not win:
        j = 0
        while j < getNbColonnesGrilleDemineur(grille) and not win:
            coord = construireCoordonnee(i,j)
            if contientMineGrilleDemineur(grille,coord) and isVisibleGrilleDemineur(grille,coord):
                win = True
            j += 1
        i += 1
    return win


def reinitialiserGrilleDemineur(grille:list)->None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = construireCoordonnee(i,j)
            reinitialiserCellule(grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)])
    return None


def decouvrirGrilleDemineur(grille:list,coord:tuple)->set:
    listeCasesVides = set()
    listeCasesVides.update([coord])
    setVisibleGrilleDemineur(grille,coord,True)
    if getContenuGrilleDemineur(grille,coord) == 0:
        voisins = getCoordonneeVoisinsGrilleDemineur(grille,coord)
        listeCasesVides.update(voisins)
        for voisin in voisins:
            if not isVisibleGrilleDemineur(grille,voisin) and getContenuGrilleDemineur(grille,voisin) == 0:
                listeCasesVides.update(decouvrirGrilleDemineur(grille,voisin))
    else:
        setVisibleGrilleDemineur(grille,coord,True)
    return listeCasesVides


def simplifierGrilleDemineur(grille:list,coord:tuple)->set:
    caseSimples = set()
    caseSimples.update([coord])
    if isVisibleGrilleDemineur(grille,coord):
        count = 0
        voisins = getCoordonneeVoisinsGrilleDemineur(grille,coord)
        for voisin in voisins:
            if getAnnotationGrilleDemineur(grille,voisin) == const.FLAG:
                count += 1
        if count == getContenuGrilleDemineur(grille,coord):
            for voisin in voisins:
                if getAnnotationGrilleDemineur(grille,voisin) != const.FLAG:
                    setVisibleGrilleDemineur(grille,voisin,True)
                    caseSimples.update([voisin])
    return caseSimples


def ajouterFlagsGrilleDemineur(grille:list,coord:tuple)->set:
    caseFlags = set()
    voisins = getCoordonneeVoisinsGrilleDemineur(grille,coord)
    count = 0
    for voisin in voisins:
        if not isVisibleGrilleDemineur(grille,voisin):
            count += 1
    if count == getContenuGrilleDemineur(grille,coord):
        for voisin in voisins:
            if not isVisibleGrilleDemineur(grille,voisin):
                while getAnnotationGrilleDemineur(grille,voisin) != const.FLAG:
                    changeAnnotationCellule(grille[getLigneCoordonnee(voisin)][getColonneCoordonnee(voisin)])
                caseFlags.update([voisin])
    return caseFlags


def resetResoudre(grille:list)->None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = construireCoordonnee(i,j)
            grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)][const.RESOLU] = False
    return None


def simplifierToutGrilleDemineur(grille:list)->tuple:
    casesSimples = set()
    caseFlags = set()
    modif = 1
    while modif > 0:
        modif = 0
        for i in range(getNbLignesGrilleDemineur(grille)):
            for j in range(getNbColonnesGrilleDemineur(grille)):
                coord = construireCoordonnee(i,j)
                simplifier = simplifierGrilleDemineur(grille,coord)
                if not grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)][const.RESOLU]:
                    if len(simplifier) > 1:
                        casesSimples.update(simplifier)
                        modif += 1
                        grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)][const.RESOLU] = True
                    flag = ajouterFlagsGrilleDemineur(grille,coord)
                    if len(flag) > 0:
                        caseFlags.update(flag)
                        modif += 1
                        grille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)][const.RESOLU] = True
    resetResoudre(grille)
    return (casesSimples,caseFlags)