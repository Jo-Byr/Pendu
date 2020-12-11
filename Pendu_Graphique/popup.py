#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:46:46 2020

@author: jonathan
"""

from random import choice
from liste_fichier import liste_fichier
from retire_accent import retire_accent
from template_reponse import template_reponse

import tkinter as tk

def open_popup(window,texte,canvas,label_vies,label_a_completer,label_tentatives,label_erreur,label_mot,label_liste):
    """
    Cette fonction fait apparaître un pop up dans la fenere donnée
    window est la fenêtre où faire apapraître le popup
    texte est le texte à y afficher
    canavs est le canvas qu'il faut vider
    label_vis est lelabel où est stocké le nombre de vies restantes
    label_a_completer est le label qui se complete avec les input du joueur
    label_tentatives est le label recevant les tentatives du joueurs
    label_erreur est le label où s'affiche les messages d'erreurs
    label_mot est le label où est stocké le mot cherché
    label_liste est le label où est stocké la liste des lettres à trouver
    """
    
    def restart(canvas,vies,label_a_completer,label_tentatives,label_erreur,label_mot,label_liste):
        """
        Cette fonction prend une partie des arguments de sa fonction mère pour en changer le contenu pour une nouvelle partie
        """
        mots = liste_fichier('liste_francais.txt')
        nouveau_mot = choice(mots)
        nouveau_mot = retire_accent(nouveau_mot[0:len(nouveau_mot)-1])
        canvas.delete('all')
        label_vies['text'] = '8'
        label_mot['text'] = nouveau_mot
        label_a_completer['text'] = template_reponse(nouveau_mot)
        label_liste['text'] = list(nouveau_mot)[1:]
        label_tentatives['text'] = ""
        label_erreur['text'] = ""
        popup.destroy()
    popup = tk.Toplevel(window)
    popup.title('Partie finie')
    label_text = tk.Label(popup,text=texte)
    label_text.pack()
    button_recommencer = tk.Button(popup,text='Nouvelle partie',command=lambda:restart(canvas,label_vies,label_a_completer,label_tentatives,label_erreur,label_mot,label_liste))
    button_recommencer.pack()
    
    button_fermer = tk.Button(popup,text="Quitter",command = lambda:[window.destroy()])
    button_fermer.pack()
    popup.mainloop()