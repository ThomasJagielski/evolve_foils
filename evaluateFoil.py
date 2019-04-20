import subprocess as sp
import shutil
import sys
import string
import time
import pandas as pd
import os


def open_csv(file):
    """Function to open a csv file with the name passed into the function"""
    return pd.read_csv(file)

def save_csv(data):
    """Function to dump the xfoil results into a csv"""
    data.to_csv('sample16-2.dat', index=False)


def call_xfoil():
    """
    Call xfoil using the bash script in 'runx.sh' to evaluate each foil
    """
    # Call xfoil using bash script
    try:
        sp.call(['./runx.sh'], timeout = 5)
    except sp.TimeoutExpired:    # If it takes more than 5 seconds, quit and return 0
        return 0,100
    # Open results.txt for file dump
    file = open('results.txt',"r")
    # read the results.txt file
    data = file.read()
    file.close()

    # Split the results from xfoil
    data = data.split('-----')

    data = data[-1]
    data = data.split('  ')





    


    # Try to run the xfoil simulation multiple times if it does not work for a given foil
    # for i in range (10):  # Number of time to try the solver before giving up

    #     try:
    #         return data[2], data[3]  # 4 for non visc 3 for visc
    #     except (IndexError, TypeError):
    #         pass



    try:
        cl = sum([float(data[2]) , float(data[10]) , float(data[18]) ,float(data[26])])
        cd = sum([float(data[3]) , float(data[11]) , float(data[19]) ,float(data[27])])
        return cl,cd  # 4 for non visc 3 for visc
    except (IndexError, TypeError):  # If file is unreadable then simulation has failed so return 0
        return 0,100



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
