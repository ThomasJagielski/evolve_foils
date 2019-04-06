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


data = evaluateFoil.open_csv('sample16.dat')

# print(data.index)

# print(data.iloc[0,0])

for i in data.index[20:-20]:

    row = data.iloc[i,0]
    row = row.split(' ')
    # print(row)
    x_coord = row[2]
    if row[3] == '':
        y_coord = row[4]
    else:
        y_coord = row[3]
        
    # x_coord = row[2]
    # y_coord = row[3]

    # print(x_coord,y_coord)
    print(float(y_coord))


    # number1 = (random.random()-.5)/10
    number2 = (random.random()-.5)/100



    # number1 = 

    data.iloc[i,0] ='  ' + str(x_coord) + ' ' + str(number2+float(y_coord))




# print(data.iloc[1,0])

# data.iloc[0,0] ='  1.000  .00101'


# print(data.iloc[0,0])
evaluateFoil.save_csv(data)

print(evaluateFoil.call_xfoil())