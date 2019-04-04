#!/bin/bash

for file in ./sample16-2.dat
do
	#we write commands to a text file called xfoil.com, this first line overwrite the file and the subsequent lines append to it
	echo "pane" > xfoil.com
	echo "oper" >> xfoil.com
	echo "visc 1e6" >> xfoil.com
	echo "pacc" >> xfoil.com
	#this is the only real dynamic line which we need
	echo $file'.analysis' >> xfoil.com
	echo "" >> xfoil.com
	echo "alfa 0" >> xfoil.com
	echo "pacc" >> xfoil.com	
	echo "" >> xfoil.com
	echo "quit" >> xfoil.com

	#we then run xfoil with its STDIN hooked up to the text file where we just wrote the commands to
	xfoil $file < xfoil.com

	#finally we delete the dat file as we have created the polar
    cp sample16-2.dat.analysis results.txt
    rm sample16-2.dat.analysis
done
