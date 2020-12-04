#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:30:49 2020

@author: jonathan
"""

def retire_accent(lettre):
    """
    Cette fonction reçoit une lettre en argument et en retire l'accent si elle en présente un.
    """
    if lettre in ["é","è","ê","ë"]:
        return('e')
    elif lettre in ['à','â','ä']:
        return('a')
    elif lettre in ['ô','ö']:
        return('o')
    elif lettre in ['ï','î']:
        return('i')
    elif lettre in ['ü','û']:
        return('u')
    else:
        return(lettre)