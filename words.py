"""
getting file from web and counting words
http://icarus.cs.weber.edu./~hvalle/hafb/words.txt
task 1: count number of words in document
"""

from urllib.request import urlopen

file = "http://icarus.cs.weber.edu./~hvalle/hafb/words.txt"
count = 0
with urlopen(file) as story:
    for line in story:

        words = line.decode("utf-8").split() # split with space as seperator
        #print(words)
        for item in words:
            count += 1


print("Total number of words", count)
