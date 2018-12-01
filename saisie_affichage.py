#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 11/17/2018
#__version__ : 2.1
#======================================================================================================
from term import *
#======================================================================================================

def saisie_polynome():
    """ Fonction itérative renvoyant un polynôme saisi au clavier """

    #Var
    poly = liste()      #Liste
    deg,pui = 0,0       #Int
    terme = term()      #Terme 

    #Begin
    print("Polynôme de la forme : a*x^n + b*x^n-1 + ... + t")
    #On demande le degrés du polynôme
    deg = int(input("Entrez le degré du polynôme : "))         
    #On récupère les termes du polynôme dans une liste tant qu'on a pas atteint le degré maximal 
    while deg >= pui :                                          
        #begin
        print("Entrez le coefficient du degré",pui," ")
        terme.coef = int(input())
        terme.p = pui
        poly = construit_liste(terme,poly)      #On utilise une primitive des listes
        pui,terme = pui+1,term()                #On passe à la puissance suivante et on réinitialise le terme
        #end
    #On retourne le polynome
    return poly             
    #End

#-------------------------------------------------------------------------------------------------------

def saisie_polynome_rec(poly="init",deg="init",pui="init_"):
    """ Fonction récursive renvoyant un polynôme saisi au clavier """

    #Var
    terme = term()    #Terme

    #Begin
    #Si on a atteint le degré maximal on retourne le polynôme
    if deg != "init" and deg < pui:
        return poly
    else :
        #begin
        #Si on a pas le degré du polynôme on le récupère
        if deg == "init" :
            poly,pui = liste(),0
            print("Polynôme de la forme : a*x^n + b*x^n-1 + ... + t")
            deg = int(input("Entrez le degrés du polynôme : "))
        #On récupère le terme du polynôme de degré pui dans une liste puis on rappel la fonction 
        #pour la puissance suivante
        while deg >= pui:
            print("Entrez le coefficient du degrés",pui," ")
            terme.coef = int(input())
            terme.p = pui
            poly = construit_liste(terme,poly)
            return saisie_polynome_rec(poly,deg,pui+1)
        #end
    #End

#-------------------------------------------------------------------------------------------------------

def saisie_polynome_ptr():
    """ Fonction renvoyant un polynôme saisi au clavier à l'aide de la structure
        de donnée des listes """

    #Var
    poly = liste()      #Liste
    deg,pui = 0,0       #Int
    terme = term()      #Terme 

    #Begin
    print("Polynôme de la forme : a*x^n + b*x^n-1 + ... + t")
    #On récupère le degré du polynôme
    deg = int(input("Entrez le degrés du polynôme : "))
    #On récupère les termes du polynôme dans une liste tant qu'on a pas atteint le degré maximal 
    while deg >= pui :
        #begin
        print("Entrez le coefficient du degrés",pui," ")
        terme.coef = int(input())
        terme.p = pui
        poly.debut = cellule(terme,poly.debut)      #On enchaîne le nouveaux terme à ceux existant
        pui,terme = pui+1, term()
        #end
    return poly
    #End
        
#======================================================================================================

def affichage_it(poly):
    """Fonction itérative affichant le polynôme poly"""
    assert isinstance(poly,liste), "Erreur, le polynôme doit être une liste"

    #Begin
    #Tant que le corps de la liste n'est pas vide, on affiche le terme suivi d'un +
    while not poly.corps().liste_vide():
        print(poly.tete().str(),end=' + ')      #On utilise la méthode str des termes
        poly = poly.corps()
    #On affiche le dernier terme sans "+" à la fin
    print(poly.tete().str())
    #End
        
#-------------------------------------------------------------------------------------------------------

def affichage_rec(poly):
    """Fonction récursive affichant le polynôme poly"""
    assert isinstance(poly,liste), "Erreur, le polynôme doit être une liste"

    #Begin
    #Tant que le corps de la liste n'est pas vide, on affiche le terme suivi d'un + puis on rappel
    #la fonction
    if not poly.corps().liste_vide():
        print(poly.tete().str(),end=' + ')
        return affichage_rec(poly.corps())
    #On affiche le dernier terme sans "+" à la fin
    print(poly.tete().str())
    #End
        
#-------------------------------------------------------------------------------------------------------

def affichage_ptr(poly):
    """Fonction affichant le polynôme poly à l'aide de la structure des listes"""
    assert isinstance(poly,liste), "Erreur, le polynôme doit être une liste"

    #Var
    ptr = None      #Pointeur
    
    #Begin
    ptr = poly.debut    #On place le pointeur sur le 1er terme
    #Tant que la cellule pointée a un voisin, on affiche le terme suivit d'un "+"
    while ptr.suivant != None :
        print(ptr.valeur.str(),end = ' + ')
        ptr = ptr.suivant
    #On affiche le dernier terme sans le "+"
    print(ptr.valeur.str())
    #End


""" Info : Le polynome nul est le terme (0,0) ==> ce n'est pas une liste vide. On ne va donc pas taité
    les cas où l'on reçoit des listes vide !!!!
    Les termes des polynômes appartiennent à la classe term.
    Les programes peuvent être plus simple, ils ont été complexifiés volontairement.
    Les programmes ont été conçus pour avoir le moins de ligne de code possible, cependant on peut surement
    les alléger.
    Chaque programme possède 3 versions : une itérative, une récursive et une avec les structures des listes.
    Pour le numéro de version X.xy :  X => Nombre de gros changement  x => nombre de changement important
    y => nombre de changement à souligner.
    Je laisse de quoi tester les fonctions ci-dessous """

#poly = saisie_polynome()
#poly_2 = saisie_polynome_rec()
#poly_3 = saisie_polynome_it()
#affichage_rec(poly)
#affichage_ptr(poly_2)
#affichage_it(poly_3)







