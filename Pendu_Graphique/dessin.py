#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:56:10 2020

@author: jonathan
"""

def dessin(cnv,n):
    """Cette fonction dessine le pendu etape par etape.
    L'argument cnv est le nom du cnvas où dessiner et n decrit l'etape a dessiner"""
    if n==8:
        cnv.create_line(50,450,250,450) #Base de l'échafaud
    elif n==7:
        cnv.create_line(140,450,140,50) #Pilier de l'échafaud
    elif n==6:
        cnv.create_line(140,50,340,50)  #Barre verticale haute de l'échafaud
    elif n==5:
        cnv.create_line(140,110,200,50) #Support de l'échafaud
    elif n==4:
        cnv.create_line(340,50,340,70)  #Corde
        cnv.create_oval(310,70,370,130) #Tete
    elif n==3:
        cnv.create_line(340,130,340,300) #Corps
    elif n==2:
        cnv.create_line(340,150,355,270) #Premier bras
        cnv.create_line(340,150,325,270) #Deuxieme bras
    else:
        cnv.create_line(340,300,325,410) #Premiere jambe
        cnv.create_line(340,300,355,410) #Deuxieme jambe