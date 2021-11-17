#pour écrire dans un fichier
with open("monfichier.txt","w") as fichier:
    fichier.write("Salut\n")
    fichier.write("Ca va ?\n")
    
#pour écrire à la fin d'un fichier sans écraser le reste
with open("monfichier.txt","a") as fichier:
    fichier.write("Troisième ligne\n")
    
#pour lire un fichier
with open("monfichier.txt","r") as fichier:
    a=fichier.read()
print(a)

#lire un fichier ligne par ligne
with open("monfichier.txt","r") as fichier:
    lignes=fichier.readlines()
print(lignes)

#pour ne pas avoir de \n
with open("monfichier.txt","r") as fichier:
    l=fichier.read().splitlines()
print(l)

'''
Exercice
Créer un dictionnaire de 5 éléments
dont les clés sont des noms
et les valeurs sont des notes.
Les notes sont prises au hasard entre 0 et 20
'''
import random
noms=["Frodo","Sam","Merry","Pippin","Bilbo"]
notes1={}
for nom in noms:
    notes1[nom]=random.randint(0,20)
print(notes1)

'''
Exercice
Sauvegarder ces données dans un fichier notes.txt
avec un nom sur la première ligne, puis une note sur
la deuxième, puis un nom sur la troisième, etc.
'''
with open("notes.txt","w") as fichier:
    for nom in notes1:
        fichier.write(nom+"\n")
        fichier.write(str(notes1[nom])+"\n")

'''
Exercice
Lire le fichier et reconstruire un autre dictionnaire
à partir des données
Le nouveau dictionnaire doit être identique
au premier
'''
with open("notes.txt","r") as fichier:
    lignes=fichier.read().splitlines()
print()
print(lignes)
print()
notes2={}
for i in range(0,len(lignes),2):
    notes2[lignes[i]]=int(lignes[i+1])
print(notes2)
print(notes1==notes2)
