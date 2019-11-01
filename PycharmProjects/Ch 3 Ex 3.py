# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range or not numeric, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

import sys
x= input("Enter score: ")
try:
    x= float(x)
except ValueError:
    print("Error")
    sys.exit()

if x == 1.0:
    print("A")
elif 1.0 > x >= 0.9:
    print("A")
elif 0.9 > x >= 0.8:
    print("B")
elif 0.8 > x >= 0.7:
    print("C")
elif 0.7 > x >= 0.6:
    print("D")
elif x < 0.6:
    print("F")
else:
    print("Error")
