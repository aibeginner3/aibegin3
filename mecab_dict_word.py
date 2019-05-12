# -*- coding: utf-8 -*-

# 必要なモジュールを読み込み
import MeCab
import sys
import string
from collections import OrderedDict
import matplotlib.pyplot as plt

# matplotlibの日本語設定
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Sans', 'BIZ UDGothic', 'Yu Gothic', 'Meiryo', 'Noto Sans CJK JP', 'IPAexGothic', 'DejaVu Sans']

# infileの文章を解析して，結果をoutfileに出力
def morph_analysis(infile, outfile):
    t = MeCab.Tagger(' '.join(sys.argv)) # 形態素解析器の変数（オブジェクト）を作成
    fin = open(infile, 'r') # 解析対象のファイルを開く
    fout = open(outfile, 'w') # 解析結果を書き出すファイルを開く
    fout.write(t.parse(fin.read())) # 読み込んで解析して書き出し
    fin.close() # ファイルを閉じる
    fout.close()
###注　読み込んで解析器に渡し結果を受け取りそれを書き出すまで，すべてutf-8の文字列で行っている

# 解析結果のファイルを読み込む
def get_m_lines(file):
    f = open(file, 'r') # 解析結果のファイルを開く
    m_lines = f.read().split('\n') # 読み込んで，改行で分割

    # m_linesの最後2つの要素はEOSと空白なのでカットしておく
    m_lines.pop(-1)
    m_lines.pop(-1)

    f.close()
    return m_lines # 結果（１形態素毎の情報のリスト）を返す

def noun_ha(mlines, outfile):
    hist = dict() # キーに名詞、値に頻度（数字）が入るのを想定
    morphs = []
    tr_hist = dict()
    plot_hist = dict()

    for line in mlines:
        morphs.append(mecab_data(line)) #形態素を１つずつ辞書型に変換

    #print(morphs)

    for i in range(len(morphs) -1): # i+1 が「は」の時を想定しているので、len -1
        #ある形態素の要素が名詞で、その次の要素が係助詞で、かつ係助詞「は」のとき
        #if morphs[i]['pos'] == '名詞' \
        #and morphs[i+1]['pos1'] == '係助詞' \
        #and morphs[i+1]['surface'] == 'は':
        if morphs[i]['pos'] == '名詞':
        #if morphs[i]['pos'] == '名詞' \
        #or morphs[i]['pos'] == '動詞' \
        #or morphs[i]['pos'] == '形容詞':
            key = morphs[i]['surface'] #その名詞をキーとする
            hist[key] = hist.get(key,0) + 1 #もし、まだそのkeyが存在しなかったら(=初めて出現したら),デフォルト値を0と考えて1を足す。

    fout1 = open('out1_' + outfile, 'w')
    print(hist, file=fout1)
    fout1.close()

    for noun in hist: #キーを取り出す
        #histは頻出回数がバリューだが、
        #tr_hist に　頻出回数をキーに変換したものを入れる。バリューを名詞のリストにする
        tr_hist[hist[noun]] = tr_hist.get(hist[noun],[])+[noun]

    fout2 = open('out2_' + outfile, 'w')
    print(tr_hist, file=fout2)
    fout2.close()

    fout3 = open('out3_' + outfile, 'w')
    for i in sorted(tr_hist.keys(), reverse = True):
        #見やすく名詞ごとに出力、頻度高い順に
        if i > 0: #頻出回数が2以上なら
            for m in range(len(tr_hist[i])):
                #同じ出現回数の名詞を分けて表示
                #print(tr_hist[i][m], i)
                print(tr_hist[i][m], i, file=fout3)
                plot_hist[tr_hist[i][m]] = i
    fout3.close()

    #print(plot_hist)
    return plot_hist

# 文字列である解析結果を使いやすい形（辞書型）に変換
def mecab_data(line):
    #print line #の  助詞,連体化,*,*,*,*,の,ノ,ノ
    mkeys = ['pos', 'pos1', 'pos2', 'pos3', 'inf', 'form', 'base', 'yomi', 'oto'] # キィを定義
    morph = OrderedDict() # 辞書型データの初期化
    data = line.split('\t') # 改行コードを外して(?)，タブで（表記とその他の情報に）分割
    #の 助詞,連体化,*,*,*,*,の,ノ,ノ が、「の」と「助詞,連体化,*,*,*,*,の,ノ,ノ」に分割される
    morph['surface'] = data[0] # 表記をしまう
    features = data[1].split(',') # その他の情報はカンマ区切りなので，カンマで分割 [助詞,連体化,*,*,*,*,の,ノ,ノ]
    for i in range(len(features)) : # 分割されたそれぞれの情報を
        morph[mkeys[i]] = features[i] # その順序に従って，適切なキィの値とする

    if morph['base'] == '*' : # 未知語について，扱いやすいように必要な情報を付加
        morph['yomi'] = '*'
        morph['oto'] = '*'

    return morph # 得られた辞書型データを返す

# カウントした単語をグラフで表示させる
def plot(countedwords):
    counts = {}
    total = sum(countedwords.values())
    c = 1
    show = 20 #何件表示する？
    for k, v in sorted(countedwords.items(), key=lambda x: x[1], reverse=True):  # 辞書を降順に入れる
        counts.update( {str(k):int(v)} )
        c += 1
        if c > show:
            break
    plt.figure(figsize=(15, 5)) #これでラベルがかぶらないくらい大きく
    plt.title('頻繁に発言したワードベスト{0} : 総単語数{1} : 単語の種類数{2}'.format(show,total,len(countedwords)), size=16)
    plt.bar(range(len(counts)), list(counts.values()), align='center')
    plt.xticks(range(len(counts)), list(counts.keys()))
    # 棒グラフ内に数値を書く
    for x, y in zip(range(len(counts)), counts.values()):
        plt.text(x, y, y, ha='center', va='bottom') #出現回数
        plt.text(x, y/2, "{0}%".format(round((y/total*100),2)),ha='center',va='bottom')  #パーセンテージ
    plt.tick_params(width=2, length=10) #ラベル大きさ 
    plt.tight_layout()  #整える
    #plt.show()

    pngname = 'plot.png'
    plt.savefig(pngname)


#品詞情報を用いて，特定の品詞について頻度表を作成
infilename  = 'data/TextData2.txt'
outfilename = 'out_test.txt'

morph_analysis(infilename, outfilename)
mlines = get_m_lines(outfilename)
countedwords = noun_ha(mlines, outfilename)
#print(type(countedwords))
#print(countedwords)
plot(countedwords)

