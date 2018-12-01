#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 11/17/2018
#__version__ : 1.3
#======================================================================================================
from saisie_affichage import *
#======================================================================================================

def valeur(poly,x):
    """Fonction itérative retournant la valeur du polynome en x"""
    assert isinstance(poly,liste),"Le polynôme est une liste"
    assert isinstance(x,(int,float)),"x est un réel"

    #Var
    resultat = 0.0    #float

    #Begin
    #Tant qu'on a pas parcourue toute la liste, on ajoute au résultat la valeur du terme en x
    while not (poly.liste_vide()) :
        resultat += poly.tete().coef * ( x ** poly.tete().p)
        poly.supprime_en_tete()
    #Puis on retourne le résultat
    return resultat
    #End

#======================================================================================================

def valeur_rec(poly,x,resultat=0.0):
    """Fonction récursive retournant la valeur du polynome en x"""
    assert isinstance(poly,liste),"Le polynôme est une liste"
    assert isinstance(x,(int,float)),"x est un réel"

    #Begin
    #Si la liste est vide on retourne le resultat
    if poly.liste_vide() :
        return resultat
    #Sinon on ajoute au résultat la valeur du terme en x
    else :
        resultat += poly.tete().coef * ( x ** poly.tete().p)
        #On rappel la fonction pour calculer le reste des termes 
        return valeur_rec(poly.corps(),x,resultat)
    #End

#======================================================================================================

def valeur_ptr(poly,x) :
    """Fonction retournant la valeur du polynome en x à l'aide de la structure des listes"""
    assert isinstance(poly,liste),"Le polynôme est une liste"
    assert isinstance(x,(int,float)),"x est un réel"

    #Var
    resultat = 0.0    #Float
    ptr = None      #Pointeur
    
    #Begin
    #On place le pointeur au début
    ptr = poly.debut
    #Tant que le pointeur est sur une cellule pleine, on calcule le terme en x
    while ptr != None :
        resultat += ptr.valeur.coef * (x**ptr.valeur.p)
        ptr = ptr.suivant       #Et on passe à la cellule suivante
    #On retourne le résultat
    return resultat
    #End


""" Info : Rien de compliqué pour cette fonction.
    Je laisse de quoi tester les fonctions ci-dessous """

#p = polynome("-3x^0,2x^1,4x^2")
#print(valeur(p,2))
#print(valeur_rec(p,2))
#print(valeur_ptr(p,2))






















