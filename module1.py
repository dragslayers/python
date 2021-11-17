#renvoie le carré d'un nombre
def carre(x):
    return x**2

#compte le nombre de voyelles dans un texte
def compte_voyelles(texte):
    cpt=0
    for char in texte:
        if char in "aeiouyAEIOUY":
            cpt+=1
    return cpt

'''
la variable __name__ n'a pas la même valeur suivant
la façon dont le module st interprété
S'il est exécuté directement, elle vaut "__main__"
Si le module st importé par un autre, elle vaut le nom
du module
'''
print("__name__ dans le module 1 :",__name__)

'''
Pour executer des instructions seulement si on exécute
directement le module mais pas si on l'importe,
on peut tester la variable __name__
'''
if __name__ == "__main__":
    print(carre(5))
    print(compte_voyelles("Toto"))
