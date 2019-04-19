load sample16-2.dat

pane
oper
iter 1000
visc 7.5e5
pacc
./sample16-2.dat.analysis

alfa 5
pacc

quit
