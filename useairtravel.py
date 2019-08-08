"""
use flight class
"""

from airtravel import flight, aircraft
from pprint import pprint as pp

def main():
    """
    test function
    :return: 
    """
    f1 = flight('SN066', aircraft("g-eup",
                        'airbusA319',
                        number_of_rows=22,
                        num_of_seats=6))



    pp(f1._seating)


if __name__ == '__main__':
    main()
    exit(0)