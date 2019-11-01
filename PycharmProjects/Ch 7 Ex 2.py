# Write a program to prompt for a file name, and then read through the file and
# look for lines of the form:
# X-DSPAM-Confidence: 0.8475

fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        num = float(line.split(":")[-1])
        total = total + num
        count = count + 1
print("Average spam confidence:", float(total/count))

