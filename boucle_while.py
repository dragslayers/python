'''
Sert à exécuter des instructions de manière répétitive
tant qu'une condition est remplie

Syntaxe :
while condition:
    instructions
    ...
'''

a=5
i=0

while i<a:
    print(i)
    i=i+1

print("Terminé")

#il existe des operateurs d'incrémentation
a+=1 # equivalent à a=a+1
a+=3
a-=1 # a=a-1
a*=2 #a=a*2
a/=3 #a=a/3

'''
Exercice
Demander d'entrer des nombres positifs ou nuls
s'arrêter dès que l'utilisateur entre un nombre négatif
Afficher la somme des entiers positifs entrés
'''
somme=0
nombre=0
while nombre>=0:
    somme+=nombre
    nombre=int(input("Entre un nombre "))
print(somme)

'''
Exercice
Demander d'entrer des nombres
s'arrêter dès que l'utilisateur entre le mot "stop"
Afficher la moyenne des nombres entrés
'''
somme=0
compteur=0
entree="0"
while entree != "stop":
    somme+=int(entree)
    entree=input("Entre un nombre (stop pour arrêter) ")
    compteur+=1
    
if compteur!=1:
    print(somme/(compteur-1))
    
    
    
    