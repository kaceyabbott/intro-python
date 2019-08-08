"""
Learn about generator functions
- describe iterable series with code functions
- are lazy evaluated: the next value in the sequence is computed on demand
- can model infinite series or sequences: data steams, mathematical series with no end
- can use pipelines

use the yield keyword
"""

def gen123():
    yield 1

    yield 2

    yield 3

def gen246():
    print('about to yield 2')
    yield 2
    print('about to yield 4')
    yield 4
    print('about to yield 6')
    yield 6
    print('about to return')




def main():
    """
    test function
    :return: 
    """
    g = gen123()
    print(g,type(g))
    #yield next value
    print(next(g))
    #iterate over the generator
    for v in gen123():
        print(v)

    h = gen246()
    print(next(h))
    print(next(h))
    print(next(h))





if __name__ == '__main__':
    main()
    exit(0)