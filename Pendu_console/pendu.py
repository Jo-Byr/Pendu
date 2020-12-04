#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:46:00 2020

@author: jonathan
"""
'STOP'

from random import choice
from score import newscore,getscore
from template_reponse import template_reponse
from retire_accent import retire_accent
from boucle import boucle
from liste_fichier import liste_fichier
        

def pendu():
    """
    Cette fonction lance une partie du jeu de pendu.
    """
    mots = liste_fichier('liste_francais.txt')
    mot_cherche = choice(mots)
    mot_cherche = retire_accent(mot_cherche[0:len(mot_cherche)-1])  #On retire les accents et le \n à la fin de la ligne
    
    [suc_vic,score,highscore] = getscore("score.txt")
    
    if score>0:
        print('Un score de',score,'est en cours, souhaitez-vous le reprendre ou commencer une nouvelle partie ? ')
        new = input('(Continuer ou Nouveau) ')
        while not(new in ['Continuer','Nouveau']):
             print('Veuillez répondre par "Continuer" ou "Nouveau"')
             new = input('(Continuer ou Nouveau)')
        if new=='Nouveau':
            score=0
            suc_vic=0
        print('\n')
    
    tentatives = ""
    
    vies = 8
    
    liste_a_trouver = list(mot_cherche)[1:] #Liste des lettres a trouver
    
    a_completer = template_reponse(mot_cherche)
    
    print('Mot à trouver :\n' + a_completer)
    
    while vies>0 and liste_a_trouver!=[mot_cherche[0]]:        
        [a_completer,mot_cherche,liste_a_trouver,tentatives,vies] = boucle(a_completer,mot_cherche,liste_a_trouver,tentatives,vies)
        print('Mot à trouver :\n' + a_completer + '\n')
        print("Il vous reste",vies,"tentatives.")
        print("Vous avez déjà proposé les lettres suivantes :",tentatives,'\n')
    if vies==0:
        print("Vies épuisées! Votre score retombe à 0.")
        score = 0
        suc_vic = 0
    else:
        print("Félicitations vous avez trouvé le mot :",mot_cherche)
        suc_vic += 1
        score += suc_vic*vies
        print("Votre score s'élève à :",score)
        if score>highscore:
            highscore = score
            print('Vous avez battu le highscore !')
        newscore(suc_vic,score,highscore,'score.txt')
    
    
    again = input("Une autre partie ? (Oui ou Non)\n")
    while again not in ['Oui','Non']:
        print("Une réponse autre que 'Oui' ou 'Non' ne fonctionnera pas.\n")
        again = input("Une autre partie ? (Oui ou Non)\n")
    if again=="Oui":
        pendu()
    else:
        print("Au revoir.")