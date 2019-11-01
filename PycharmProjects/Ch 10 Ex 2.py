# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour
# from the "From" line by finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

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
        time = line[5]
        time = time.split(":")
        hour = time[0]
        count[hour] = count.get(hour, 0) + 1

tmp = count.items()
tmp = sorted(tmp)

for key, value in tmp:
    print(key, value)



