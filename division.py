#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 12/2/2018
#__version__ : 1.0
#======================================================================================================
from multiplication import *
#======================================================================================================

def division_it(poly_1,poly_2) :
    """ Fonction retournant le quotient de la division euclidienne de poly_1 par poly_2 """
    assert isinstance(poly_1,liste),'Poly_1 doit être une liste'
    assert isinstance(poly_2,liste),'Poly_2 doit être une liste'

    #Var
    quotient, poly, copy_poly_2 = liste(), liste(), liste()   #Liste
    terme = term()                      #Terme

    #Begin
    if poly_1.tete().p < poly_2.tete().p :  #Si le degré du diviseur est superieur à celui du dividende
        quotient = construit_liste(terme,quotient)
        return quotient                     #On retourne le polynome nul
    while poly_1.tete().p >= poly_2.tete().p :  #Tant que le degré du dividende est superieur à celui du diviseur
        #begin
        copy_poly_2 = copy_liste(poly_2)    #On crée une copie de poly_2
        terme, poly = term(), liste()       #On crée le monôme tel que poly1_tete = poly2_tete
        terme.p = poly_1.tete().p - poly_2.tete().p
        terme.coef = poly_1.tete().coef / poly_2.tete().coef
        poly = construit_liste(terme,poly)  
        quotient = construit_liste(terme,quotient)  #On ajoute le monôme au quotient
        #On soustrait le produit du monôme fois poly_2 à poly_1
        poly_1 = soustraction(poly_1,multiplication_it(copy_poly_2,poly)) 
        while poly_1.tete().coef == 0 :     #On supprime les termes à coefficient nul
            poly_1.supprime_en_tete()
        #end
    return retourne_liste(quotient)    #On retourne le quotient
    #End

#======================================================================================================

def division_rec(poly_1,poly_2,quotient=liste()) :
    """ Fonction recursive retournant le quotient de la division euclidienne de poly_1 par poly_2 """
    assert isinstance(poly_1,liste),'Poly_1 doit être une liste'
    assert isinstance(poly_2,liste),'Poly_2 doit être une liste'

    #Begin
    if poly_1.tete().p < poly_2.tete().p :   #Si le degré du diviseur est superieur à celui du dividende
        if quotient.liste_vide() :           #Si le quotient est une liste vide
            quotient = construit_liste(term(),quotient) #Il devient le polynôme nul
        return quotient                      #On retourne le polynome
    else :
        #begin
        copy_poly_2 = copy_liste(poly_2)    
        terme, poly = term(), liste()       
        terme.p = poly_1.tete().p - poly_2.tete().p
        terme.coef = poly_1.tete().coef / poly_2.tete().coef
        poly = construit_liste(terme,poly)  
        quotient = construit_liste(terme,quotient)  
        poly_1 = soustraction(poly_1,multiplication_it(copy_poly_2,poly)) 
        while poly_1.tete().coef == 0 :    
            poly_1.supprime_en_tete()
        return division_rec(poly_1,poly_2,quotient)  #On rappel la fonction
        #End

#======================================================================================================

def division_it(poly_1,poly_2) :
    """Fonction retournant le quotient de la division euclidienne de poly_1 par poly_2 en utilisant
        la structure des listes """
    assert isinstance(poly_1,liste),'Poly_1 doit être une liste'
    assert isinstance(poly_2,liste),'Poly_2 doit être une liste'

    #Var
    quotient,poly,copy_poly_2 = liste(), liste(), liste()   #Liste
    terme = term()                      #Terme
    ptr_1, ptr_2 = None, None           #Pointeur

    #Begin
    ptr_1, ptr_2 = poly_1.debut, poly_2.debut
    if ptr_1.valeur.p < ptr_2.valeur.p :
        quotient.debut = cellule(terme,quotient.debut)
        return quotient
    while ptr_1.valeur.p >= ptr_2.valeur.p :
        #begin
        copy_poly_2 = copy_liste(poly_2)    
        terme, poly = term(), liste()       
        terme.p = ptr_1.valeur.p - ptr_2.valeur.p
        terme.coef = ptr_1.valeur.coef / ptr_2.valeur.coef
        poly.debut = cellule(terme,poly.debut)  
        quotient.debut = cellule(terme,quotient.debut)  
        poly_1 = soustraction(poly_1,multiplication_it(copy_poly_2,poly)) 
        while ptr_1.valeur.coef == 0 :     
            ptr_1 = ptr_1.suivant
        #end
    return retourne_liste(quotient)  
    






""" J'utilise 2 primitives des listes dans la fonction ptr, copy_liste et retourne_liste.
    Je n'ai pas trop testé la fonction encore une fois donc il se peut qu'il y a des erreurs.
    J'ai corrigé la fonction soustraction, donc si ce n'est pas fait téléchargé la màj.
    Encore une fois j'ai moins commenté les fonctions rec et ptr car il n'y a rien de nouveaux.
    Plus généralement s'il y a des erreurs merci de me le faire savoir.
    Désolé si les commentaires sont bourrés de fautes
    Je ne vais pas trop répondre aux questions
    Pour un petit don : https://www.paypal.me/envoimonble/1
    Pour un gros don : https://www.paypal.me/envoimonble/10
    Je vous laisse tester les fonctions """



#p = polynome("1x^0,-2x^1,-1x^2,2x^3")
#l = polynome("1x^0,1x^1,1x^2")
#m = division_it(p,l)
#affichage_ptr(m)



