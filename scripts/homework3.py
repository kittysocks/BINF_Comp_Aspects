import sys
import os 
from itertools import chain

file_dir = "../hw_files"
fasta_name = file_dir+"/spike_sequence.fasta"
infile = open(fasta_name,mode="r")
outfile_name = "../hw_files/revised_spike_sequence.fasta"

dict1 = {}
temp_key = ''


#print(infile)

for line in infile:

    s_line = line.rstrip()
    
    if s_line.startswith(">"):
        edit1 = s_line.rstrip()
        edit2 = edit1.split()
        wanted_line = edit2[0]
        line_split = wanted_line.split("|")
        spike = line_split[2]
        
        if spike.startswith("SPIKE_"):
            #print(s_line)
            
            space_split = s_line.split(" ")
            protein_id = space_split[0]
            #print(protein_id)

            temp_key = protein_id
            dict1[temp_key] = ''

            #print(dict1)
            
    else:
        dict1[temp_key]=dict1[temp_key]+ s_line     
            
            
dict1 = {value:key for key, value in dict1.items()}
#print(dict1)

outfile = open(outfile_name,mode="w")

for key,value in dict1.items():
    outfile.write(value)
    outfile.write("\n")
    outfile.write(key)
    outfile.write("\n")
#print(dict1.items())
outfile.close()



    