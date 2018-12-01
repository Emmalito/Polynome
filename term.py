from liste import *

class term(object):
    """Classe définissant un terme d'un polynôme"""

    def __init__(self,puissance = 0, coefficient = 0.0):
        self.p = puissance
        self.coef = coefficient

    def str(self):
        """Conversion d'un terme en str"""
        #Si la puissance est nul on ne renvoi que le coefficient
        if self.p == 0 :        
            return str(self.coef)
        #Si la puissance = 1, on ne renvoi pas la puissance
        if self.p == 1 :
            return str(self.coef)+"x"
        #Sinon on renvoi le terme
        else: 
            return str(self.coef)+"x^"+str(self.p)

    def eq(self,terme):
        """Fonction d'égalité"""
        assert isinstance(terme,term),'Terme doit être un terme'

        #On retourne un booléen 
        return self.p == terme.p and self.coef == terme.coef

    def recup(self,chaine):
        """Transforme une chaîne de caractère en terme"""
        assert isinstance(chaine,str),'Chaine doit être un str'
        # chaine = 'ax^n'   très important
        #On sépare le coefficient et la puissance de la chaine
        chaine = chaine.split("x^")
        #Et on les insère dans le terme
        self.coef = int(chaine[0])
        self.p = int(chaine[1])
        return self
        
            
def polynome(chaine):
    """Fonction transformant une chaine de caractère en polynome"""
    assert isinstance(chaine,str),'Chaine doit être un str'

    # chaine = 'ax^0,bx^1,cx^2,...,dx^n'  très important
    #On sépare les termes du polynomes
    chaine = chaine.split(',')
    terme, poly = term(), liste()
    #Puis on les rentre dans une liste
    for monome in chaine :
        terme.recup(monome)
        poly = construit_liste(terme,poly)
        terme = term()
    #Et on renvoi la liste
    return poly
















    
