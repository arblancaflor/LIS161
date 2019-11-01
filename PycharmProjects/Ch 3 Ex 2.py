# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.

import sys

x= input("Enter Hours: ")
y= input("Enter Rate: ")

try:
    x=float(x)
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

try:
    y=float(y)
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

if x > 40:
    print("Pay: ", (40*y)+(x-40)*1.5*y)
else:
    print("Pay: ", x*y)
