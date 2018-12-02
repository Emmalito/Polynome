#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 11/23/2018
#__version__ : 2.1
#======================================================================================================
from soustraction import *
#======================================================================================================

def multiplication_it(poly_1,poly_2) :
    """ Fonction recursive retournat une liste contenant le developpement du produit de poly_1 par
        poly_2 """
    assert isinstance (poly_1,liste),"Le polynôme doit être une liste"
    assert isinstance (poly_2,liste),"Le polynôme doit être une liste"

    #Var
    copy_poly_2, prod1, produit = liste(), liste(), liste() #Liste
    
    #Begin
    copy_poly_2 = copy_liste(poly_2)    #On copie poly_2 à l'aide d'une primitive de liste
    prod1 = liste()                 #On crée une liste pour le produit de poly_1.tete * poly_2
    while not poly_1.liste_vide() :    #Tant qu'on a pas développé tout le produit
        #begin
        copy_poly_2 = copy_liste(poly_2)    #On copie poly_2 à l'aide d'une primitive de liste
        prod1 = liste()                 #On crée une liste pour le produit de poly_1.tete * poly_2
        while not copy_poly_2.liste_vide() :  #Tant qu'on a pas multiplié le terme de poly1 par poly2
            #begin
            copy_poly_2.tete().coef = copy_poly_2.tete().coef * poly_1.tete().coef
            copy_poly_2.tete().p = copy_poly_2.tete().p + poly_1.tete().p
            prod1 = construit_liste(copy_poly_2.tete(),prod1)  #On insere le résultat dans une liste
            copy_poly_2.supprime_en_tete()
            #end
        produit = construit_liste(retourne_liste(prod1),produit) #On insere le developpement dans une liste
        poly_1 = poly_1.corps() #On recommence avec le terme suivant
        #end
    return multiplication_aux(produit)  #On retourne la liste du developpement du produit(poly1*poly2)
    #End

#======================================================================================================

def multiplication_rec(poly_1,poly_2,produit=liste()) :
    """ Fonction recursive retournat une liste contenant le developpement du produit de poly_1 par
        poly_2 """
    assert isinstance (poly_1,liste),"Le polynôme doit être une liste"
    assert isinstance (poly_2,liste),"Le polynôme doit être une liste"

    #Begin
    copy_poly_2 = copy_liste(poly_2)    #On copie poly_2 à l'aide d'une primitive de liste
    prod1 = liste()                 #On crée une liste pour le produit de poly_1.tete * poly_2
    if not poly_1.liste_vide() :    #Tant qu'on a pas développé tout le produit
        #begin
        while not copy_poly_2.liste_vide() :  #Tant qu'on a pas multiplié le terme de poly1 par poly2
            #begin
            copy_poly_2.tete().coef = copy_poly_2.tete().coef * poly_1.tete().coef
            copy_poly_2.tete().p = copy_poly_2.tete().p + poly_1.tete().p
            prod1 = construit_liste(copy_poly_2.tete(),prod1)  #On insere le résultat dans une liste
            copy_poly_2.supprime_en_tete()
            #end
        produit = construit_liste(retourne_liste(prod1),produit) #On insere le developpement dans une liste
        return multiplication_rec(poly_1.corps(),poly_2,produit) #On rappel la fonction
        #end
    else :
        return multiplication_aux(produit)  #On retourne la liste du developpement du produit(poly1*poly2)
    #End

#======================================================================================================
    
def multiplication_ptr(poly_1,poly_2) :
    """ Fonction retournant le développement du produit entre poly_1 et poly_2 à l'aide de la
        structure des listes """
    assert isinstance (poly_1,liste),"Le polynôme doit être une liste"
    assert isinstance (poly_2,liste),"Le polynôme doit être une liste"

    #Var
    produit,prod1 = liste(),liste()     #Liste
    terme = term()                      #Terme
    prt_1,ptr_2 = None,None             #Pointeur


    #Begin
    ptr_1, ptr_2 = poly_1.debut, poly_2.debut   #On place les pointeurs aux début des listes
    #produit.debut = cellule(term(0,0),produit.debut) #Le produit = polynome nul
    while ptr_1 != None :           #Tant qu'on a pas parcouru poly_1
        #begin
        prod1 = liste()
        while ptr_2 != None :       #On parcours le poly_2
            #begin
            terme = term()
            terme.coef = ptr_1.valeur.coef * ptr_2.valeur.coef #On multiplie les coef entre eux
            terme.p = ptr_1.valeur.p + ptr_2.valeur.p  #On additionne les puissances entres elles
            prod1.debut = cellule(terme,prod1.debut) #On ajoute le nvx terme dans une liste
            ptr_2 = ptr_2.suivant  #on passe au terme suivant de poly2
            #end
        #Une fois qu'on a fait le produit du terme de poly1 par poly2
        ptr_1,ptr_2 = ptr_1.suivant, poly_2.debut   #On passe au terme suivant
        prod1 = retourne_liste(prod1) #On retourne la liste du produit
        produit.debut = cellule(prod1,produit.debut) #On met la liste dans une autre liste
        #end
    return multiplication_aux(produit) #Puis on va additionner les produit des termes
    #End

#======================================================================================================

def multiplication_aux(produit):
    """Fonction auxilliaire renvoyant la somme des polynômes composant le produit"""

    #Begin
    #S'il n'y a qu'un seul élément dans la liste produit, on le renvoi
    if produit.corps().liste_vide():
        return produit.tete()
    else :  #Sinon on additionne les 2 premiers éléments qu'on supprime 
        poly_1, poly_2 = produit.tete(), produit.corps().tete()
        produit.supprime_en_tete(), produit.supprime_en_tete()
        produit = construit_liste(addition(poly_1,poly_2),produit)   #On met la somme dans la liste
        return multiplication_aux(produit)     #Puis on rappel la fonction
    #End
                




""" Info : Les fonction it,rec et ptr,retournent une liste contenant le développement du produit de poly1 par poly2.
    La fonction aux retourne la somme de ce développement.
    Les fonctions n'ont pas trop été testé, donc il peut y avoir des erreurs.
    J'ai créé une nouvelle primitive des listes, copy_liste, qui permet de copier une liste dans un autre répertoire,
    ce qui permet de modifier la copie sans modifier l'original.
    Je vous laisse tester le programme """

    
#a = polynome("0x^0")
#p = polynome("3x^0,0x^1,4x^2")
#l = polynome("2x^0,0x^1,5x^2,3x^3")


#m = multiplication_it(l,p)

#m = multiplication_ptr(p,l)

#m = multiplication_ptr(l,a)

#m = multiplication_ptr(a,p)

#affichage_ptr(m)





        
