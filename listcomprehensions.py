"""
list comprehensions
readble, expressive, and effective
"""
from math import factorial, sqrt
from pprint import pprint as pp



def prime(p):
    if p <2:
        return False
    for i in range(2, int(sqrt(p))+1):
        if p % i == 0:
            return False
    return True

def main():
    """
    test function
    :return: 
    """
    words = 'today i am very happy to learn about list comprehensions'.split()
    #print(words)
    data = [] # empty list
    for word in words:
        #some analysis
        data.append(word)

    #filter data
    print(words)

    #task: find the length of the first 20 factorial numbers
    #factorial numbers
    length = []
    for x in range(20):
        #print(factorial(x))
        length.append(len(str(factorial(x))))

    print(length)

    #use a list comprehensoin: []
    info2 = [len(str(factorial(x))) for x in range(20)]
    #print(info2)
   # pp(info2)

    #set comprehensions: ()
    info3 = {len(str(factorial(x))) for x in range(100)}
    #pp(info3)

    #dictionary comprehensions
    nbateams = {"jazz": "slc","warriors":"oakland","lakers":"la", 'clippers':'la'}

    teamsnba = {city:mascot for mascot, city in nbateams.items()}
    pp(nbateams)
    pp(teamsnba)

    #filter predicates



    primenums = [x for x in range(10) if prime(x)]
    pp(len(primenums))







if __name__ == '__main__':
    main()
    exit(0)