# -*- coding: utf-8 -*-

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import os

np.set_printoptions(precision=2)


dirname1 = './testdata_dir_out'

files = os.listdir(dirname1)

docs=[]
for file in files:
	infile = dirname1 + '/' + file
	f = open(infile, 'r')
	lines = f.read().split('\n')
	f.close()

	word_tmp=''
	for line in lines:
		if line!='' and 'EOS' not in line:
			words = line.split('\t')
			word = words[0]
			#print(words)
			flag = words[1].split(',')[0]
			if flag=='名詞':
				#print(word)
				word_tmp = word_tmp + word + " "
	docs.append(word_tmp)

#print(docs)

#exit()

#docs = np.array([
#        '白 黒 赤',      # 文書１
#        '白 白 黒',      # 文書２
#        '白 黒 黒 黒',   # 文書３
#        '白'            # 文書４
#        ])
print('docs')
print(docs)


#import codecs
## データの用意
#corpus = codecs.open('tfidf-dataset.txt', 'r', 'utf-8').read().splitlines()

#count_vectorizer = CountVectorizer(input='filename', max_df=0.5, min_df=1, max_features=3000)

vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b', lowercase=False, norm=None, smooth_idf=False)
vecs = vectorizer.fit_transform(docs)

#print('vectorizer')
#print(vectorizer)
#print('vecs')
#print(vecs)

# token_pattern=u'(?u)\\b\\w+\\b’ を指定しました。
# これは、文字列長が 1 の単語を処理対象に含めることを意味します。
# この指定をはずすと、長さ一文字の単語がまったくカウントされなくなります。

index = vecs.toarray().argsort(axis=1)[:,::-1]
feature_names = np.array(vectorizer.get_feature_names())
feature_words = feature_names[index]

#print('index')
#print(index)
print('feature_names')
print(feature_names)
#print('feature_words')
#print(feature_words)

#print('vocabulary')
#print(vectorizer.vocabulary_)

print('vecs.toarray')
print(vecs.toarray())
#-----------------------
# [[ 0.4   0.77  0.49]         ← 文書１のベクトル
#  [ 0.85  0.    0.52]         ← 文書２のベクトル
#  [ 0.26  0.    0.96]         ← 文書３のベクトル
#  [ 1.    0.    0.  ]]        ← 文書４のベクトル
#-----------------------

print('idf')
print(vectorizer.idf_)


#for k,v in sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1]):
#    print(k,v)
#-------
# 白 0
# 赤 1
# 黒 2
#-------

print('======================')
print('= count =')
print('======================')

cnt_vectorizer = CountVectorizer(token_pattern='(?u)\\b\\w+\\b', lowercase=False)
X = cnt_vectorizer.fit_transform(docs)
features = cnt_vectorizer.get_feature_names()

print(features)

#print(type(X))
#print(X)
#print(X.shape)
print(X.toarray())

