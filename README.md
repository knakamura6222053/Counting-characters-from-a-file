# Objective
Count the number of accession numbers corresponding to genes and their number from the refGene.txt file

## Install
refGene.txt URL https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz

### Protocol
1) Put download refGene.txt in the directory where you want to run the script
  ※ Please check your file name. If you can't run this script, you may be different file name.
2) Run this script under python environment
  ※ Output file already specified in script
3) Make sure that the "output file" is created in your directory.
4) If the file has not been created or is empty, you check the location of the execution directory and the directory where refGene.txt is located

#### Notes
"refGene_count_script.py" is a script that counts the number of genes for all accession numbers.
"NM_only_count.py" is a script that counts the number of genes of those with accession number NM.

