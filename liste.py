class cellule(object):
    def __init__(self,valeur=0,suivant=None):
        #begin
        self.valeur = valeur
        self.suivant = suivant
        #end

class liste(object):
    def __init__(self,cell=None):
        #begin
        self.debut = cell
        #end

    def liste_vide(self):
        #begin
        return self.debut == None
        #end

    def tete(self):
        #begin
        return self.debut.valeur
        #end
    
    def corps(self):
        #begin
        return liste(self.debut.suivant)
        #end
    
    def insere_en_tete(self,valeur):
        #begin
        self.debut = cellule(valeur,self.debut)
        #end

    def construit_liste(self,valeur):
        #begin
        return liste(cellule(valeur,self.debut))
        #end

    def supprime_en_tete(self):
        #begin
        self.debut= self.debut.suivant
        #end

def retourne_liste(l) :
    #Begin
    copy = liste()
    while not l.liste_vide() :
        copy = construit_liste(l.tete(),copy)
        l.supprime_en_tete()
    return copy
    #End

def copy_liste(l) :
    #Begin
    import copy
    return copy.deepcopy(l)
    #End
    
def construit_liste(valeur,l):
    #begin
    return liste(cellule(valeur,l.debut))
    #end
        

