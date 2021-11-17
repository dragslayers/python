import math

print("math")
print(math.sqrt(9))
print(math.pi)



import time

print("time")
# #bloquer l'exécution pendant un certain temps
# print("a")
# time.sleep(2)
# print("b")

# #mesurer des durées
# t1=time.time()
# reponse=input("Que vaut 2+2 ? ")
# t2=time.time()
# if reponse=="4":
#     print("OK !")
# else:
#     print("C'est faux !")
# print("Tu as mis",t2-t1,"secondes pour répondre")



import random

print("random")
#génère un entier aléatoire entre a et b inclus
print(random.randint(5,10))
print(random.randint(5,10))
print(random.randint(5,10))

#simuler un lancer de dé
print(random.randint(1,6))

#génère un float aléatoire entre 0 et 1
print(random.random())

#tire au hasard un élément dans une liste
liste=["a","b","c","d"]
print(random.choice(liste))

'''
Exercice
Ecrire une fonction qui ne prend pas de paramètre
et qui renvoie "pile" ou "face" aléatoirement
avec une chance sur 2 de renvoyer "pile"
et une chance sur 2 de renvoyer "face"
'''
def pileouface1():
    if random.randint(0,1)==0:
        return "pile"
    else:
        return "face"
    
def pileouface2():
    return random.choice(["pile","face"])

print(pileouface1())
print(pileouface2())
