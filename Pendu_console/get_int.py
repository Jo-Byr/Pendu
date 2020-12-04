#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:24:13 2020

@author: jonathan
"""

def is_int(string,i):
    try:
        int(string[i])
    except:
        return("Not an int")
    return("Int")

def get_int(string):
    """
    This function takes a string finishing by one or several int and one str
    It returns the int, or the serie of int.
    """
    k=-2;
    while is_int(string,k)=="Int":
        k -= 1
    return(int(string[k+1:-1]))