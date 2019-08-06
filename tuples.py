"""
workins with tuples and collections etc...
"""

def do_tuples():
    #use () to define tuples. immutable sequence of objects
    t = ("ogden", 1.99, 2)
    print(t, type(t))
    print("size", len(t))
    print("one memeber", t[0])

    for item in t:
        print(item)
        #single tuples must end with comma
        t1 = (6,)
        print(t1, type(t1))

        #paranthesis are optional
        t2 = 1, 2, 3, 4, 5
        print(t2, type(t2))

def minmax(items):
    #returns min and max of a list
    return(min(items),max(items))

def swap(a,b):
    return b,a



def main():
    """
    test function
    :return: 
    """
    # do_tuples()

    min, max = (minmax([56,76,12,90,-1]))
    print('min', min, 'max', max)
    a = "jelly"
    b = "bean"
    a,b =swap(a,b)
    print(a,b)

if __name__ == '__main__':
    main()
    exit(0)