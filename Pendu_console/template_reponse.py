#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:29:49 2020

@author: jonathan
"""

def template_reponse(mot):
    """Cette fonction prend un string en argument et retourne un template de reponse du jeu de pendu.
    Par exemple, "python" devient "P _ _ _ _ _"
    """
    reponse = mot[0].upper() #Reponse se remplissant (A _ _ _)
    
    for k in range(len(mot)-1):
        reponse += ' _'
    return(reponse)