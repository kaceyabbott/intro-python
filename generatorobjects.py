"""
generator objects are a cross between comprehensions and generator functions
syntax: similar to list comprehension:
    (expr(item) for item in iterable)
"""


from listcomprehensions import prime


def main():
    """
    test function
    :return: 
    """
    msq = (x*x for x in range(1,100001))
    print(msq, type(msq))
    #print(sum(msq))
    #print('the sum of the first 1m square numbers is:', sum(msq))
    #print('the sum of the first 1m square numbers is:', sum((x*x for x in range(1,100001))))


    print('the sum of the first 1-10000 prime numbers is:', sum(x for x in range(1,10000)if prime(x)))

if __name__ == '__main__':
    main()
    exit(0)