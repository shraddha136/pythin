#4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
#Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use raw_input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.


#method to compute the gross pay
def computepay(h,r):
    
    if h > 40:
		gross_pay = ( ( 40 * r ) + ( (h - 40) * 1.5 * r) )    
    else:
        gross_pay = h * r
        
    return gross_pay

#get the values of hours and rate from the user	
hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate per hour:")
try:
	h = float(hrs)
except:
    h = -1
    
try:
	r = float(rate)
except:
    r = -1

#print the appropriate error messages of the pay accordingly
if h == -1.0 or r == -1.0:
   print "Incorrect value for hours or rate"
elif h > 0 and r > 0:
	print computepay(h,r)

#print p
