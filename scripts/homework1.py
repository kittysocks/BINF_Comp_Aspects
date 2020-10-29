import os
from itertools import chain

file_dir = "../hw_files/"
fasta = os.listdir(file_dir)
infile = open(file_dir+fasta[1],"r")
outfile_name = "../revised_sequences.fasta"

dict1={}
temp_key = ''
temp_number = 0

print(infile)

for line in infile:
    #print(line)
    line = line.rstrip()
#    
    if line.startswith(">"):
        temp_key =line
        dict1[temp_key]= ''
        temp_number +=1
        
    else:
        dict1[temp_key] = dict1[temp_key]+ line 
        #print(temp_key," : ",dict1[temp_key])
        
infile.close()

dict2 = dict1.copy()
small_num = 0
n_num = 0

for item in dict2.keys():
    if (len(dict2[item])<29700):
        small_num+=1
        del(dict1[item])
    elif((len(dict2[item])>29700) and (dict2[item].find("N") > -1)):
        n_num +=1
        del(dict1[item])
       
       
print(small_num)
print(n_num)

dict1 = {value:key for key, value in dict1.items()}

outfile = open(outfile_name,mode="w")
for key,value in dict1.items():
    outfile.write(value + "\n" + key + "\n")
    
outfile.close()

print "The original file had ", temp_number, " genome records."
print "The revised file had ", len(dict1), " unique records."






