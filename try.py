# -*- coding: utf-8 -*-

# 必要なモジュールを読み込み
import os
import MeCab

m = MeCab.Tagger('mecabrc')  # -Ochasen/-Owakati/-Oyomi/mecabrc

dirname = './testdata_dir'
files = os.listdir(dirname)
#print(files)

for file in files:

	# 解析結果のファイルを読み込む
	print('::: ' + file)
	infile = dirname + "/" + file
	f = open(infile, 'r')
	lines = f.read().split('\n') # 読み込んで，改行で分割
	f.close()

#	outfilename = 'out_' + infile
#	fout = open(outfilename, "w")

	sent = ''
	for i in range(len(lines)):
		sent = sent + lines[i].strip()
		#print(lines[i].strip(),end='')
	print(sent)

	words = m.parse(sent)
	print(words)

	output_words = []

	for row in words.split("\n"):
		word = row.split("\t")[0]
		if word == "EOS":
			break
		else:
			pos = row.split("\t")[1].split(",")[0]
			if pos == "名詞":
				output_words.append(word)

	print(list(set(output_words)))

#	fout.close()


