#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

#local variable with the text
text = "X-DSPAM-Confidence:    0.8475";

#get the length of the string
len = len(text)

#get the position of required number
num = text.find('0.8475')

#extract the number and convert to float and print
found = float(text[num:len])
print found
