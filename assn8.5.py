# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt


#Get the name of the file that the user enters
fname = raw_input("Enter file name: ")
#if the user does not enter any filename
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

#initialize and declare local variables
#initialize the count to 0
count = 0

#create list to store the IDs from the file for the lines starting with 'From'
list = list()

#read through the file and store the IDs in the list and compute their count
for line in fh:
	line = line.rstrip()
	if not line.startswith("From "): continue
	else:
		count = count + 1
		words = line.split()
        print words[1]
        	
		
#print the total number of lines with the address of the person who sent the message        
print "There were", count, "lines in the file with From as the first word"
