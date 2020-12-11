#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:51:57 2020

@author: jonathan
"""

import tkinter as tk
from random import choice
from retire_accent import retire_accent
from template_reponse import template_reponse
from liste_fichier import liste_fichier
from boucle import boucle

def pendu():
    """
    Cette fonction lance une partie de pendu fenêtrée quand appelée.
    Un label de score est présent mais je n'ai pas eu le temps de le remplir dans le temps imparti
    """
    mots = liste_fichier('liste_francais.txt')
    mot_cherche = choice(mots)
    mot_cherche = retire_accent(mot_cherche[0:len(mot_cherche)-1])  #On retire les accents et le \n à la fin de la ligne
    liste_a_trouver = list(mot_cherche)[1:]
    
    #Création de la fenêtre
    window = tk.Tk()
    window.geometry("900x800")
    
    #Cachés
    """
    Ne pouvant pas modifier la valeur des variables depuis des fonctions externes, je les stocke dans des label cachés dont je modifie les attributs text
    """
    label_mot = tk.Label(window,text=mot_cherche)
    label_mot.config(font = ("Arial",1))
    label_mot.pack(side = tk.LEFT,anchor = tk.SW)
    
    label_liste = tk.Label(window,text = liste_a_trouver)
    label_liste.config(font = ("Arial",1))
    label_liste.pack(side = tk.LEFT,anchor = tk.SW)
    
    label_vies = tk.Label(window,text='8')
    label_vies.config(font = ("Arial",1))
    label_vies.pack(side = tk.LEFT,anchor = tk.SW)
    
    #Bloc de score
    label_score = tk.Label(window,justify=tk.LEFT) #borderwidth et relief permettent de voir les bordures du label
    label_score.config(font=("Arial",12))
    label_score.pack(side = tk.LEFT, anchor = tk.NW)    #le label prendra les dimensions du texte à l'intérieur
    
    #Frame d'interaction (mot cherché, proposition et message d'erreur)
    frame_interaction = tk.Frame(window, borderwidth=2,relief='solid')
    frame_interaction.pack()
    
    #Mot à compléter
    label_a_completer = tk.Label(frame_interaction,text=template_reponse(mot_cherche))
    label_a_completer.config(font=('Arial',16))
    label_a_completer.pack()
    
    #Proposition
    frame_proposition = tk.Frame(frame_interaction, borderwidth=2,relief='solid')
    frame_proposition.pack()
    
    label_consigne = tk.Label(frame_proposition, text = "Proposez une lettre : ")
    label_consigne.pack(side="left")
    
    entry_proposition = tk.Entry(frame_proposition, width=2)
    entry_proposition.pack(side = tk.RIGHT)
    
    #Erreur
    stringvar_erreur = tk.StringVar()
    stringvar_erreur.set('')
    label_erreur = tk.Label(frame_interaction,text = stringvar_erreur.get(),foreground="red")
    label_erreur.pack(side = "bottom")
    
    #Propositions faites
    frame_tentatives = tk.Frame(frame_interaction, borderwidth=2,relief='solid')
    frame_tentatives.pack()
    
    label_tentatives1 = tk.Label(frame_tentatives,text="Lettres déjà proposées : ")
    label_tentatives1.pack()
    
    stringvar_tentatives = tk.StringVar()
    stringvar_tentatives.set('')
    
    label_tentatives2 = tk.Label(frame_tentatives,text=stringvar_tentatives.get())
    label_tentatives2.pack()
    
    #Canvas pour le pendu
    cnv_pendu = tk.Canvas(window,height=500,width=400)
    cnv_pendu.pack(side = tk.BOTTOM)
    
    
    button_proposition = tk.Button(frame_proposition,text="Proposer",command = lambda : boucle(window,cnv_pendu,label_tentatives2,label_erreur,label_a_completer,entry_proposition,label_vies,label_mot,label_liste))
    button_proposition.pack(side = tk.RIGHT)
    
    window.mainloop()