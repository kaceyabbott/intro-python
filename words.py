"""
getting file from web and counting words
http://icarus.cs.weber.edu./~hvalle/hafb/words.txt
task 1: count number of words in document
"""


from urllib.request import urlopen




def fetch_words(file):
    """
    count words in url file
    :param filename: url to file
    fetch the words from a file on the web
    :return: a list with the items
    """

    word_count = []
    count = 0
    with urlopen(file) as story:
        for line in story:

            words = line.decode("utf-8").split() # split with space as seperator
            #print(words)
            for item in words:
                word_count.append(item)

    return word_count

def print_items(items):
    """
    print elements of the list
    :param items: list
    :return: nothing
    """
    for item in items:
        print(item)
    pass


def main():
    """
    Test function for words library
    :return: nothing
    """
    file = "http://icarus.cs.weber.edu./~hvalle/hafb/words.txt"
    words = fetch_words(file)
    print_items(words)

if __name__ == '__main__':
    main()
    exit()

