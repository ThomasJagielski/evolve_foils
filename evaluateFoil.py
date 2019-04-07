import subprocess as sp
import shutil
import sys
import string
import time
import pandas as pd
import os


def open_csv(file):
    return pd.read_csv(file)

def save_csv(data):
    data.to_csv('sample16-2.dat', index=False)


def call_xfoil():

    sp.call(['./runx.sh'])

    file = open('results.txt',"r")

    data = file.read()
    file.close()
    open('results.txt', 'w').close()
    data = data.split('-----')

    data = data[-1]
    data = data.split('  ')

    for i in range (10):  # Number of time to try the solver before giving up

        try:
            return data[2], data[3]
        except IndexError:
            pass



if __name__ == "__main__":
    print(call_xfoil())

# data = runXfoil.run_xfoil()


# data = data.split(' ')

# file = open('results.txt',"w")

# # file.write(str(cl))
# # file.write(str(cd))
# file.close()

# os.system('rm -r data_save.txt')

# print(len(data))
# print(data)
