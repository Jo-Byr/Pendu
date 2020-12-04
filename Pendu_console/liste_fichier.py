#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 05:05:36 2020

@author: jonathan
"""

def liste_fichier(chemin):
    """
    Cette fonction retourne une liste des mots présents dans un fichier.
    Afin que la liste soit au format attendu, il faut que les mots soient présentés ligne par ligne
    """
    with open(chemin,encoding = "ISO-8859-1") as fichier:
        mots=[]
        for k in fichier:
            mots.append(k)    
        return(mots)