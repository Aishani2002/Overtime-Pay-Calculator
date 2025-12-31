#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value.


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

def computepay(h, r):
    if(h<=40):
        total_pay = h * r

    else:
        total_pay = (40 * r) + ((h-40)*(1.5 * r))   

    return (total_pay)

p = computepay(h, r)
print("Pay", p)