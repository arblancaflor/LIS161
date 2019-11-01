# Write a function called count() that accepts a string (word) and a character (char)
# and outputs the number of occurrences of char in word


def count(word, char):
    num = 0
    for letter in word:
        if letter == char:
           num = num + 1
    print("No. of occurrences of", char, "in word:", num)
    return


x = input("Enter a word: ")
y = input("Enter a letter: ")

count(x, y)
