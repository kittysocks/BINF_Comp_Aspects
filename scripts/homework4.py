import sys
import numpy as np

file_input=open("../hw_files/Yeast_FAA4_string_interactions.tsv",mode='r') #open and read the file

dict1={}
temp_key1=''
temp_key2=''
key_id=0

for line in file_input:
    line=line.rstrip()
    #print(line)
    node_name = line.split("\t")
    #backwards t - splits different columns into words
    #print(node_name[0])
    temp_key1=node_name[0]
    temp_key2=node_name[1]

    if temp_key1 in dict1:
        pass

    else:
        dict1[temp_key1]=key_id
        key_id+=1

    if temp_key2 in dict1:
        pass
    else:
        dict1[temp_key2]=key_id
        key_id+=1

file_input.close()

p_array = np.zeros((len(dict1),len(dict1)))

    
file_input=open("../hw_files/Yeast_FAA4_string_interactions.tsv",mode='r')
line_id=0
for line in file_input:
        line=line.rstrip()
        line_id+=1
        if line_id > -1:
            node_name = line.split("\t")
            p_array[dict1[node_name[0]]][dict1[node_name[1]]]=round(1000.0*float(node_name[12]))
            p_array[dict1[node_name[1]]][dict1[node_name[0]]]=round(1000.0*float(node_name[12]))

            if p_array[dict1[node_name[0]]][dict1[node_name[1]]] > 0:
                print (p_array[dict1[node_name[0]]][dict1[node_name[1]]])

file_input.close()

text_file=open("../hw_files/Yeast_FAA4_string_interactions_matrix", mode='w')
for row in p_array:
    np.savetxt(text_file,row)

#print(p_array)
text_file.close()

print("There are", len(dict1), "proteins")

print(dict1)

