import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 入力ファイル
infile = "boston_data.xlsx"

# 出力グラフフォルダ
figdir = 'plot'

# データ読み込み
df = pd.read_excel(infile, header=0, index_col=0)

# ビニングデータ
df['部屋数(離散値)'] = pd.cut(df['部屋数'].values, bins=[3,4,5,6,7], labels=['3～4','4～5','5～6','6～7']).add_categories('Out_of_Range')
df = df.fillna({'部屋数(離散値)': 'Out_of_Range'})
#df['部屋数(離散値)'].cat.add_categories(['Out of Range']).fillna({'部屋数(離散値)': 'Out of Range'})
#print(df.head())		# 先頭5行表示
#print(df['部屋数(離散値)'].cat.categories)

# 行列名読み出し
columns = df.columns.tolist()	# 列
index   = df.index.tolist()		# 行
#print(columns, index)
#print(df.head())		# 先頭5行表示

# 欠損値確認
#df.info()
#print(df['部屋数(離散値)'])

#exit()

# 関数 #########################################################################
### 数値データ　ヒストグラム　軸幅指定なし
def histplot0(DF, feature_name, figname):
	sns.distplot(DF[feature_name], rug=False, kde=False)
	plt.ylabel('count')
	plt.grid()
	plt.savefig(figname)
	plt.close()

### 数値データ　ヒストグラム　軸幅指定あり
def histplot(DF, feature_name, nbin, xmin, xmax, ymin, ymax, figname):
	sns.distplot(DF[tuple(feature_name)], rug=False, kde=False, bins=nbin,
				hist_kws={'color': 'k', 'range': [xmin, xmax]})
	plt.xlim(xmin, xmax)
	plt.ylim(ymin, ymax)
	plt.ylabel('count')
	plt.grid()
	plt.savefig(figname)
	plt.close()

### 離散データ　ヒストグラム　軸幅指定なし
def histcountplot0(DF, feature_name, figname):
	sns.catplot(data=DF, x=feature_name, kind='count')
	plt.grid()
	plt.savefig(figname)
	plt.close()

### 数値データ　散布図プロット
def scatterplot0(DF, xfeat, yfeat, figname):
	sns.scatterplot(data=DF, x=xfeat, y=yfeat)
	plt.grid()
	plt.savefig(figname)
	plt.close()

### 離散データ　散布図プロット
def stripplot0(DF, xfeat, yfeat, figname):
	sns.stripplot(data=DF, x=xfeat, y=yfeat)
	plt.grid()
	plt.savefig(figname)
	plt.close()

################################################################################

# 数値データ、カテゴリデータ判別
columns_num, columns_obj = [], []
for feature_name in columns:
	if df.dtypes[feature_name]=='int64' or df.dtypes[feature_name]=='float64':
		columns_num.append(feature_name)
	else:
		columns_obj.append(feature_name)

# pairplot
if(1):
	sns.pairplot(df)
	figname = figdir + '/pairplot.png'
	plt.savefig(figname)
	plt.close()

# ヒストグラム
if(1):
	for feature_name in columns_num:
		histplot0(df, feature_name, figdir + '/hist_' + feature_name + '.png')
		print('hist ', feature_name)

	for feature_name in columns_obj:
		histcountplot0(df, feature_name, figdir + '/hist_' + feature_name + '.png')
		print('hist ', feature_name)

if(0):
	feature_name='犯罪'
	histplot(feature_name, 100, 0, 100, 0, 400, figdir + '/hist_' + feature_name + '.png')

# 散布図
if(1):
	for i in range(len(columns_num)-1):
		for j in range(i+1,len(columns_num)):
			figname = figdir + '/scatter_' + columns_num[i] + '_' + columns_num[j] + '.png'
			scatterplot0(df, columns_num[i], columns_num[j], figname)
			print(figname)

# カテゴリ別の散布図
if(1):
	for xFeature in columns_obj:
		for yFeature in columns_num:
			figname = figdir + '/strip_' + xFeature + '_' + yFeature + '.png'
			stripplot0(df, xFeature, yFeature, figname)
			print(figname)


exit()


### 相関分析

# corrメソッドで相関係数を算出できる
df.corr()['価格']


# まずは線形回帰をつかうことを指定
clf = linear_model.LinearRegression()

# 説明変数をDataFrameとして設定し、arrayに変換
X = df[['部屋数', '低給職業']].as_matrix()

# 目的変数をDataFrameとして設定し、arrayに変換
Y = df['価格'].as_matrix()

# fitメソッドで第1引数に説明変数arrayを第2引数に目的変数を指定する。
clf.fit(X, Y)

# 各説明変数の係数
clf.coef_

# 切片
clf.intercept_

# 決定係数（相関係数の2乗）
clf.score(X, Y)



exit()





import sklearn.datasets as datasets

### データロード
datasets = datasets.load_boston()
# dataメソッドでデータ部分を取り出せる
df = pd.DataFrame(datasets.data)
#print(df.head())

# feature_namesメソッドでカラム名の部分を取り出せる
df.columns = datasets.feature_names
#print(df.head())

feature_names_japanese = ['犯罪', '住宅密度', '商業割合', '川周辺', '窒素酸化物', '部屋数', '古物件', '雇用施設距離', '高速アクセス', '不動産税率', '教師率', '黒人率', '低給職業']
# df.columnsにリストを代入することでカラム名を変更できる
df.columns = feature_names_japanese
#print(df.head())

# targetメソッドで住宅価格のリストが取り出せます
# df['新カラム名']にリストを代入することで、新カラム名の列ができます
df['価格']  = datasets.target
print(df.head())

#df.to_excel('boston_data.xlsx')

