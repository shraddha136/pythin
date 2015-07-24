#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85

#read the number from the user
number = raw_input("Enter a number between 0.0 and 1.0")
#convert the number to a float
n = float(number)

#display the grade accordingly
if n >= 0.9 and n <= 1.0:
   print "A"
elif n >= 0.8 and n < 0.9:
   print "B"
elif n >= 0.7 and n < 0.8:
   print "C"
elif n >= 0.6 and n < 0.7:
   print "D"
elif n < 0.6 and n >= 0.0:
   print "F"
elif n < 0.0 or n > 1.0:
    print "Number out of range!"

   

