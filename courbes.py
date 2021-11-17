#matplotlib permet de tracer des graphiques
import matplotlib.pyplot as plt

#la fonction plot crée un graphe
#on lui donne une liste d'abscisses
#et une liste d'ordonnées
#plus éventuellement des paramètres pour gérer les style
#du graphe

abscisses=[0,1,2,3,4,5]
ordonnees=[-2,3,7,-1,0,3]
y2=[8,8,5,5,3,3]

#le 3e paramètre de plot détermine le style
#c'est une str
#1er caractère : couleur (rgbwkycm)
#2e caractère : style des marqueurs (xo+)
#ensuite : style des traits (- ou --)
plt.plot(abscisses,ordonnees,"ro--",label="données 1")

plt.plot(abscisses,y2,"bx-",label="données 2")

#titre des axes
plt.xlabel("x")
plt.ylabel("y")

#afficher la légende
plt.legend()

#parfois nécessaire pour afficher le graphe
#dépend de l'éditeur
plt.show()
#plt.savefig("figure.png")
