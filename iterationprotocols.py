"""
learn about iterable, iterator objects
Use the built in iter(), next()
"""

def first(iterable):
    """
    return next member of list if available
    :param iterable: object
    :return: next object or
    :except: valueerror or stopiteration
    """
    iterator = iter(iterable)

    try:
            return next(iterator)
    except  StopIteration:
        raise ValueError("iterable is empty")


def main():
    """
    test function
    :return: 
    """
    iterable = ['spring', 'summer','fall','winter']
    iterator = iter(iterable) # give me an interator
    print(type(iterator),iterator)
    print(next(iterator))

    print(first(iterable))


if __name__ == '__main__':
    main()
    exit(0)