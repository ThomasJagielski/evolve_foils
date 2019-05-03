"""
Use cosine spacing on the hydrofoil for a better chance of passing through the xfoil simulation
"""
import random
import string
import sys
import numpy as np   # Used for statistics

from deap import algorithms
from deap import base
from deap import tools

def create_x():
    """
    Implement cosine spacing. Creates a x spacing 
    with a higher density at the leading and 
    trailing edges where curvature is high.

    The spacing is saved in a text file and loaded 
    when the function is called
    """
    text = open('sample16.dat', 'r')
    text = text.read()
    text = text.split()

    new_text = []
    for i in range(2,len(text)-1,2):
        new_text.append(float(text[i]))

    new_text = new_text[:-1]

    return(new_text)