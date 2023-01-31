#!/usr/bin/env/python3

# refGene.txtを読み込む
with open("refGene.txt", "r")as file:
    
# gene_nameとcountをする際の枠を作る。(dict型)
    d_gene_counts = {}

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

# 結果のソート
#sorted_d_gene_counts = sorted(d_gene_counts.items(), key = lambda x: x[1], reverse=True)

# 結果出力(NM番号を取り出してsort)
with open("only_NM_count.txt","w")as output:
    for gene_name in sorted(d_gene_counts.keys()):
        count = d_gene_counts[gene_name]
        output.write(f"{gene_name}\t{count}\n")




## 出力する
#for gene_name,count in sorted_d_gene_counts:
#    print(gene_name,count)
        
             
