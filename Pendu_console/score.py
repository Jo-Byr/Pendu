#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:05:23 2020

@author: jonathan
"""
from get_int import get_int

def getscore(string):
    """
    Cette fonction récupère les données du fichier de score, de chemin l'argument.
    Ces données sont  : le nombre de victoires successives, le score en cours, le highscore
    """
    file = open(string,'rt')
    rl = file.readlines()
    vic_suite = get_int(rl[0])
    score = get_int(rl[1])
    highscore = get_int(rl[2])
    file.close()
    return(vic_suite,score,highscore)

def newscore(sv,s,hs,chemin):
    """
    Cette fonction modifie les donnée du fichier de score de chemin d'accès le 4e argument.
    Les données à modifier sont le nombre de victoires successives, le score et le highscore selon :
        Victoires successives : sv
        Score : s
        Highscore : hs
    """
    sv = str(sv)
    s = str(s)
    hs = str(hs)
    score_file_w = open(chemin,"wt")
    score_file_w.write("Victoires successives : "+sv+"\n")
    score_file_w.write("Score : "+s+"\n")
    score_file_w.write("Highscore : "+hs+"\n")
    score_file_w.close()