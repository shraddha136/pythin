# 2.3 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
#Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
#You should use raw_input to read a string and float() to convert the string to a number. 
#Do not worry about error checking or bad user data.

#read the hours and rate from the user
hrs = raw_input("Enter Hours:")
rateprhr = raw_input("Enter Rate per hour:")

#convert to float and compute the gross pay and print
gross_pay = float(hrs) * float(rateprhr)
print gross_pay
