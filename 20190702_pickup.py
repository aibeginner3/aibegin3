# -*- coding: utf-8 -*-

infile = 'wordlist2.csv'
f = open(infile, 'r')
lines = f.read().split('\n')
f.close()

outfilename = 'out_' + infile
fout = open(outfilename, "w")

for i in range(len(lines)):

	line = lines[i]
	if 'Asap' in line:
		before = lines[i-1]
		for word in before.split(','):
			print(word, file=fout)
		for word in line.split(','):
			print(word.split(':')[1].split('}')[0], file=fout)

fout.close()


