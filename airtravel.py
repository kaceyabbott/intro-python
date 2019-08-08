"""
a flight class. model for aircraft flights
"""

class flight:
    """
    a flight with a particular passenger aircraft
    """
    def __init__(self,number, aircraft):
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
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating()
        self._seating = [None] + \
                    [{letter: None for letter in seats} for _ in rows]


    def number(self):

        return self._number

    def airline(self):

        return self._number[:2]






class aircraft:
    def __init__(self, registration, model, number_of_rows, num_of_seats):
        self._registration = registration
        self._model = model
        self._number_of_rows = number_of_rows
        self._num_of_seats = num_of_seats

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def number_of_rows(self):
        return self._number_of_rows

    def num_of_seats(self):
        return self._num_of_seats

    def seating(self):
        return (range(1, self._number_of_rows + 1),
                'ABCDEFGHJK'[:self._num_of_seats])










def main():
    """
    test function
    :return: 
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)