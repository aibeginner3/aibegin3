import jaconv

testword = 'aiueoAIUEOａｉｕｅｏＡＩＵＥＯあいうえおアイウエオｱｲｳｴｵ１２３４５12345'

print(testword)
print('====================================')

print('\n### z2h, digit=True, ascii=True #「ひらがな」以外半角')
print(jaconv.z2h(testword, digit=True, ascii=True))  #=> もんすたｰえなじｰ2
print('\n### h2z, digit=True, ascii=True #「ひらがな」以外全角')
print(jaconv.h2z(testword, digit=True, ascii=True))  #=> もんすたーえなじー２

print('\n### hira2kata #「ひらがな」だけを「カタカナ」に')
print(jaconv.hira2kata(testword))  #=> モンスターエナジー2

print('\n### z2h, digit=True, ascii=True #「カタカナ」以外の半角')
print(jaconv.z2h(testword, digit=True, ascii=True))  #=> ﾓﾝｽﾀｰｴﾅｼﾞｰ2
print('\n### h2z, digit=True, ascii=True #「カタカナ」以外の全角')
print(jaconv.h2z(testword, digit=True, ascii=True))  #=> モンスターエナジー２

print('\n### lower #全て小文字')
print(testword.lower())  #=> monster energy２
print('\n### upper #全て大文字')
print(testword.upper())  #=> MONSTER ENERGY２
print('\n### capitalize #１文字目大文字')
print(testword.capitalize())  #=> Monster energy２
print('\n### title #単語頭大文字')
print(testword.title())  #=> Monster Energy２

print('\n### z2h, digit=True, ascii=True #全て小文字')
print(jaconv.z2h(testword, digit=True, ascii=True))  #=> monster energy2
print('\n### z2h upper, digit=True, ascii=True #全て大文字')
print(jaconv.z2h(testword.upper(), digit=True, ascii=True))  #=> MONSTER ENERGY2
print('\n### z2h capitalize, digit=True, ascii=True #１文字目大文字')
print(jaconv.z2h(testword.capitalize(), digit=True, ascii=True))  #=> Monster energy2
print('\n### z2h title, digit=True, ascii=True #単語頭大文字')
print(jaconv.z2h(testword.title(), digit=True, ascii=True))  #=> Monster Energy2

print('\n### h2z, digit=True, ascii=True #全て小文字')
print(jaconv.h2z(testword, digit=True, ascii=True))  #=> ｍｏｎｓｔｅｒ　ｅｎｅｒｇｙ２
print('\n### h2z upper, digit=True, ascii=True #全て大文字')
print(jaconv.h2z(testword.upper(), digit=True, ascii=True))  #=> ＭＯＮＳＴＥＲ　ＥＮＥＲＧＹ２
print('\n### h2z capitalize, digit=True, ascii=True #１文字目大文字')
print(jaconv.h2z(testword.capitalize(), digit=True, ascii=True))  #=> Ｍｏｎｓｔｅｒ　ｅｎｅｒｇｙ２
print('\n### h2z title, digit=True, ascii=True #単語頭大文字')
print(jaconv.h2z(testword.title(), digit=True, ascii=True))  #=> Ｍｏｎｓｔｅｒ　Ｅｎｅｒｇｙ２


# ひらがな to カタカナ
jaconv.hira2kata(u'ともえまみ')
# => u'トモエマミ'

# ひらがな to 半角カタカナ
jaconv.hira2hkata(u'ともえまみ')
# => u'ﾄﾓｴﾏﾐ'

# カタカナ to ひらがな
jaconv.kata2hira(u'巴マミ')
# => u'巴まみ'

# 半角文字 to 全角文字
jaconv.h2z(u'ﾃｨﾛ･ﾌｨﾅｰﾚ')
# => u'ティロ･フィナーレ'

# ASCII以外の半角文字 to 全角文字
jaconv.h2z(u'abc', ascii=True)
# => u'ａｂｃ'

# 数字以外の半角文字 to 全角文字
jaconv.h2z(u'123', digit=True)
# => u'１２３'

# カタカナ以外の半角文字 to 全角文字
jaconv.h2z(u'ｱabc123', kana=False, digit=True, ascii=True)
# => u'ｱａｂｃ１２３'

# 全角文字 to 半角文字
jaconv.z2h(u'ティロ・フィナーレ')
# => u'ﾃｨﾛ・ﾌｨﾅｰﾚ'

# ASCII以外の全角文字 to 半角文字
jaconv.z2h(u'ａｂｃ', ascii=True)
# => u'abc'

# 数字以外の全角文字 to 半角文字
jaconv.z2h(u'１２３', digit=True)
# => u'123'

# カタカナ以外の全角文字 to 半角文字
jaconv.z2h(u'アａｂｃ１２３', kana=False, digit=True, ascii=True)
# => u'アabc123'

# normalize
jaconv.normalize(u'ティロ･フィナ?レ', 'NFKC')
# => u'ティロ・フィナーレ'

# ひらがな to アルファベット
jaconv.kana2alphabet(u'じゃぱん')
# => japan

# アルファベット to ひらがな
jaconv.alphabet2kana(u'japan')
# => じゃぱん

exit()

hira = "もんすたーえなじー2"
romaji = "mondter energy２"

#【変数格納】「ひらがな」 ⇒ 「カタカナ」
kata = jaconv.hira2hkata(hira)

#「ひらがな」以外半角
print(jaconv.z2h(hira,digit=True, ascii=True))  #=> もんすたｰえなじｰ2
#「ひらがな」以外全角
print(jaconv.h2z(hira,digit=True, ascii=True))  #=> もんすたーえなじー２

#「ひらがな」だけを「カタカナ」に
print(jaconv.hira2kata(hira))  #=> モンスターエナジー2
#「カタカナ」以外の半角
print(jaconv.z2h(kata,digit=True, ascii=True))  #=> ﾓﾝｽﾀｰｴﾅｼﾞｰ2
#「カタカナ」以外の全角
print(jaconv.h2z(kata,digit=True, ascii=True))  #=> モンスターエナジー２

#全て小文字
print(romaji.lower())  #=> monster energy２
#全て大文字
print(romaji.upper())  #=> MONSTER ENERGY２
#１文字目大文字
print(romaji.capitalize())  #=> Monster energy２
#単語頭大文字
print(romaji.title())  #=> Monster Energy２

#全て小文字
print(jaconv.z2h(romaji,digit=True,ascii=True))  #=> monster energy2
#全て大文字
print(jaconv.z2h(romaji.upper(),digit=True,ascii=True))  #=> MONSTER ENERGY2
#１文字目大文字
print(jaconv.z2h(romaji.capitalize(),digit=True,ascii=True))  #=> Monster energy2
#単語頭大文字
print(jaconv.z2h(romaji.title(),digit=True,ascii=True))  #=> Monster Energy2

#全て小文字
print(jaconv.h2z(romaji,digit=True,ascii=True))  #=> ｍｏｎｓｔｅｒ　ｅｎｅｒｇｙ２
#全て大文字
print(jaconv.h2z(romaji.upper(),digit=True,ascii=True))  #=> ＭＯＮＳＴＥＲ　ＥＮＥＲＧＹ２
#１文字目大文字
print(jaconv.h2z(romaji.capitalize(),digit=True,ascii=True))  #=> Ｍｏｎｓｔｅｒ　ｅｎｅｒｇｙ２
#単語頭大文字
print(jaconv.h2z(romaji.title(),digit=True,ascii=True))  #=> Ｍｏｎｓｔｅｒ　Ｅｎｅｒｇｙ２

