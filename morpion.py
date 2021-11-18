import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Morpion")

taille_case = 100
marge = 10

canvas = tk.Canvas(fenetre,width=3*taille_case,height=3*taille_case,
                   background="white")
canvas.grid(row=1,column=1)

canvas.create_line(taille_case,0,taille_case,3*taille_case)
canvas.create_line(2*taille_case,0,2*taille_case,3*taille_case)
canvas.create_line(0,taille_case,3*taille_case,taille_case)
canvas.create_line(0,2*taille_case,3*taille_case,2*taille_case)

label=tk.Label(fenetre)
label.grid(row=2,column=1)

#dessine une croix à la position x,y
def croix(x,y):
    canvas.create_line(x+marge,y+marge,
                       x+taille_case-marge,y+taille_case-marge,
                       fill="blue",width=3)
    canvas.create_line(x+marge,y+taille_case-marge,
                       x+taille_case-marge,y+marge,
                       fill="blue",width=3)
    
#dessine un rond à la position x,y
def rond(x,y):
    canvas.create_oval(x+marge,y+marge,
                       x+taille_case-marge,y+taille_case-marge,
                       outline="red",width=3)
    
#renvoie la case contenant le pixel x,y
def case(x,y):
    if x<taille_case:
        colonne=0
    elif x<2*taille_case:
        colonne=1
    else:
        colonne=2
    if y<taille_case:
        ligne=0
    elif y<2*taille_case:
        ligne=1
    else:
        ligne=2
    return (ligne,colonne)

#alternative
def case2(x,y):
    return (y//taille_case,x//taille_case)

#teste les alignements sachant la ligne et la colonne
#où le joueur a joué
def alignement(ligne,colonne):
    #alignement horizontal
    if grille[ligne][0]==grille[ligne][1]==grille[ligne][2]:
        return True
    
    #alignement vertical
    if grille[0][colonne]==grille[1][colonne]==grille[2][colonne]:
        return True
    
    #première diagonale
    if grille[0][0]==grille[1][1]==grille[2][2]!=0:
        return True
    
    #deuxième diagonale
    if grille[0][2]==grille[1][1]==grille[2][0]!=0:
        return True
    
    return False
    
    
#représente l'état du jeu à un instant donné
# 0 représente une case vide
# 1 représente une croix
# 2 représente un rond
grille = [ [0,0,0], [0,0,0], [0,0,0] ]
tour=0
def clic(evenement):
    global tour
    #on trouve la case cliquée
    ligne,colonne=case(evenement.x,evenement.y)
    #on calcule ses coordonnées
    x=colonne*taille_case
    y=ligne*taille_case
    #on teste si la case est vide
    if grille[ligne][colonne] == 0:
        #on alterne croix et rond
        if tour%2==0:
            croix(x,y)
            grille[ligne][colonne]=1
        else:
            rond(x,y)
            grille[ligne][colonne]=2
        if alignement(ligne,colonne):
            label.config(text="Victoire !")
            #on désactive le clic
            canvas.unbind("<Button-1>")
        elif tour==8:#égalité
            label.config(text="Match nul !")
            #on désactive le clic
            canvas.unbind("<Button-1>")
        tour+=1
    
canvas.bind("<Button-1>",clic)

tk.mainloop()
