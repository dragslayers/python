class Personne:
    def __init__(self,nom):
        self.nom = nom
        self.argent=0
        
    def presente_toi(self):
        print("Bonjour, je m'appelle",self.nom)
        
    def get_argent(self):
        return self.argent
        
        
p1 = Personne("Thibaut")
print(p1.nom)

p2=Personne("Toto")
print(p2.nom)
p2.presente_toi()#equivalent à Personne.presente_toi(p2)
print(p2.get_argent())

class Salarie(Personne):
    def __init__(self,nom,fonction):
        super().__init__(nom)
        self.fonction=fonction
        
    def salaire(self,montant):
        self.argent+=montant
        
p3=Salarie("Tutu","CEO")
p3.salaire(1000000)
print(p3.get_argent())

