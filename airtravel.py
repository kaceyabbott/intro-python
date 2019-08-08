"""
a flight class. model for aircraft flights
"""

class flight:
    """
    a flight with a particular passenger aircraft
    """
    def __init__(self,number):
        """
        initializes flight number
        :param number: flight number
        ":raise: valueerror
        """
        # implementation details begin with '_'
        #validate flight number:
        # 5 chars long, AADDD

        if len(number) != 5:
            raise ValueError('invalid flight number'.format(number))
        if not number[:2].isalpha():
            raise ValueError('invalid flight number'.format(number))
        if not number[:2].isupper():
            raise ValueError('invalid flight number'.format(number))
        if not number[2:].isnumeric():
            raise ValueError('invalid flight number'.format(number))

        self._number = number




    def number(self):

        return self._number

    def airline(self):

        return self._number[:2]



def main():
    """
    test function
    :return: 
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)