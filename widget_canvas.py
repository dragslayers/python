import tkinter as tk

fenetre = tk.Tk()

#quatrième widget : le canvas permet de dessiner des formes
#géométriques à l'écran et d'interagir avec l'utilisateur
canvas = tk.Canvas(fenetre,width=400,height=200,background="white")
canvas.grid(row=1,column=1)

#on peut dessiner sur le canvas
#Attention : sur un canvas, les ordonnées vont du haut vers le bas
#exemple : segment entre les points (20,40) et (100,120)
canvas.create_line(20,40,100,120)
#ligne verticale au milieu du canvas
canvas.create_line(200,0,200,200,fill="blue",width=5)

#rectangle en spécifiant la diagonale
canvas.create_rectangle(50,100,100,150,fill="blue",outline="red",width=3)

#ovale en spécifiant la bounding box (rectangle circonscrit)
canvas.create_oval(300,50,330,80,outline="blue")

drapeau = tk.Canvas(fenetre,width=400,height=200,background="blue")
drapeau.grid(row=2,column=1)
drapeau.create_line(0,0,400,200,fill="white",width=40)
drapeau.create_line(0,200,400,0,fill="white",width=40)

#interactivité

#fonction callback appelée à chaque clic sur le canvas
#le paramètre evenement contient entre autres les coordonnées
#du curseur
def clic(evenement):
    print(evenement.x,evenement.y)
    
#demande à tkinter d'associer le clic gauche de la souris
#à notre fonction clic
canvas.bind("<Button-1>",clic)

tk.mainloop()

'''
Exercice
Créer un deuxième canvas sous le premier et dessiner avec deux lignes
le drapeau de l'Ecosse
'''

