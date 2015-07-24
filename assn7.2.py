#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
#initialize the variable to store the floating point values
num = 0
#initialize the variable to store the number of lines of the required form
line_count = 0
fh = open(fname)

#read through the file to get the line of the required format, extract the floating point number
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line_count=line_count+1
    start = line.find(':')
    num = num + float(line[start+2:len(line)])
	
#pint the average of the floating point number	
print "Average spam confidence:", num/line_count
