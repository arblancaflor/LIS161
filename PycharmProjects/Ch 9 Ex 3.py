# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using
# a maximum loop to find who has the most messages and print how many messages the person has.

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

for key in count:
    if count[key] > maxval:
        maxval = count[key]
        maxkey = key
print(maxkey,maxval)

