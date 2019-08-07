"""
Learn about range() Collection
"""


def main():
    """
    test function
    :return: 
    """
    for i in range(5):
        print(i)


    #set the initial value:
    print("now setting initial value")
    for i in range(5, 10):
        print(i)

    # create list from range

    l = list(range(5, 10))
    print(l, type(l))
    l2 = list(range(5, 10)) + list(range(30,40))
    print(l2, type(l2))
    #step argument
    l3 = list(range(0,20,2))
    print(l3, type(l3))

    s = [0,2,3,4,6]
    for i in range(len(s)):
        print(s[i])

    #better way
    for v in s:
        print(v)

    # enumerate(): returns an iterable series
    t = [6, 12, 788, 654, 123]
    for i, v in enumerate(t):
        print(i, v)


if __name__ == '__main__':
    main()
    exit(0)