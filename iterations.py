"""
when working with iterators, generators, etc
look at the documentatoin for the itertools module
"""

from itertools import islice, count, chain
from listcomprehensions import prime

import statistics


def main():
    """
    test function
    :return: 
    """
    thousandprimes = islice((x for x in count() if prime(x)), 1000)
    print(thousandprimes,type(thousandprimes))
    #print('list of first 1000 prime numbers:', list(thousandprimes))
    #if you need to use the object again, you will need to regenerate it
    thousandprimes = islice((x for x in count() if prime(x)), 1000)
    print('list of first 1000 prime numbers:',sum((thousandprimes)))
    #other built ins use with itertools: any(or) or all(and)
    print(any([False, False, True]))
    print(all([False, False, True]))


    print('any primes in range',any(prime(x) for x in range(1328,1363)))

    names = ['London','New York','Ogden']
    print(all(name == name.title() for name in names))

    #another builtin: zip()
    sunday = [2,2,5,7,9,10,9,6,4,4]
    monday = [12,14,14,15,15,16,15,13,10,9]
    tuesday = [13,14,15,15,16,17,16,16,12,12]



    for temps in zip(sunday,monday, tuesday):
        print('min=',min(temps),'max=',max(temps),'average=',statistics.mean(temps))

    # {:6.1f} => chars width, 1 decimal precision floating point

    #chain
    alltemps = chain(sunday,monday,tuesday)
    print('all temps > 0',all(t> 0 for t in alltemps))





if __name__ == '__main__':
    main()
    exit(0)