# -*- coding: utf-8 -*-

import datetime

infile = 'data2.csv'
f = open(infile, 'r')
lines = f.read().split('\n')
f.close()

outfilename = 'out_' + infile
fout = open(outfilename, "w")

last = lines[len(lines)-1]
if last=='':
	last = lines[len(lines)-2]
	if last=='':
		last = lines[len(lines)-3]
		if last=='':
			last = lines[len(lines)-4]
			if last=='':
				last = lines[len(lines)-5]
print(last)

stamp = last.split('_')[1]
year  = int(stamp[0:4])
month = int(stamp[4:6])
day   = int(stamp[6:8])
hour  = int(stamp[8:10])
min   = int(stamp[10:12])
sec   = int(stamp[12:14])
t_end = datetime.datetime(year,month,day,hour,min,sec)
print(t_end)
sec_end = float(last.split(',')[1])
print(sec_end)

for i in range(len(lines)):
	if i!=0 and lines[i]!='':
		sec  = float(lines[i].split(',')[1])
		dsec = datetime.timedelta(seconds=sec_end - sec)
		tval = t_end - dsec
		print(lines[i],',',tval, sep='')
		
		

fout.close()


