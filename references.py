"""
playing with references

"""

def modify(k):
    """
    modify the countent of a list
    :param k:
    :return: nothin
    """
    # list are pass by reference
    k.append(39)
    print("k = ",k)

def replace(g):
    """
    replace input list locally
    :param g: input list
    :return: nothing
    """
    g = [17, 48, 89]
    print("g =",g)

def replace_content(g):
    """
    replace input list globally
    input list
    return nothing
    """
    g[0] = 88
    g[1] = 22
    g[2] = 44
    print("g = ", g)


def main():
    """
    test func
    :return: nothin
    """
    m = [9, 15, 24]
    print("before modify() m = ", m)
    modify(m)
    print("after modify() m = ", m)
    replace(m)
    print("after replace() m =", m)
    replace_content(m)
    print("after replace content", m)


if __name__ == '__main__':
    main()
    exit(0)