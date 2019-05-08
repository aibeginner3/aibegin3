#! /usr/bin/python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import sys, os

files = os.listdir('./')
print(files)

#filename = 'test.csv'
for filename in files:

	print(filename)
	#--- read file 
	f = open(filename)
	lines = f.readlines()
	f.close()

	#--- read header
	#headers = lines[0].strip().split(',')
	#print(headers)
	#nhead = len(headers)

	nline = len(lines)
	print(nline)

#--- read data
#data=[]
#for i in range(1,nline):
  #tmpdata       = lines[i].strip().split(',')
  #tmpdata_float = [float(num) for num in tmpdata]
  #data.append(tmpdata_float)
#array_data = np.array(data)
#ndata = len(data)
#print(ndata)
#print(array_data)
#dt = array_data[3,0]-array_data[2,0]

#x = array_data[:,0]
#y = array_data[:,3]

#nt_dev = 700
#sum_res=999999999999
#for nt_dev in range(5,ndata-5):
#  x1,y1,x2,y2=[],[],[],[]
#  x1, y1 = x[0:nt_dev], y[0:nt_dev]
#  x2, y2 = x[nt_dev:ndata], y[nt_dev:ndata]
#  A1 = np.array([x1,np.ones(len(x1))]).T
#  A2 = np.array([x2,np.ones(len(x2))]).T
#  (par1, res1, rank1, s1) = np.linalg.lstsq(A1,y1,rcond=None)
#  (par2, res2, rank2, s2) = np.linalg.lstsq(A2,y2,rcond=None)
#  sum_res0 = res1[0]+res2[0]
#  #print(par1, res1, rank1, s1)
#  #print(par2, res2, rank2, s2)
#  #print(sum_res0)
#  if(sum_res>sum_res0):
#    zx1,zy1,zx2,zy2,zA1,zA2 = x1,y1,x2,y2,A1,A2
#    zpar1,zpar2 = par1,par2
#    sum_res = sum_res0
#    devide = nt_dev*dt

#print(devide)
#exit()

#--- plot
#plt.plot(x, y, 'r')
#plt.xlabel('Time[s]')
#plt.ylabel('Gear')
#plt.xlim(f1xmin,f1xmax)
#plt.ylim(f1ymin,f1ymax)
#plt.legend()
#plt.grid()
#plt.show()
#param = '_{}-{}_t_{:.3f}'.format(gear1,gear2,t1*dt)
#png = 'figure{}.png'.format(param)
#plt.savefig(png)
#plt.close()

