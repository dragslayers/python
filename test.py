print("hello world")
variable1 = 2
variable2 = 5

print(variable1)
print(variable1+variable2)

'''
commentaire plusieurs lignes
'''

#commentaire une ligne

'''

print("la variable contient", variable1, "et c'est bien")

print("abc"+"def")

mastring="abc"+str(3)
print(mastring)

'''

'''
    entree=input("date de naissance?\n")
    entree=2021-int(entree)
    print("tu as ou auras :" , entree)
'''

'''
condition ternaire
a =2 if true else 3
a = 2 if false else 3
'''

'''
entree=int(input("entrez une valeur positive"))
cpt = entree

while entree > 0:
    entree=int(input("entrez une valeur positive"))
    if entree > 0:
        cpt+=entree
    
print("la somme est",cpt)
'''

'''
i=0
somme=0
nombre=0

while nombre != "stop":
        somme+=int(nombre)
        i+=1
        nombre=input("entrez une valeur")
        
if i!=1:
    print("la moyenne est",somme/(i-1))
else:
    print("la moyenne est",somme)
'''

'''
for i in range(0,10):
    print(i*i)

somme=0
entree=0

for i in range(0,4):
    entree=int(input("entrez un nombre"))
    somme+=entree
    

print(somme)
'''


'''
def mafonction(param1,param2):
    variable=param1+param2
    return variable

print(mafonction(1,1))

def affiche_zero():
    print(0)

affiche_zero()
z = affiche_zero()
print(z)
'''

'''
def majeur(annee):
    if 2021-annee >= 18:
        return "majeur"
    return "mineur"

print(majeur(2020))
print(majeur(2000))

def fonction(nb1,nb2):
    if nb1<nb2:
        return nb1+nb2
    return nb1*nb2

print(fonction(1,2))
print(fonction(2,1))

def verifAnneeAge(annee,age):
    return 2021-annee == age

print(verifAnneeAge(2000,21))
print(verifAnneeAge(2005,20))
'''

'''
def occruence(string):
    cpt=0
    for i in string:
        if(i == "e"):
            cpt+=1
    return cpt
print(occruence("eeeeee"))
print(occruence("nombre"))

def voyelles(string1,string2):
    cpt1=0
    cpt2=0
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U","y","Y"}
    for char in string1:
        if any(char in vowels for char in string1):
            cpt1=+1
    for char in string2:
        if any(char in vowels for char in string2):
            cpt2=+1
    return cpt1 > cpt2
    
print(voyelles("qsdf","azertyuio"))
'''
'''
liste=[]
for i in range(3):
    entree=input("entrez une chaine de caractere\n")
    liste.append(entree)

print()
print(liste)

liste2=[]
entree="0"
while entree!="stop":
    liste2.append(int(entree))
    entree=input("entrez un nombre\n")

liste2.remove(0)
print(liste2)
'''
'''
liste=[3,6,2,8,4,3,4,9,3,-2,-1,3]

def minimum(liste):
    res_min = liste[0]
    for elements in liste:
        if(res_min > elements):
            res_min = elements
    return res_min        

print(minimum(liste))

def somme(liste):
    resultat=0
    for elements in liste:
        resultat+=elements
    return resultat

print(somme(liste))

def compte(liste, valeur):
    cpt=0
    for elements in liste:
        if elements==valeur:
            cpt+=1
    return cpt

print(compte(liste,3))

def tous_positifs(liste):
    for elements in liste:
        if elements < 0:
            return False
    return True

print(tous_positifs(liste))

def test(a):
    if a:
        return True

print(test(False))
'''
'''

def divisible(d,n):
    return d%n == 0
     
print(divisible(12,6))
print(divisible(12,7))


def diviseur(n):
    liste=[]
    for i in range(1,n+1):
        if divisible(n,i):
            liste.append(i)

    return liste

print(diviseur(1))

def premier(n):
    return len(diviseur(n)) == 2

print(premier(10))
print(premier(1))

def listepremier():
    liste=[]
    for i in range(0,100):
        if premier(i):
            liste.append(i)
    return liste

print(listepremier())
'''
'''
classe={}
for i in range (3):
    nom=input("entrez un nom\n")
    note=input("entrez une note\n")
    classe[nom] = note
moyenne=0
for cle in classe:
    moyenne += int(classe[cle])

print(moyenne/3)


classe2={}
noms=["Joe","William","Jack","Averell"]

notes=[ [13,17,15,15,13],[12,15,13,12], [11,15,17,14,11,13], [5,8,7,5,6]]

for i in range (len(noms)):
    classe2[noms[i]] = notes[i]
print(classe2)


classe3={}
for i in range (len(noms)):
    moyenne=0
    for j in range(len(notes[i])):
        moyenne+=notes[i][j]
    moyenne/=len(notes[i])
    classe3[noms[i]] = moyenne
print(classe3)


for nom in classe2:
    print(classe2[nom])
    print(sum(classe2[nom]))
    classe3[nom] = sum(classe2[nom])/len(classe2[nom])
print(classe3)
'''

