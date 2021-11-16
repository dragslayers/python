#une liste est une collection d'objets indexés
liste1 = [5, 7, "toto", True, -2.7]
print(liste1)

#on accède à un élément par son indice
print(liste1[0])
print(liste1[1])
#on peut compter à partir de la fin
print(liste1[-1])
print(liste1[-2])

#concaténation
print([3,2,1]+[6,5,4])

#ajout d'un élément en fin de liste
liste1.append("dernier")
print(liste1)

#taille d'une liste
print(len(liste1))

#enlever un élément
liste1.remove("toto")
print(liste1)
print()

#on parcourt souvent des listes avec des boucles for

#parcours par valeur
for element in liste1:
    print(element)
print()
    
#parcours par indice
for i in range(len(liste1)):
    print(i,liste1[i])
print()

#création de liste élément par élément
liste2=[]
for i in range(7):
    liste2.append(i**2)
print(liste2)
print()


'''
Exercice
Créer une liste et la remplir avec trois str
données par l'utilisateur
'''
liste3=[]
for i in range(3):
    liste3.append(input("Entre ce que tu veux : "))
print(liste3)
print()

'''
Exercice
Créer une liste et la remplir avec des nombres
donnés par l'utilisateur jusqu'à ce qu'il entre
le mot "stop"
'''
liste4=[]
entree=input("Entre un nombre (stop pour arrêter) : ")
while entree!="stop":
    liste4.append(int(entree))
    entree=input("Entre un nombre (stop pour arrêter) : ")
print(liste4)
print()
