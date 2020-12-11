#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:12:38 2020

@author: jonathan
"""

def stringlist_from_str(string):
    """
    string doit être une liste de string sous forme de string '["a","b","c"]' par exemple
    On retourne la liste associée
    """
    L = string.split(',')
    L[-1] = L[-1][:-1]
    for k in range(len(L)):
        L[k] = L[k][2:len(L[k])-1]
    return(L)