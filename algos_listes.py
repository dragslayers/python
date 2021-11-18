liste=[3,6,2,8,4,3,4,9,3,-2,-1,3]
print(liste)
print("min",min(liste))
print("max",max(liste))
print("somme",sum(liste))
print("nb de 3 :",liste.count(3))

'''
Exercice:
Sans utiliser les fonctions ci-dessus, réécrire
ces fonctions avec des boucles
'''
#renvoie le plus petit élément de la liste
#on suppose que la liste n'est pas vide
def minimum(liste):
    resultat=liste[0]
    for element in liste:
        if element<resultat:
            resultat=element
    return resultat
    
print(minimum(liste))
    
#renvoie la somme des éléments de la liste
def somme(liste):
    resultat=0
    for element in liste:
        resultat+=element
    return resultat
    
print(somme(liste))
    
#renvoie le nombre d'occurrences de la valeur dans la liste
def compte(liste,valeur):
    resultat=0
    for element in liste:
        if element == valeur:
            resultat+=1
    return resultat
    
print(compte(liste,3))

#renvoie True si tous les éléments sont >=0
#false si au moins un élément est négatif
def tous_positifs(liste):
    for element in liste:
        if element<0:
            return False
    return True
    
print(tous_positifs(liste))
    
'''
Exercice
Ecrire une fonction qui prend en paramètre
deux entiers n et d et qui teste
si d est un diviseur de n
'''
def divise(n,d):
    return n%d==0

print(divise(12,6))

'''
Exercice
Ecrire une fonction qui prend en paramètre un entier n
et qui renvoie la liste de ses diviseurs
'''

'''
Exercice
Ecrire une fonction qui prend en paramètre un entier n
et qui teste si n est premier
rappel : un nombre premier possède exactement 2 diviseurs
'''

'''
Exercice
Afficher la liste des nombres premiers inférieurs à 100
'''