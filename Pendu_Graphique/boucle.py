#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:31:18 2020

@author: jonathan
"""

from dessin import dessin
from popup import open_popup

def boucle(window,canvas,label_tentatives,label_erreur,label_a_completer,entry,label_vies,label_mot,label_liste):
    """
    Cette fonction effectue un "tour" de jeu de pendu : demander uner lettre, vérifier si elle fait partie du mot cherché et mettre à jour les différentes valeurs.
    window est la fenêtre de jeu
    canvas le canvas de dessin du pendu
    label_tentatives le label où sont écrites les lettres proposées
    label_erreur celui où sont notés les messages d'erreur (cela comprend aussi les messages de réussite)
    label_a_completer est le label qui se complete avec les propositions du joueur
    entry est l'endroit où le joueur propose une lettre
    label_vies est le label où est stocké le nombre de vies restantes
    label_mot est le label où est stocké le mot actuellement cherché
    label_liste est le label où est stockée la liste des lettres à trouver
    """
    
    proposition = entry.get().lower()
    mot_cherche = label_mot['text']
    liste_a_trouver = label_liste['text']
    
    if proposition in liste_a_trouver:
        #La proposition faite appartient au mot
        for k in range(1,len(mot_cherche)):
            #On vérifie où placer la lettre
            if mot_cherche[k]==proposition:
                #On la place
                text = label_a_completer['text']
                new_text = text[:2*k]+proposition+text[2*k+1:]
                label_a_completer.config(text = new_text)
        label_erreur.config(text = proposition.upper() + " apparaît dans le mot!")
        
        reponse_underscore = label_a_completer['text']
        reponse = ""
        for k in range(len(reponse_underscore)):
            if k%2==0:
                reponse+=reponse_underscore[k]
        if mot_cherche==reponse.lower():
            #Vérification de fin de partie par victoire (pop up si réussite)
            label_erreur.config(text = "Bravo vous avez trouvé!")
            open_popup(window,'Vous avez gagné!',canvas,label_vies,label_a_completer,label_tentatives,label_erreur,label_mot,label_liste)
            return()
        
    #Tests des propositions non valides           
    elif proposition=="":
        label_erreur.config(text = "Veuillez proposer une lettre")
        
    elif len(proposition)>1:
        label_erreur.config(text = "Veuillez ne proposer qu'une lettre à la fois")
        
    else:
        #La proposition est valide mais n'appartient pas au mot
        label_erreur.config(text = proposition.upper() + " n'apparaît pas dans le mot.")
        if int(label_vies['text'])>0 and not(proposition in label_tentatives['text']):
            #Si les vies ne sont pas épuisées ont dessine l'étape suivante
            dessin(canvas,int(label_vies['text']))
            label_vies['text'] = str(int(label_vies['text'])-1)
        if int(label_vies['text'])==0:
            #Sinon un pop up apparaît
            label_erreur.config(text = "Vous avez epuisé vos essais\nLe mot était : " + mot_cherche)
            open_popup(window,'Vous avez épuisé vos tentatives!',canvas,label_vies,label_a_completer,label_tentatives,label_erreur,label_mot,label_liste)
            return()
        
        
    if len(label_tentatives['text'])==0 and len(proposition)==1:
            label_tentatives['text'] = proposition
            
    elif len(label_tentatives['text'])>0 and len(proposition)==1:
        if not(proposition in label_tentatives['text']):
            label_tentatives['text'] = label_tentatives['text']+ ', ' + proposition
