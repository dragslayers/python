'''
Exercice : jeu du nombre mystère
L'ordinateur tire un nombre N au hasard entre 1 et 100
Puis il demande au joueur de deviner.
Si le joueur donne un nombre plus petit que N,
afficher "plus haut"
Si le joueur donne un nombre plus grand que N,
afficher "plus bas"
Quand le joueur tombe sur N, la partie est terminée.
Afficher le nombre de coups

Mettre ce code dans une fonction
et appeler cette fonction
tant que le joueur veut refaire des parties
'''
import random

def partie():
    nombre_mystere=random.randint(1,100)
    essai=int(input("Devine le nombre entre 1 et 100 : "))
    compteur=1
    while essai != nombre_mystere:
        if essai > nombre_mystere:
            print("Plus bas !")
        else:
            print("Plus haut !")
        essai=int(input("Devine le nombre entre 1 et 100 : "))
        compteur+=1
    print("Bravo ! Tu as trouvé en",compteur,"coups")
    return input("Veux-tu rejouer ? (o/n) ")=="o"
    
while partie():
    print()
