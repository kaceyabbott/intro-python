"""
learn about functions/definitions
use the keyword: def <name>(parameters):
"""


def even_or_odd(number):
    """
     This fuction will tell you if the number is even or odd and return a string
     :param number: input number
     :print: 'even': on even numbers
                'odd' on odd number
    """
    if number % 2 == 0 :
        print("even")
    else:
        print("odd")


def main():
    """test function"""
        ## call function
    print(__name__)
    even_or_odd(66)
    even_or_odd(33)

if __name__ == "__main__":
        main()
        exit(0)


