"""
working with python functions and return handles
"""

def egg(var):
    """
    returns variable back ot the user
    :param var:
    :return: input object
    """
    return var

def sum_two(num1, num2=8):
    """
    sum two integer objects
    :param num1: object 1
    :param num2: object 2 optional
    :return: sum of objects
    """
    total = num1 + num2
    print(num1, "+", num2, "= ", total)
    return num1+num2


def main():
    """
    test function
    :return:
    """
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)
    n1 = 3
    n2 = 9
    sum_two(n1,n2)
    sum_two(n1)


if __name__ == '__main__':
    main()
    exit(0)