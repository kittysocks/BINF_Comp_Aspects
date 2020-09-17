import os
#Importing modules, modules contain functions that aren't default in Python
import sys
# OS Module - open files, see what's in a folder(directory)













file_dir = "../hw_files/"
#file_dir stands for file directory, the directory that contains the file of interest
fasta = os.listdir(file_dir)
infile = open(file_dir+fasta[1],"r")
#print(infile)
#infile_lines = infile.readlines()
#print(infile_lines)
counter = 0
n_counter = 0
test = 0

for line in infile:

    if line.startswith(">"):
        counter +=1
        s_line = line.split()
        genome = s_line[0]
        
        for letters in genome:
            n_genome = letters.find("N")
            #print(test)
            if n_genome == -1:
                pass
            else:
                n_counter += 1
                print(genome) 
                
    
                  
    
print("There are " + str(counter) + " sequences")
print("There are " + str(n_counter) + " sequences that contain the letter N") 

#
#for line in infile_lines:
#    if line.startswith(">"):  
#          
#        print(counter)