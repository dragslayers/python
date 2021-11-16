print("hello world")
variable1 = 2
variable2 = 5

print(variable1)
print(variable1+variable2)

'''
commentaire plusieurs lignes
'''

#commentaire une ligne

print("la variable contient", variable1, "et c'est bien")

print("abc"+"def")

mastring="abc"+str(3)
print(mastring)

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

for i in range(0,10):
    print(i*i)

somme=0
entree=0

for i in range(0,4):
    entree=int(input("entrez un nombre"))
    somme+=entree
    

print(somme)
