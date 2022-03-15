#range(n) donne l'intervalle [0;n[
for i in range(5):
    print(i)
print()
    
#range(start,stop) donne l'intervalle [start;stop[
for i in range(3,8):
    print(i)
print()

#range(start,stop,step) qui saute step pas à chaque tour
for i in range(6,38,10):
    print(i)
print()

#on peut mettre des steps négatifs
for i in range(5,0,-1):
    print(i)
print()

'''
Exercice
afficher tous les carrés inférieurs ou égaux à 100
'''
for i in range(11):
    print(i**2)

'''
Exercice
Demander 4 nombres et afficher leur somme
'''
somme=0
for i in range(4):
    somme+=float(input("Entre un nombre "))
print(somme)

'''testsetets'''