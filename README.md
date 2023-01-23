## Counting-characters-from-a-file

# Open the refGene.txt file
with open("refGene.txt", "r") as file:
    
    # Create a dictionary to store the gene name and count (dict型で遺伝子名を数える)
    gene_counts = {}
    
    # Iterate through each line in the file (fileにある列のそれぞれの要素の処理)
    for line in file:
        
        # Split the line by tab character 
        # line.strip() : 文字列の一部を削除
        # split("\t")でタブ区切りに変更
        #カラムにデータを入れる
        columns = line.strip().split("\t")
        
        # Get the gene name from the second column (2つ目のカラムから遺伝子名のデータを抽出)
        gene_name = columns[1]
        # Check if the gene name is already in the dictionary
        if gene_name in gene_counts:
            # If it is, increment the count
            gene_counts[gene_name] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            gene_counts[gene_name] = 1
    
    # Print out the gene name and count for each gene (各遺伝子に対して実行し、出力)
    for gene_name, count in gene_counts.items():
        print(gene_name, count)
