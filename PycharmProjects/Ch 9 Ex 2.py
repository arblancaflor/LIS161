# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages
# have come from each email address, and print the dictionary.

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
        email = line[1]
        count[email] = count.get(email,0) + 1
print(count)