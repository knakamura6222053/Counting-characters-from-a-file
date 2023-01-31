#!/usr/bin/env/python3

# refGene.txtを読み込む
with open("refGene.txt", "r")as file:
    
# gene_nameとcountをする際の枠を作る。(dict型)
    d_gene_name = {}

# 1列ごとにデータを繰り返し読み込む
    for line in file:
        
# 列ごとの空白除去してタブ区切りにしてカラムに入れる
        columns = line.strip().split("\t")

# refGene.txtのgenomeをカラムに入れていく 
        gene_name = columns[1]
       # accession番号がNMから始まるもの
        if not gene_name.startswith("NM"):
            continue

# d_gene_counts内にgene_nameがすでに入っている場合(複数)
        if gene_name in d_gene_counts:
            d_gene_counts[gene_name] += 1


        else:
            d_gene_counts[gene_name] = 1


#出力する
    for gene_name,count in d_gene_counts.items():
        print(gene_name,count)
        
             
