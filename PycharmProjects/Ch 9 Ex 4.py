# This program records the domain name (instead of the address) where the message was sent from instead of
# who the mail came from (i.e., the whole email address). At the end of the program,
# print out the contents of your dictionary.

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
        email = email.split("@")
        domain = email[1]
        count[domain] = count.get(domain, 0) + 1
print(count)


