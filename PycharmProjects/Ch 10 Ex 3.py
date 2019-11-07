# Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert
# all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation,
# or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency
# varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies

count = dict()
sort_list = list()
fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("File name cannot be opened:", fname)
    quit()

for line in fhand:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                count[letter] = count.get(letter, 0) + 1
            else:
                letter = ""

tmp = count.items()
print(tmp)
for k,v in tmp:
    sort_list.append((v,k))
tmp = sorted(sort_list, reverse=True)
print(tmp)






