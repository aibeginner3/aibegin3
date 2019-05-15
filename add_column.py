#! /usr/bin/python
# coding: utf-8

import sys, os

filename = 'data1.csv'

#--- read file 
f = open(filename)
lines = f.readlines()
f.close()

fout = open('out.csv', 'w')

for line in lines:

	line = line.strip()
	#--- read path
	path = line.split(',')
	#print(path[1])
	dirs = path[1].split('\\')
	#print(dirs)
	print('{},{},{},{}'.format(line,dirs[3],dirs[4],len(dirs)), file=fout)

fout.close()