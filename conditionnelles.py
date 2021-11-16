entree=int(input("Entre un nombre entier : "))

'''
syntaxe :
if condition:
    instructions
    ...
elif condition:
    instructions
    ...
elif ...
else:
    instructions
    ...
'''
'''
les blocs elif et else sont facultatifs
il peut y avoir plusieurs elif mais pas plus d'un else
il n'y a pas de condition dans un else

Attention ! En python, l'indentation a du sens
C'est ce qui délimite les blocs des structures de contrôle
Pour sortir d'un bloc, on désindente les instructions
'''

    
print("première condition")

if entree >= 0:
    print("positif")
else:
    print("negatif")
    
print("deuxième condition")

if entree > 0:
    print("positif")
elif entree < 0:
    print("negatif")
else:
    print("nul")
    
'''
Exercice
demander à l'utilisateur son âge
afficher "mineur" ou "majeur" suivant s'il a moins ou plus
de 18 ans ou afficher "menteur" si le nombre est négatif
ou s'il est plus grand que 130
'''
age=int(input("Quel âge as-tu ? "))
if age < 0 or age > 130:
    print("Menteur")
elif age >= 18:
    print("Majeur")
else:
    print("Mineur")
