"""
getting file from web and counting words
http://icarus.cs.weber.edu./~hvalle/hafb/words.txt
task 1: count number of words in document
"""

from urllib.request import urlopen
word_count = {}
file = "http://icarus.cs.weber.edu./~hvalle/hafb/words.txt"
count = 0
with urlopen(file) as story:
    for line in story:

        words = line.decode("utf-8").split() # split with space as seperator
        #print(words)
        for item in words:
            #check if already in dictionary
            if item in word_count:
                word_count[item] += 1
            #if not then add to dictionary
            else:
                word_count[item] = 1
            count += 1


print("Total number of words", count)


#task 2 count number of times each work appears in file

print(word_count)



