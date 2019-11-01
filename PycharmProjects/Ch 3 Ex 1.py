# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

x= float(input("Enter Hours: "))
y= float(input("Enter Rate: "))

if x > 40:
    print("Pay: ", (40*y)+(x-40)*1.5*y)
else:
    print("Pay: ", x*y)
