# -*- coding: utf-8 -*-

# 必要なモジュールを読み込み
import sys

# 解析結果のファイルを読み込む
file = 'point_check11.txt';
f = open(file, 'r')
lines = f.read().split('\n') # 読み込んで，改行で分割
f.close()

# linesの最後2つの要素はEOSと空白なのでカットしておく
# lines.pop(-1)
# lines.pop(-1)

#print(lines)

title_flag=0
flag=0
for i in range(len(lines)):
#	print(i)
	if ':::::' in lines[i]:
		if title_flag==0:
			print(':::::' + lines[i+1])
			title_flag=1
			flag=0
		elif title_flag==1:
			title_flag=0
	if '-----' in lines[i]:
		flag=0
		print(lines[i+1])
		flag=flag+1
	elif flag==1:
		flag=flag+1
	elif flag>1:
		print('|||||' + lines[i])



