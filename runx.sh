#!/bin/bash

# Adapted from https://github.com/asurath/airfoil-analysis/blob/master/datanalysis.sh

for file in ./sample16-2.dat
do
	#we write commands to a text file called xfoil.com, this first line overwrite the file and the subsequent lines append to it

	echo "pane" > xfoil.com
	echo "oper" >> xfoil.com
	
	echo "iter 100" >> xfoil.com
	echo "pacc" >> xfoil.com

	echo $file'.analysis' >> xfoil.com
	echo "" >> xfoil.com
	echo "alfa 2.5" >> xfoil.com
	echo "pacc" >> xfoil.com	
	echo "" >> xfoil.com
	echo "quit" >> xfoil.com

	#we then run xfoil with its STDIN hooked up to the text file where we just wrote the commands to
	xfoil $file < xfoil.com > /dev/null 2>&1

	#copy the results to a results.txt file and then delete the original file
    cp sample16-2.dat.analysis results.txt
    rm sample16-2.dat.analysis
done
