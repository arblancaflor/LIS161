# Write another program that prompts for a list of numbers as the previous exercise
# and at the end prints out both the maximum and minimum of the numbers instead of the average.

sum = 0
count = 0

while True:
    x = input("Enter number: ")
    try:
        x = float(x)
    except ValueError:
        if x == "done":
            if count != 0:
                print(sum, count, max, min)
            break
        else:
            print("Invalid input")
            continue

    if count == 0:
        max = x
        min = x

    if max < x:
        max = x
    if min > x:
        min = x

    count = count + 1
    sum = sum + x

