#tout ce qui suit un # est un commentaire

'''
Tout ce qui est entre des triple apostrophes
Est considéré comme commentaires
Ce qui permet d'ecrire des commentaires
sur plusieurs lignes
'''

print("Hello world!")#la fonction print affiche dans le shell ses paramètres

variable1=3
variable2=5

print(variable1)
print(variable1+variable2)

#la fonction print accepte plusieurs paramètres
print("la variable 1 contient la valeur",variable1,
      " et c'est très bien")

#on peut aussi concaténer directement des str
print("abc"+"def")

#conversions de types
mastring="abc"+str(variable1)
print(mastring)
print(int("2")+2)

#la fonction input demande à l'utilisateur d'entrer du texte
entree=input("Quel est ton nom ?\n")
print("Tu as écrit :",entree)

'''
Exercice
Demander à l'utilisateur d'entrer son année de naissance
et afficher quel anniversaire il va fêter en 2021
'''
annee=int(input("Quelle est ton année de naissance ? "))
print("Tu as",2021-annee,"ans")