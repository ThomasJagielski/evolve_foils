"""
Isolate the coefficient of drag and coefficient of lift from the results of the xfoil simulation
"""
import subprocess as sp
import shutil
import sys
import string
import time
import pandas as pd
import os
import evaluateFoil
import random
import numpy as np

data = evaluateFoil.open_csv('sample16.dat') # Open the results file


for i in data.index[20:-20]:
    # Split the results by row
    row = data.iloc[i,0]
    row = row.split(' ')

    x_coord = row[2]
    if row[3] == '':
        y_coord = row[4]
    else:
        y_coord = row[3]
        

    print(float(y_coord))



    number2 = (random.random()-.5)/100




    data.iloc[i,0] = '  ' + str(x_coord) + ' ' + str(number2 + float(y_coord))

evaluateFoil.save_csv(data)

print(evaluateFoil.call_xfoil())