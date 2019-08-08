"""
use flight class
"""

from airtravel import flight, aircraft
from pprint import pprint as pp


def makeflight():
    """
    lkjasdflkj
    :return:
    """


    f1 = flight('SN066', aircraft("g-eup",
                              'airbusA319',
                              number_of_rows=22,
                              num_of_seats=6))

    #pp(f1._seating)

    f1.allocate_seat("3A", 'guido')
   # pp(f1._seating)
    f1.allocate_seat("2A", 'guido')
    return f1


def main():
    """
    test function
    :return: 
    """
    f1 = makeflight()
   # pp(f1._seating)
    #print("available seats", flight.num_availableseats())

    def consolecardprinter(passenger,seat,flight_number,aircraft):
        output = "| name: {0}"\
                "flight: {1}"\
                'seat: {2}'\
                'aircraft: {3}'\
                ' |'.format(passenger, flight_number,seat,aircraft)

        lines = [output]
        card = '\n'.join(lines)
        print(card)
        print()


if __name__ == '__main__':
    main()
    exit(0)