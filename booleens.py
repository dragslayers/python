# -*- coding: utf-8 -*-
'''
Toute expression dont le résultat est un booléen
peut être utilisée comme condition dans un if
Exemples :
'''

#comparaisons
print(3>2)
print(5==5)
print(2!=0)
print("abc"!="def")
print()#sert à passer une ligne dans le shell

#appartenance
print("T" in "Thibaut")
print("abc" not in "Thibaut")
print()

#operateurs logiques
print(not False)
print(True and True)
print(True or False)
print(3>2 and "to" in "Toto")
print()

'''
Tables de vérité des opérateurs logiques

x       not x
True    False
False   True

x       y       x and y      x or y
True    True    True         True
True    False   False        True
False   True    False        True
False   False   False        False
'''

