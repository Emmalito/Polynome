#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 11/17/2018
#__version__ : 1.4
#======================================================================================================
from soustraction import *
#======================================================================================================
   
def multiplication_ptr(poly_1,poly_2):
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
                




""" Info : La fonction ptr retourne une liste contenant le développement du produit de poly1 par poly2.
    La fonction aux retourne la somme de ce développement.
    Les fonctions n'ont pas trop été testé, donc il peut y avoir des erreurs.
    Il manque la fonction rec et it.
    Plus généralement s'il y a des erreurs merci de me le faire savoir.
    Désolé si les commentaires sont bourrés de fautes
    Je ne vais pas trop répondre aux questions
    Pour un petit don : https://www.paypal.me/envoimonble/1
    Pour un gros don : https://www.paypal.me/envoimonble/10
    Je vous laisse tester le programme """

    
#a = polynome("0x^0")
#p = polynome("3x^0,0x^1,4x^2")
#l = polynome("2x^0,0x^1,5x^2,3x^3")


#m = multiplication_ptr(l,p)

#m = multiplication_ptr(p,l)

#m = multiplication_ptr(l,a)

#m = multiplication_ptr(a,p)

#affichage_ptr(m)





        
