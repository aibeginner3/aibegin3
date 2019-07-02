# -*- coding: utf-8 -*-

infile = 'wordlist.csv'
f = open(infile, 'r')
lines = f.read().split('\n')
f.close()

outfilename = 'out_' + infile
fout = open(outfilename, "w")

for line in lines:

	if line!='':
		newline = line + ",-1,-1,1,名詞,固有名詞,一般,*,*,*,*,*,*,AW"
		print(newline, file=fout)

fout.close()


