#!/usr/bin/env/python3

# read refGene.txt file
with open("refGene.txt") as file:
    data = file.readlines()

# create a dictionary to store gene name and its count
gene_count = {}

# loop through each line in the file
for line in data:
    items = line.strip().split("\t")
    accession = items[1]
    gene_name = items[12]
    # check if accession number starts with "NM"
    if accession.startswith("NM"):
        # add gene name to dictionary or increase its count
        if gene_name in gene_count:
            gene_count[gene_name] += 1
        else:
            gene_count[gene_name] = 1

# output
with open("only_NM_count.txt","w")as output:
    for gene_name in sorted(gene_count.keys()):
        count = gene_count[gene_name]
        output.write(f"{gene_name} \t{count}\n")




