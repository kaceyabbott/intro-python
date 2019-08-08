"""
use flight class
"""

from airtravel import flight


def main():
    """
    test function
    :return: 
    """
    f = flight('SN066')
    print(f,type(f))
    f2 = flight('SN013')
    print(f2.number())
    print(f2.number(),f2.airline())
    # could use: flight.number(f)


if __name__ == '__main__':
    main()
    exit(0)