"""
playing with lists a little bit more
"""


def main():
    """
    test function
    :return: 
    """
    s = "show how to do it".split()
    print(s)
    # acces by index
    print("s[3]", s[3])
    print("last member", s[len(s)-1])
    #instead use negative index
    print("s[-1]", s[-1])
    # slicing
    print(s)
    print("from 1 to one before last", s[1:-1])
    print('from position all to end', s[2:])
    print('from begining to 3', s[:3])
    # amke a copy of list
    t = s #shallow copy
    print('s',s)
    print("t", t)
    print("t is s:", t is s)
    t = s[:] # deep copy
    # t is s.copy()
    # t = list(s)
    print("t is s:", t is s)
    print(type(t),type(s))
    # shallow copies
    # A list of list
    a = [[1,2],[3,4]]
    print(a,type(a))
    print("a[0]:", a[0])
    print("a[0][1]", a[0][1])
    #copy the list of list

    b = a[:]
    a[0] = [1,2]
    print(a ==b)

    #modify a[1]
    a[1].append(5)
    print("a1", a[1])
    print("b1", b[1])
    print('is a = b', a[1] is b[1])
    print("a", a)
    print("b", b)

    #repetition
    c = [21, 37]
    d = c*4
    print(d)
    s = [[-1,1]] *5
    print(s)
    s[1].append(7)
    print(s)

    #index()
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print(i)
    print("the index of fox entry is", i , w[i])
    #i = w.index('cat')
    #print(i)

    #membership testing with count()
    print("'the' value is", w.count('the'))
    #also test mempership in, not in
    print(37 in [12,22,37,99])
    print(88 not in [12, 22, 37, 99])
    # removing elements from list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(len(w),w)
    del w[3]
    print(len(w),w)

    # remove using: remove()
    w.remove("over")
    print(len(w),w)

    #rearranging list of elements
    g = [1,11,123,12111,654654]
    print(g)
    g.reverse() #permanent change
    print("reverse g", g)
    g.reverse()

    #sorting mehtod accepts 2 arguments, key and reverse
    d = [21,654,978,741,852,101,1]
    print("before sort",d)
    d.sort()
    print("after sort", d)
    d = [21, 654, 978, 741, 852, 101, 1]
    d.sort(reverse = True)
    print("sort.reverse d:", d)

    #sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    w.sort(key = len)

    print(w)






if __name__ == '__main__':
    main()
    exit(0)