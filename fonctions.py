'''
Une fonction a
- un nom
- des paramètres
- éventuellement une valeur de retour
'''

def mafonction(param1,param2):
    variable=param1+param2
    return variable

resultat = mafonction(2,3)
print(resultat)

print(mafonction("ab","cd"))

#le return est facultatif
#par défaut, une fonction renvoie None
def affiche_zero():
    print(0)
    
affiche_zero()
z = affiche_zero()
print(z)

'''
Exercice
Écrire une fonction qui prend en paramètre une annee de
naissance et qui renvoie la chaine de caractère "majeur"
ou "mineur" suivant l'âge de la personne
'''
def majorite(annee):
    if 2021-annee < 18:
        return "mineur"
    else:
        return "majeur"
    
print(majorite(2015))


'''
Exercice
Ecrire une fonction qui prend en paramètre 2 nombres
et qui renvoie leur somme si le premier est strictement
le plus petit des deux,
et leur produit si le premier est le plus grand
'''
def calcul_bizarre(a,b):
    if a<b:
        return a+b
    else:
        return a*b
    
c=calcul_bizarre(9,2)
print(c)
print(calcul_bizarre(2,9))

'''
Exercice
Écrire une fonction qui prend en paramètre une annee
de naissance et un age et qui renvoie un booléen :
True si l'année et l'âge correspondent,
False sinon
'''
def verif(annee,age):
    return 2021-annee == age

print(verif(2020,1))
if verif(2000,21):
    print("C'est bon")
else:
    print("Ca va pas")

'''
Exercice
Ecrire une fonction qui prend en paramètre une str
et qui renvoie le nombre de "e" dans la str
'''
def compte_e(chaine):
    resultat=0
    for lettre in chaine:
        if lettre == "e":
            resultat+=1
    return resultat

print(compte_e("Bebe"))


'''
Exercice
Ecrire une fonction qui prend en paramètre deux str
et qui teste si la première contient plus de voyelles
que la deuxième (renvoie un booléen)
'''
def voyelles(chaine1,chaine2):
    #on compte le nombre de voyelles dans la premiere
    compte1=0
    for lettre in chaine1:
        #on regarde si la lette actuelle est une voyelle
        if lettre in "aeiouyAEIOUY":
            compte1+=1
    #on compte le nombre de voyelles dans la deuxieme
    compte2=0
    for lettre in chaine2:
        #on regarde si la lette actuelle est une voyelle
        if lettre in "aeiouyAEIOUY":
            compte2+=1
    return compte1 > compte2

print(voyelles("Thibaut","Lepage"))
print(voyelles("aaa","bbb"))
