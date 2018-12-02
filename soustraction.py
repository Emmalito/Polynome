#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 11/22/2018
#__version__ : 1.4
#======================================================================================================
from addition import *
#======================================================================================================

def soustraction(poly1,poly2):
    """Fonction itértive revoyant la différence entre poly1 et poly2"""
    assert isinstance(poly1,liste),"Poly1 doit être une liste"
    assert isinstance(poly2,liste),"Poly2 doit être une liste"

    #Var
    différence = liste()
    
    #Begin
    while not( poly1.liste_vide() or poly2.liste_vide() ) :  #Tant qu'une des 2 listes n'est pas vide
        #begin
        puissance_1 = poly1.tete().p            #Meme principe que pour addition
        puissance_2 = poly2.tete().p
        if puissance_1 > puissance_2 :
            différence = construit_liste(poly1.tete(),différence)
            poly1.supprime_en_tete()
        if puissance_2 > puissance_1 :
            poly2.tete().coef = -poly2.tete().coef      #On rajoute le - devant le terme de poly_2
            différence = construit_liste(poly2.tete(),différence)
            poly2.supprime_en_tete()
        if puissance_1 == puissance_2 :
            poly1.tete().coef -= poly2.tete().coef  #On fait la diff entre coef de poly_1 et poly_2
            différence = construit_liste(poly1.tete(),différence)
            poly1.supprime_en_tete(), poly2.supprime_en_tete()
        #end
    while not poly1.liste_vide(): 
        différence = construit_liste(poly1.tete(),différence)
        poly1.supprime_en_tete()
    while not poly2.liste_vide():
        poly2.tete().coef = -poly2.tete().coef 
        différence = construit_liste(poly2.tete(),différence)
        poly2.supprime_en_tete()
    return retourne_liste(différence)
    #End
    
#======================================================================================================

def soustraction_rec(poly1,poly2,différence=liste()):
    """Fonction récursive revoyant la différence entre poly1 et poly2"""
    assert isinstance(poly1,liste),"Poly1 doit être une liste"
    assert isinstance(poly2,liste),"Poly2 doit être une liste"

 
    #Begin
    if poly1.liste_vide() and poly2.liste_vide() :
        return retourne_liste(différence)
    while not( poly1.liste_vide() or poly2.liste_vide() ) :
        #begin
        puissance_1 = poly1.tete().p
        puissance_2 = poly2.tete().p
        if puissance_1 > puissance_2 :
            différence = construit_liste(poly1.tete(),différence)
            return soustraction_rec(poly1.corps(),poly2,différence)
        if puissance_2 > puissance_1 :
            poly2.tete().coef = -poly2.tete().coef
            différence = construit_liste(poly2.tete(),différence)
            return soustraction_rec(poly1,poly2.corps(),différence)
        if puissance_1 == puissance_2 :
            poly1.tete().coef -= poly2.tete().coef
            différence = construit_liste(poly1.tete(),différence)
            return soustraction_rec(poly1.corps(),poly2.corps(),différence)
        #end
    while not poly1.liste_vide(): 
        différence = construit_liste(poly1.tete(),différence)
        return soustraction_rec(poly1.corps(),poly2,différence)
    while not poly2.liste_vide():
        poly2.tete().coef = -poly2.tete().coef 
        différence = construit_liste(poly2.tete(),différence)
        return soustraction_rec(poly1,poly2.corps(),différence)
    #End

#======================================================================================================

def soustraction_ptr(poly1,poly2):
    """Fonction revoyant la différence entre poly1 et poly2 à l'aide de la structure des listes"""
    assert isinstance(poly1,liste),"Poly1 doit être une liste"
    assert isinstance(poly2,liste),"Poly2 doit être une liste"

    #Var
    ptr_1, ptr_2 = None, None       #Pointeurs
    différence = liste()            #Liste

    #Begin
    ptr_1,ptr_2 = poly1.debut, poly2.debut
    while (ptr_1 != None) and (ptr_2 != None) :
        #begin
        puissance_1 = ptr_1.valeur.p
        puissance_2 = ptr_2.valeur.p
        if puissance_1 > puissance_2 :
            différence.debut = cellule(ptr_1.valeur,différence.debut)
            ptr_1 = ptr_1.suivant
        if puissance_2 > puissance_1 :
            ptr_2.valeur.coef = -ptr_2.valeur.coef
            différence.debut = cellule(ptr_2.valeur,différence.debut)
            ptr_2 = ptr_2.suivant
        if puissance_1 == puissance_2 :
            ptr_1.valeur.coef -= ptr_2.valeur.coef
            différence.debut = cellule(ptr_1.valeur,différence.debut)
            ptr_1, ptr_2 = ptr_1.suivant, ptr_2.suivant
        #end
    while ptr_1 != None :
        différence.debut = cellule(ptr_1.valeur,différence.debut)
        ptr_1 = ptr_1.suivant
    while ptr_2 != None :
        ptr_2.valeur.coef = -ptr_2.valeur.coef
        différence.debut = cellule(ptr_2.valeur,différence.debut)
        ptr_2 = ptr_2.suivant
    return retourne_liste(différence)
    #End
        





""" Info : Les fonctions soustraction sont un copié collé des fonctions addition. Je ne les ai donc pas vérifié. Il
    se peut qu'il y a des erreurs. Je n'ai pas beaucoup commenté non plus.
    S'il y a une erreur merci de me le dire.
    Les conditions qui vérifient que poly1 et poly2 sont vides sont surtout utile pour la division.
    Je vous laisse tester les fonctions """

#a = polynome("0x^0")
#p = polynome("3x^0,0x^1,5x^2")
#l = polynome("1x^0,4x^1,5x^2,2x^3")

#m = soustraction(p,l)
#m = soustraction(l,a)
#m = soustraction(a,p)

#m = soustraction_rec(p,l)
#m = soustraction_rec(l,a)
#m = soustraction_rec(a,p)


#m = soustraction_ptr(p,l)
#m = soustraction_ptr(l,a)
#m = soustraction_ptr(a,p)

#affichage_ptr(m)






