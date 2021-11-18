import tkinter as tk

#pour créer une fenêtre
fenetre = tk.Tk()
#fenetre.configure(background='white')

#les éléments qui composent une fenêtre s'appellent des widgets

#premier widget : le label permet d'afficher du texte
label1 = tk.Label(fenetre,text="Nombre de clics : 0")
#placer un widget sur la fenêtre
#row désigne la ligne
#column désigne la colonne
#rowspan indique sur combien de lignes afficher le widget
#columnspan indique sur combien de colonnes afficher le widget
label1.grid(row=1,column=1,columnspan=2)

nb_clics=0

#fonction callback appelée quand on clique sur le bouton
def clic_bouton():
    #par défaut, les variables sont considérées locales dans les fonctions
    #on doit dire à python d'utiliser la variable globale à la place
    global nb_clics
    nb_clics+=1
    label1.config(text="Nombre de clics : "+str(nb_clics))

#deuxième widget : le bouton sur lequel on peut cliquer
bouton1 = tk.Button(fenetre,text="Clique moi !",command=clic_bouton)
bouton1.grid(row=2,column=1)

def reset():
    global nb_clics
    nb_clics=0
    label1.config(text="Nombre de clics : 0")
    
bouton_reset=tk.Button(fenetre,text="reset",command=reset)
bouton_reset.grid(row=2,column=2)

#boucle principale
tk.mainloop()

'''
Exercice:
Ajouter un bouton reset qui remet le compteur à zéro
'''
