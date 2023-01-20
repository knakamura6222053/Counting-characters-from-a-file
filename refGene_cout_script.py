#!/usr/bin/env/python3

#　ファイルやディレクトリの操作のosモジュールのインポート
#　対応する文字列のインポート
#　csvモジュールのインポート
#　operatorモジュールのインポート
#  コマンドライン引数のインポート

import os
import re
import csv
import operator
import sys

count= {}
args = sys.argv

print(args[0])
print(args[1])


# refGene.txtから取り出したい要素の変数を設定

file = 'refGene.txt'
pattern = args[1]


with open('refGene.txt', mode = 'r')as f:
    data = f.readlines()

#GREP_TARGETでpatternにマッチしたものをまとめる。

GREP_TARGET = [line for line in data if pattern in line]

#マッチしたものを新しいtxtに記述する。

with open('args[1].txt', mode = 'w')as f:
    f.writelines(GREP_TARGET)

#txtを読み込み、csv形式に直す。

with open('args[1].txt', mode = 'r')as f:
    csvdata = csv.reader(f,delimiter='\t')
    result = sorted(csvdata,key=operator.itemgetter(1))

# 該当の列(AccessionとGene)のものを抽出

    for row in result:
        Accession = row[1]

#　該当のものがあればカウントしていく。

        count.setdefault(Accession, 0)
        count[Accession] +=1
for key, value in count.items():
    print('{}: {}'.format(key, value)) 





