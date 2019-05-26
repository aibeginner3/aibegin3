# -*- coding: utf-8 -*-

import os

# MeCab解析用の自作モジュール読み込み
import mecab_func as myf

#品詞情報を用いて，特定の品詞について頻度表を作成
dirname1 = './testdata_dir'
dirname2 = './testoutdata_dir'

words = ['名詞', '動詞', '形容詞']

files = os.listdir(dirname1)

for word in words:

	log_data = dirname2 + '/plot_' + word + '_data.txt'
	log_plot = dirname2 + '/plot_' + word + '.png'

	print(word)
	for file in files:

		infilename   = dirname1 + '/' + file
		outfilename  = dirname2 + '/out_' + file

		myf.morph_analysis(infilename, outfilename)

	mlines=[]
	for file in files:

		outfilename  = dirname2 + '/out_' + file
		out2filename = dirname2 + '/out_' + word + '_' + file

		mlines_tmp = myf.get_m_lines(outfilename)
		myf.word_freq(mlines_tmp, word, out2filename)
		mlines.extend(mlines_tmp)

	countedwords = myf.word_freq(mlines, word, log_data)
	myf.plot(countedwords, word, log_plot)