'''
import random

def piece():
    liste=["pile","face"]
    print(random.choice(liste))
piece()


def jeurandom():
    nbr = random.randint(1,100)
    cpt=0
    entree=int(input("devine le nombre\n"))
    while entree !=nbr:
        if(entree > nbr):
            print("plus bas")
            entree=int(input("devine le nombre\n"))
        else:
            print("plus haut")
            entree=int(input("devine le nombre\n"))
        cpt+=1

    print("bravo vous avez trouvé en",cpt,"coups\n")
    print(nbr)

jeurandom()
'''
'''
import matplotlib.pyplot as plt

abscisses = [0,1,5,3,6,9]
ordonnes = [6,8,5,1,5,3]

plt.plot(abscisses,ordonnes,"ro--")

plt.show()
plt.savefig("figure.png")
'''
'''
with open("monfichier.txt","w") as fichier:
    fichier.write("Bonjour")

import random

promo={}
noms=["Joe","William","Jack","Averell","crotte"]
for i in range (len(noms)):
    promo[noms[i]] = random.randint(0,20)

print(promo)

with open("notes.txt","w") as fichier:
    for i in promo:
        fichier.write(i+"\n")
        fichier.write(str(promo[i])+"\n")
with open("notes.txt","r") as fichier:
    print(fichier.read())

newpromo={}

with open("notes.txt","r") as fichier:
    l=fichier.read().splitlines()
print(l)

for i in range(0,len(l),2):
    newpromo[l[i]]=int(l[i+1])
print(newpromo)
print(newpromo == promo)
'''
'''
import tkinter as tk
fenetre = tk.Tk()
fenetre.title("my prog")

texte = tk.StringVar("")
texte2 = tk.StringVar("")
texte3 = tk.StringVar("")

label1 = tk.Label(fenetre,text="nombre de clics : 0")
label1.grid()
nb_clics=0

entry1 = tk.Entry(fenetre,textvariable=texte)
entry1.grid()

label2 = tk.Label(fenetre,textvariable=texte)
label2.grid()


def clic_bouton():
    global nb_clics
    nb_clics+=1
    label1.config(text="nombre de clics : "+str(nb_clics))

def clic_reset():
    global nb_clics
    nb_clics=0
    label1.config(text="nombre de clics : "+str(nb_clics))

bouton1 = tk.Button(fenetre, text="clique moi",command=clic_bouton)
bouton1.grid(row=2,column=1)
bouton2 = tk.Button(fenetre, text="reset",command=clic_reset)
bouton2.grid(row=2,column=2)

label3 = tk.Label(fenetre,text="prenom")
label3.grid(row=4,column=0)

label3 = tk.Label(fenetre,text="mdp")
label3.grid(row=4,column=1)

entry2 = tk.Entry(fenetre,textvariable=texte2)
entry2.grid(row=5,column=0)
entry3 = tk.Entry(fenetre,textvariable=texte3)
entry3.grid(row=5,column=1)

bouton3 = tk.Button(fenetre, text="ok",command=clic)
bouton3.grid(row=5,column=2)

label4 = tk.Label(fenetre,text="entrez ton prénom et clique")
label4.grid(row=6,column=0,columnspan=3)

tk.mainloop()
'''


import tkinter as tk

fenetre = tk.Tk()

canvas = tk.Canvas(fenetre,width=400,height=200,background="white")
canvas.grid()

canvas.create_line(200,0,200,200,fill="blue",width=5)

canvas2 = tk.Canvas(fenetre,width=400,height=200,background="blue")
canvas2.grid()

canvas2.create_line(410,0,0,200,fill="white",width=30)
canvas2.create_line(0,0,410,200,fill="white",width=30)

tk.mainloop()
