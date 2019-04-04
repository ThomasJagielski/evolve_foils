import subprocess as sp
import shutil
import sys
import string
import time
import pandas as pd
import os





# output_df = pd.DataFrame({'col1':[1,2], 'col2' : [3,4]})  
# print(output_df)
# output_df.to_csv('output_file_name.dat')
# data = 

# file = open('testdat.dat',"w")
# file.write(data)
# file.close()





def run_xfoil():

    # def issueCmd(cmd,echo=True):
    #     ps.stdin.write(cmd)
    def issueCmd(cmd,echo=True):
        comm = ps.communicate(cmd)




    ps = sp.Popen(['xfoil'],
                stdin=sp.PIPE,
                stdout=None,
                stderr=None)
    
    
    
    
    # if method==1:
    #     res = ps.communicate( string.join(["naca",
    #                                         "0016",
    #                                        ],'\n') )

    # issueCmd('naca \n'.encode())
    # issueCmd('0016 \n'.encode())
    issueCmd('load \n'.encode())
    issueCmd('sample16-2.dat\n'.encode())
    # issueCmd('test\n'.encode())
    # issueCmd('oper \n'.encode())
    issueCmd('oper \n'.encode())
    issueCmd('visc \n'.encode())
    issueCmd('1e6 \n'.encode())
    # issueCmd('alfa 0 \n'.encode())
    issueCmd('pacc \n'.encode())
    issueCmd(' data_save.txt\n'.encode())
    issueCmd('\n'.encode())
    issueCmd('data_save \n'.encode())
    # issueCmd(' aseq 0 1 1\n'.encode())
    issueCmd('alfa 0\n'.encode())
    issueCmd('pacc \n'.encode())
    issueCmd('\n \n'.encode())
    issueCmd('quit \n'.encode())


    file = open('data_save.txt',"r")

    data = file.read()
    file.close()
    data = data.split('-----')

    data = data[-1]
    data = data.split('  ')

    # issueCmd('rm -r data_save.txt\n'.encode())
    

    # print(data[2])
    # print(data[3])
    # ps.kill()
    return data[2], data[3]










# time.sleep(5)
# ps.kill()

# ps.communicate('naca')
# ps.communicate('0016')
# ps.communicate('oper')
# ps.communicate('visc')
# ps.communicate('1e6')
# ps.communicate('alfa 0')
# ps.communicate('pacc')
# ps.communicate('data_save.txt')
# ps.communicate('aseq 0 1 1')
# ps.communicate('pacc'