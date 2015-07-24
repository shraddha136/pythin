#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

#Get the name of the file that the user enters
name = raw_input("Enter file:")
#if the user does not enter any filename
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#initialize and declare local variables

#list to store and sort the hour and its respective count
list = list()
#dictionary to compute the count of each hour
counts = dict()
#string to store the color ":"
colon = ":"

#get the line that starts with "From", get the hours' value and compute the times it occurs in the file
for line in handle:
	line = line.rstrip()
	if not line.startswith("From "): continue
	else:
		pos = line.find(colon)
		hour = line[pos-2:pos]
		counts[hour] = counts.get(hour,0)+1
        
#build a list with the hour as key and its count as value from the dictionary computed above		
for key,val in counts.items():
    time = (key,val)
    list.append(time)

#sort the list by key (here, hour)
list.sort()

#print the hour and count values from the list
for hr, count in list:
    print hr, count
        	
