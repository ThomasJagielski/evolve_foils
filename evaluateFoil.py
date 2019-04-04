import subprocess as sp
import shutil
import sys
import string
import time
import pandas as pd
import runXfoil
import os

# file = open('sample16.dat',"r")

# data = file.read()
# file.close()
data = pd.read_csv('sample16.dat')

print(data)

data.to_csv('sample16-2.dat', index=False)



sp.call(['./runx.sh'])



file = open('results.txt',"r")

data = file.read()
file.close()
data = data.split('-----')

data = data[-1]
data = data.split('  ')

print(data[2], data[3])


# data = runXfoil.run_xfoil()


# data = data.split(' ')

# file = open('results.txt',"w")

# # file.write(str(cl))
# # file.write(str(cd))
# file.close()

# os.system('rm -r data_save.txt')

# print(len(data))
# print(data)
