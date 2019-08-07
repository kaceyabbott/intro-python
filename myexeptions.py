"""
Learn about exceptions
"""
import sys
def convert(s):
    """
    converts a string to a integer
    :param s: string
    :return: integer
    :raise valueerror on zerodivisionerror

    """

    try:

        return int(s)
    except (ValueError, TypeError) as e:
        print("conversion error {}".format(str(e)), file=sys.stderr)
        pass
    return -1

def sqrt(x):
    """
    compute square root of number methof of heron alexandria
    :param x: number
    :return: sqrt of x
    """
    guess = x
    i = 0

    try:
        while guess*guess != x and i < 20:
            guess = (guess+x/guess)/2.0
            i =+1
    except ZeroDivisionError:
        raise ValueError()
    return guess

def main():
    """
    test function
    :return: 
    """

    #print(convert("11"))
   # print(convert("hello"))
    #print(convert([1,4,8]))
    try:
        print(sqrt(9))
        print(sqrt(-1))
    except ValueError:
        print("cannont compute the value of - numbers")

    print("done")

if __name__ == '__main__':
    main()
    exit(0)