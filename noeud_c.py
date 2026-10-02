import numpy as np
class Noeud:
    def __init__(self, valeur, enfant = None):
        self.valeur = valeur
        self.enfant = enfant
        if self.enfant is None:
            self.enfant = []
    def ajouter_enfant(self, nouvel_enfant):
        if not isinstance(nouvel_enfant, Noeud):
            raise TypeError ("nouvel_enfant doit etre un Noeud")
        self.enfant.append(nouvel_enfant)
    def affiche(self):
        print(self.valeur)
        for noeud in self.enfant:
            noeud.affiche()
    def evaluer(self, variable):
        if isinstance(self.valeur, (int,float)):
            return self.valeur
        elif self.valeur in variable:
            return variable[self.valeur]
        elif len(self.enfant)>0:
            if self.valeur == "+":
                return self.enfant[0].evaluer(variable) + self.enfant[1].evaluer(variable)
            elif self.valeur == "exp":
                return np.exp(self.enfant[0].evaluer(variable))


deux = Noeud(valeur = 2)
y = Noeud(valeur = "y")
plus = Noeud(valeur = "+", enfant=[deux,y])

exp = Noeud(valeur = "exp")
exp.ajouter_enfant(plus)
exp.affiche()
print(exp.evaluer({"y": 3}))