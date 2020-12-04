#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:31:18 2020

@author: jonathan
"""

from retire_liste import retire_liste

def boucle(reponse,mot,a_trouver,tentatives,vies):
    """
    Cette fonction effectue un "tour" de jeu de pendu : demander uner lettre, vérifier si elle fait partie du mot cherché et mettre à jour les différentes valeurs.
    reponse est le mot à compléter par les inputs du joueur, sous le format A _ _ _ _
    mot est le mot cherché
    a_trouver est la liste des lettres encore à trouver par le joueur
    tentatives est la liste des lettres proposées par le joueur aux tours précédents
    vies est le nombre de vies restantes au joueur
    """
    
    proposition = input("Proposition : ").lower()
    
    while len(proposition)>1:
        print("Veuillez ne proposer qu'une lettre à la fois")
        proposition = input("Proposition : ").lower()
        print("\n")
        
    tentatives += " "+proposition
    
    if proposition in a_trouver:
        print(proposition.upper() + " se trouve dans le mot !")
        a_trouver = retire_liste(proposition,a_trouver)
        liste_reponse = list(reponse)
        for k in range(1,len(mot)):
            if mot[k]==proposition:
                liste_reponse[2*k] = proposition
        reponse = ""
        for k in liste_reponse:
            reponse+=k
    else:
        print(proposition.upper() + " ne se trouve pas dans le mot.")
        vies -= 1
    print("\n")
    return(reponse,mot,a_trouver,tentatives,vies)