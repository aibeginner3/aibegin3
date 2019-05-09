#! /usr/bin/python
# coding: utf-8

import sys, os

path = './'
files = os.listdir(path)
#print(files)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
#print(files_dir)
#files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
#print(files_file)
#exit()

cnt=0
for directory in files_dir:

	dir_files = os.listdir(path + directory)
	for filename in dir_files:

		#--- read file 
		f = open(path + directory + '/' + filename)
		lines = f.readlines()
		f.close()

		nline = len(lines)
		#print(filename)
		#print(path + directory + '/' + filename)
		print(path + directory + '/' + filename + ' : ' + str(nline))
		cnt = cnt + nline

print('total: ' + str(cnt))
