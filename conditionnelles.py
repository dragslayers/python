entree=int(input("entrez un nombre : "))


'''
python separe le bloc if via l'indentation
'''


print("premiere condition")

if entree>=0:
    print("positif")
else:
    print("negatif")
    
print("deuxieme condition")

if entree>0:
    print("positif")
elif entree < 0:
    print("negatif")
else:
    print("nul")
