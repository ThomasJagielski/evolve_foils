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
        sp.call(['./runx.sh'], timeout = 1)
    except sp.TimeoutExpired:    # If it takes more than 1 second, quit
        return 0,100 # Return a foil with a fitness of 0

    # Open results.txt for file dump
    file = open('results.txt',"r")
    # read the results.txt file
    data = file.read()
    file.close()

    # Split the results from xfoil
    data = data.split('-----')

    data = data[-1]  # Select the part where the numbers are stored
    data = data.split('  ')



    try:
        # Attempt to grab the coefficient of lift and drag out of the file that xfoil creates
        cl = sum([float(data[2]) , float(data[10]) , float(data[18]) ,float(data[26])])
        cd = sum([float(data[3]) , float(data[11]) , float(data[19]) ,float(data[27])])
        return cl,cd
    except (IndexError, TypeError, ValueError):  # If file is unreadable or returns a bad string then simulation has failed
        return 0,100 # Return a foil with a fitness of 0



if __name__ == "__main__":
    print(call_xfoil())
