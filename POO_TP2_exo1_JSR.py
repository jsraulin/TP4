#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:50:19 2024

@author: seb
"""
liste_test = [0,-2,5,6]
#Exo1:
def afficher(p):
    for i in range(len(p)-1, 0, -1):
        if(p[i] == 0):
            continue
        if i != (len(p)-1):
            if( p[i] < 0):
                print(" - ", end=' ')
            else:
                print(" + ", end=' ')
        print(f"{abs(p[i])} * X^{i}", end=' ')
    if p[0] != 0:
        print(p[0], end='')
    print()
    
def get_valeur(p, x):
    res = 0
    for i in range(len(p)):
        res += p[i] * x**i
    return res
    
def deriver(p):
    pol_der = []
    for i in range(1,len(p)):
        pol_der.append(p[i]*i)
    return pol_der

afficher(liste_test)
print(get_valeur(liste_test, 5))
print(afficher(deriver(liste_test)))
print(deriver(liste_test))
#Test1245abv