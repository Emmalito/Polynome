#======================================================================================================
# Projet polynôme
#-------------------------------------------------------------------------------------------------------
#__author__ : DELAR EMMALITO
#__date__ : 11/10/2018
#__version__ : 1.00
#======================================================================================================
from liste import *
#======================================================================================================

def saisie_polynome():
    """Fonction itérative renvoyant un polynôme saisi au clavier"""

    #Var
    poly = liste()      #liste
    deg,n,a = 0,0,0     #int
    
    #Begin
    print("Polynôme de la forme : a*x^n + b*x^n-1 + ... + t")
    deg = int(input("Entrez le degrés du polynôme : "))
    a = input("Entrez le coefficient du degrés 0 \n")
    poly = construit_liste(a,poly)
    n += 1
    while deg >= n :
        print("Entrez le coefficient du degrés",n," ")
        a = input()
        if n == 1:
            poly = construit_liste(a+"x",poly)
            n += 1
        else:
            poly = construit_liste(a+"x^"+str(n),poly)
            n += 1
    return poly
    #End
#-------------------------------------------------------------------------------------------------------

def saisie_polynome_rec(poly="init",deg="init",n="init_"):
    """Fonction récursive renvoyant un polynôme saisi au clavier"""

    #Var
    #deg,n,a => int  poly => liste

    #Begin
    if deg != "init" and deg < n:
        return poly
    else :
        if deg == "init" :
            poly,n = liste(),0
            deg = int(input("Entrez le degrés du polynôme : "))
            a = input("Entrez le coefficient du degrés 0 \n")
            poly = construit_liste(a,poly)
            return saisie_polynome_rec(poly,deg,n+1)
        while deg >= n:
            print("Entrez le coefficient du degrés",n," ")
            a = input()
            poly = construit_liste(a+"x^"+str(n),poly)
            return saisie_polynome_rec(poly,deg,n+1)
    #End
        
#======================================================================================================

def affichage_rec(poly):
    """Fonction récursive affichant le polynôme poly"""
    assert isinstance(poly,liste), "Erreur, le polynôme doit être une liste"

    #Begin
    if not poly.corps().liste_vide():
        print(poly.tete(),end=' + ')
        affichage(poly.corps())
    else :
        print(poly.tete())
    #End
#-------------------------------------------------------------------------------------------------------

def affichage_it(poly):
    """Fonction itérative affichant le polynôme poly"""
    assert isinstance(poly,liste), "Erreur, le polynôme doit être une liste"

    #Begin
    while not poly.corps().liste_vide():
        print(poly.tete(),end=' + ')
        poly = poly.corps()
    else :
        print(poly.tete())
    #End

#======================================================================================================






"""poly = liste()
poly = construit_liste("2",poly)
poly = construit_liste("3x",poly)
poly = construit_liste("4x^2",poly)
poly = construit_liste("3x^3",poly)
affichage_it(poly)"""






