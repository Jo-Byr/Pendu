#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:30:25 2020

@author: jonathan
"""

def retire_liste(s,L):
    """
    s est un string et L une liste de strings.
    Cette fonction retire toutes les occurences de s dans L, sauf la première lettre.
    """
    L2 = [L[0]]
    for k in range(len(L)-1):
        if L[k+1]!=s:
            L2.append(L[k+1])
    return(L2)