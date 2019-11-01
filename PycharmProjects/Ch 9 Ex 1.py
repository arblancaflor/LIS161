# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with "From", then look for the third word and keep a running count of each
# of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

count = dict()

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("File name cannot be opened:", fname)
    quit()

for line in fhand:
    if line.startswith("From "):
        line = line.split()
        date = line[2]
        count[date] = count.get(date,0) + 1
print(count)