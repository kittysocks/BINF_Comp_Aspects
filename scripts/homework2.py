import sys, string
import alignment

file_input=open("../hw_files/sequences.fasta",mode='r') #open and read the file

dict1={} #creates a empty dictonary
temp_key='' #creates a temp key for the dictonary
temp_number=0;
for line in file_input: #for each line by line, read it into variable 'line'. 
	line=line.rstrip() #removes the enter symbol ("\n") of each line
	#print (line+"!") 
	if line.startswith(">"): #selects the lines that starts with >
		temp_key=line #record it as temp key
		dict1[temp_key]='' #makes a dictionary item with key of temp_key, but empty value to be updated later
		temp_number+=1
	else: #If the line doesnt start with >, then this
		dict1[temp_key]=dict1[temp_key]+line #updates the value by adding new readed line
		#print(temp_key," : ",dict1[temp_key]) #prints the (key and value) temp_key, which is the line that starts with >, space, and the lines that doesnt have the >.
file_input.close()


for each1 in dict1.keys():
        #print each1, "\n"
        for each2 in dict1.keys():
                if each1 != each2:
                        print "Now aligning the following two sequences\n"
                        str1_500=dict1[each1][0:500]
                        print each1, "\n", str1_500
                        str2_500=dict1[each2][0:500]
                        print each2, "\n", str2_500, "\n"
                        print "Runing Needleman algorithm for golbal alignment\n"
                        alignment.needle(str1_500, str2_500)
                        print "Runing Waterman algorithm for local alignment\n"
                        alignment.water(str1_500, str2_500)
                        break # ignore the others!  
                else:
                        pass # do once, compare once! 
                
        break # break each1  



