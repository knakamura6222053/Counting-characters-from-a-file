#!/usr/bin/env/python3

# Open the refGene.txt file 
with open("refGene.txt", "r") as file:
    
    # Create a dictionary to store the gene name and count
    gene_counts = {}
    
    # Iterate through each line in the file
    for line in file:
        
        # Split the line by tab character
        columns = line.strip().split("\t")
        
        # Get the gene name from the second column
        gene_name = columns[1]
        
        # Check if the gene name is already in the dictionary
        if gene_name in gene_counts:
            # If it is, increment the count
            gene_counts[gene_name] += 1
        else:
            
            # If it's not, add it to the dictionary with a count of 1
            gene_counts[gene_name] = 1
# sort result
sorted_gene_counts =sorted(gene_counts.items(), key = lambda x: x[1], reverse=True)

# output 
with open("Accession_count.txt","w")as output:
    for gene_name, count in sorted_gene_counts:
        output.write(f"Gene:{gene_name} \nCount:{count}\n")
    
    
## Print out the gene name and count for each gene
#for gene_name, count in gene_counts.items():
#   print(gene_name, count)

