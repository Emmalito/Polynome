#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 11/17/2018
#__version__ : 1.4
#======================================================================================================
from valeur import *
#======================================================================================================

def addition(poly1,poly2):
    """Fonction itértive revoyant la somme de poly1 et poly2"""
    assert isinstance(poly1,liste),"Poly1 doit être une liste"
    assert isinstance(poly2,liste),"Poly2 doit être une liste"

    #Var
    somme = liste()     #Liste
    
    #Begin
    while not( poly1.liste_vide() or poly2.liste_vide() ) : #Tant qu'une des listes n'est pas vide
        #begin
        puissance_1 = poly1.tete().p    #On récupère les puissance du 1er terme des listes
        puissance_2 = poly2.tete().p
        if puissance_1 > puissance_2 :  #Si le degré du 1er poly est + grand que celui du second
            somme = construit_liste(poly1.tete(),somme) #On l'ajoute directement à la somme
            poly1.supprime_en_tete() #puis on le supprime
        if puissance_2 > puissance_1 : #De meme 
            somme = construit_liste(poly2.tete(),somme)
            poly2.supprime_en_tete()
        if puissance_1 == puissance_2 : #Si les degrés sont égaux
            poly1.tete().coef += poly2.tete().coef  #On somme leur coef
            somme = construit_liste(poly1.tete(),somme) #On insère la somme dans le nouveau polynome
            poly1.supprime_en_tete(), poly2.supprime_en_tete() #et on supprime les 2 termes
        #end
    while not poly1.liste_vide(): #Si poly_2 est vide, on ajoute ce qu'il reste de poly_1 à la somme
        somme = construit_liste(poly1.tete(),somme)
        poly1.supprime_en_tete()
    while not poly2.liste_vide(): #Si poly_1 est vide, on ajoute ce qu'il reste de poly_1 à la somme
        somme = construit_liste(poly2.tete(),somme)
        poly2.supprime_en_tete()
    return retourne_liste(somme) #On retourne la somme
    #End
    
#======================================================================================================

def addition_rec(poly1,poly2,somme=liste()):
    """Fonction récursive revoyant la somme de poly1 et poly2"""
    assert isinstance(poly1,liste),"Poly1 doit être une liste"
    assert isinstance(poly2,liste),"Poly2 doit être une liste"

 
    #Begin
    if poly1.liste_vide() and poly2.liste_vide() : #Si les 2 listes sont vides, on renvoi la somme
        return retourne_liste(somme)
    while not( poly1.liste_vide() or poly2.liste_vide() ) : #Tant qu'une liste n'est pa vide
        #begin
        puissance_1 = poly1.tete().p                    #On fait fait comme pour la fonction itérative
        puissance_2 = poly2.tete().p
        if puissance_1 > puissance_2 :
            somme = construit_liste(poly1.tete(),somme)
            return addition_rec(poly1.corps(),poly2,somme) #Puis on rappel la fonction avec les termes en moins
        if puissance_2 > puissance_1 :
            somme = construit_liste(poly2.tete(),somme)
            return addition_rec(poly1,poly2.corps(),somme)
        if puissance_1 == puissance_2 :
            poly1.tete().coef += poly2.tete().coef
            somme = construit_liste(poly1.tete(),somme)
            return addition_rec(poly1.corps(),poly2.corps(),somme)
        #end
    while not poly1.liste_vide() :
        somme = construit_liste(poly1.tete(),somme)
        poly1.supprime_en_tete()
    while not poly2.liste_vide() :
        somme = construit_liste(poly2.tete(),somme)
        poly2.supprime_en_tete()
    #On renvoi ensuite la somme
    return retourne_liste(somme)
    #End

#======================================================================================================

def addition_ptr(poly1,poly2):
    """Fonction revoyant la somme de poly1 et poly2 à l'aide de la structure des listes"""
    assert isinstance(poly1,liste),"Poly1 doit être une liste"
    assert isinstance(poly2,liste),"Poly2 doit être une liste"

    #Var
    ptr_1, ptr_2 = None, None   #Pointeurs
    somme = liste()             #Liste

    #Begin
    ptr_1,ptr_2 = poly1.debut, poly2.debut
    while (ptr_1 != None) and (ptr_2 != None) :
        #begin
        puissance_1 = ptr_1.valeur.p
        puissance_2 = ptr_2.valeur.p
        if puissance_1 > puissance_2 :
            somme.debut = cellule(ptr_1.valeur,somme.debut)
            ptr_1 = ptr_1.suivant
        if puissance_2 > puissance_1 :
            somme.debut = cellule(ptr_2.valeur,somme.debut)
            ptr_2 = ptr_2.suivant
        if puissance_1 == puissance_2 :
            ptr_1.valeur.coef += ptr_2.valeur.coef
            somme.debut = cellule(ptr_1.valeur,somme.debut)
            ptr_1, ptr_2 = ptr_1.suivant, ptr_2.suivant
        #end
    while ptr_1 != None :
        somme.debut = cellule(ptr_1.valeur,somme.debut)
        ptr_1 = ptr_1.suivant
    while ptr_2 != None :
        somme.debut = cellule(ptr_2.valeur,somme.debut)
        ptr_2 = ptr_2.suivant
    return retourne_liste(somme)
    #End
        

""" Info : Pour la fonction récursive, il y a 3 paramètres d'entré mais 2 suffises pour qu'il fonctionne (poly1 et poly2)
    La fonction retourne_liste() sert à inverser une liste. Je l'utilise pour que la liste somme soit bien
    une liste de terme décroissant.
    Les fonctions rec et ptr sont moins commentées parce que y'a rien de nouveau.
    Les listes ne peuvent être vide donc je ne traite pas ce cas. (je sais je me répète)
    Les conditions "While not" sont placés dans un ordre logique.
    Les conditions qui assurent que poly_1 et poly_2 soient vide sont surtout utile pour les fonctions multiplications
    Je laisse de quoi tester les fonction """






#p = polynome("-3x^0,2x^1,4x^2")
#l = polynome("6x^0,-2x^1,5x^2,3x^3")
#affichage_it(addition(p,l))
#affichage_it(addition_rec(p,l))
#affichage_it(addition_ptr(p,l))







        
