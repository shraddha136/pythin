#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

#initialize the largest and smallest numbers to none
largest = None
smallest = None

#read the input by the user and compute the largest and smallest number simultaneously
while True:
    num = raw_input("Enter the number :")
    try:
        n = float(num)
    except:
        n = -1
    if num == "done" : 
		break
    if n == -1:
        print "Invalid input"
        
    else:
        if smallest == None :
           
            smallest = n
            largest = n
        else:
            if n < smallest:
                
                smallest = n
            if n > largest:
                
                largest = n
    
#print the largest and smallest numbers
print "Maximum is", int(largest)
print "Minimum is", int(smallest)
