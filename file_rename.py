"""
rename files from a folder
get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""

import os


def rename_files():
    '''
    rename files in a folder
    :return: nothing
    '''
    pass


def main():
    """
    test function
    :return: nothing
    """

    rename_files()
    file = r"C:\Users\kaceyabbott\Desktop\KJA\Day 2\prankOrig"
    path = os.getcwd()


    info = os.listdir(file)
    os.chdir(file)

    for item in info:
        new_info = item.lstrip('0123456789')

        os.rename(item, new_info)
        print(new_info)
    os.chdir(path)

if __name__ == '__main__':
    main()
    exit(0)
