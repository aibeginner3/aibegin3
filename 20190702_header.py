# -*- coding: utf-8 -*-

infile = 'data1.csv'
f = open(infile, 'r')
lines = f.read().split('\n')
f.close()

outfilename = 'out_' + infile
fout = open(outfilename, "w")

infile = 'data1_header.csv'
fhead = open(infile, 'r')
header = fhead.read().split('\n')[0]
fhead.close()

for i in range(len(lines)):

	if i==0:
		print(header, file=fout)
	else:
		print(lines[i], file=fout)

fout.close()


