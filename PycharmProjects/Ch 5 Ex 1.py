# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.
# count = count + 1
# total = x + total

sum = 0
count = 0

while True:
    x = input("Enter number: ")
    try:
        x = float(x)
    except ValueError:
        if x == "done":
            if count != 0:
                print(sum, count, sum / count)
            break
        else:
            print("Invalid input")
            continue

    count = count + 1
    sum = sum + x
