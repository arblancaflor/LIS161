# Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fname = input("Enter the file name: ")
fhand = open(fname)
for line in fhand:
    line = line.upper()
    print(line)