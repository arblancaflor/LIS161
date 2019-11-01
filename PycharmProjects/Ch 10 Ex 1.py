# Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email)
# tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

count = dict()
maxval = 0
maxkey = ""
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

tmp = count.items()
tmp = sorted(tmp, reverse=True)

for key in count:
    if count[key] > maxval:
        maxval = count[key]
        maxkey = key
print(maxkey,maxval)

