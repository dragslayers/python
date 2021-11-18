import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Connexion")

label1 = tk.Label(fenetre,text="Prénom :")
label1.grid(row=1,column=1)

#une stringvar permet de communiquer entre widgets avec des str
texte = tk.StringVar()
#il existe aussi des IntVar et des FloatVar

#troisième widget : Entry pour entrer du texte
#le paramètre textvariable indique la StringVar à modifier
entry1 = tk.Entry(fenetre,textvariable=texte)
entry1.grid(row=1,column=2)

labelmdp = tk.Label(fenetre,text="Mot de passe :")
labelmdp.grid(row=2,column=1)

mdp = tk.StringVar()

entrymdp = tk.Entry(fenetre,textvariable=mdp)
entrymdp.grid(row=2,column=2)

def clic():
    #la méthode get de StringVar renvoie une str
    #avec le contenu actuel de la StringVar
    if mdp.get() == "azerty":
        label2.config(text="Bienvenue "+texte.get())
    else:
        label2.config(text="mot de passe incorrect")

bouton1 = tk.Button(fenetre,text="OK",command=clic)
bouton1.grid(row=2,column=3)

label2 = tk.Label(fenetre,text="Entre ton prénom et clique sur OK")
label2.grid(row=3,column=1,columnspan=3)


tk.mainloop()

'''
Exercice
Ajouter un autre champ qui demande le mot de passe
Quand on clique sur OK,
si le mot de passe est azerty, le label souhaite
la bienvenue à l'utilisateur
Sinon, il dit "mot de passe incorrect"
'''
