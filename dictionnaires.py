#un dictionnaire est une collection d'objets
#repérés par une clé
#les valeurs peuvent être de n'importe quel type
#les clés peuvent être de différents types
#qui doivent être "hashable", c'est à dire qu'on peut
#comparer deux éléments de ce type
repertoire={"Thibaut":"0608418540",
            "Toto":"0704584554",
            "Tata":"010754565"}

#pour accéder à un élément
print(repertoire["Thibaut"])
repertoire["Thibaut"]="0604152557"
print(repertoire["Thibaut"])

#pour ajouter un élément
repertoire["Tutu"]="070542545"
print(repertoire)

#pour parcourir un dictionnaire:
for cle in repertoire:
    print("cle :",cle,"valeur :",repertoire[cle])
    
'''
Exercice
Demander à l'utilisateur de rentrer 3 noms et 3 notes et
créer un dictionnaire dont les clés sont les noms
et les valeurs sont les notes
puis calculer la moyenne de la classe
'''
# notes_evaluation={}
# for i in range(3):
#     cle=input("Nom ? ")
#     valeur=int(input("Note ? "))
#     notes_evaluation[cle]=valeur
    
# #on calcule la moyenne
# somme=0
# for cle in notes_evaluation:
#     somme+=notes_evaluation[cle]
# print(somme/len(notes_evaluation))


'''
Exercice
Créer un dictionnaire dont les clés sont les noms
et les valeurs sont les listes de notes
à partir des listes suivantes:
'''
noms=["Joe","William","Jack","Averell"]
notes=[ [13,17,15,15,13],
      [12,15,13,12],
      [11,15,17,14,11,13],
      [5,8,7,5,6]]
notes_dalton={}
for i in range(len(noms)):
    notes_dalton[noms[i]]=notes[i]
    
print(notes_dalton)

'''
Exercice
Créer un dictionnaire dont les clés sont les noms des 4
élèves précédents et les valeurs sont leurs moyennes.
'''
moyennes_dalton={}
for nom in notes_dalton:
    moyennes_dalton[nom]=sum(notes_dalton[nom])/len(notes_dalton[nom])
print(moyennes_dalton)
