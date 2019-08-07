"""
working with sets
an unordered collections of unique, immutable objects
define using {} do not need a key
you cna use the set() constructor to creat one
"""


def main():
    """
    test function
    :return: 
    """
    p = {4,654,18,79,65}
    print(p,type(p))
    data = [1,3,4,2,88,3,1]
    # eleminate duplicates
    sdata = set(data)
    print(sdata, type(sdata))
    #iterate with for
    for item in sdata:
        print(item)
    #supports memebership testing: in, not in
    print(5 in sdata)
    print(5 not in sdata)
    #adding elements to a set:

    sdata.add(45)
    print(sdata)
    sdata.update([2,99,44,33,1,2,88])
    print(sdata)
    #removing elements
    sdata.remove(44) #if not there will cause error
    print(sdata)
    sdata.discard(77) #no error
    print(sdata)
    #copy sets
    bk_data = sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)

    #### define some sets
    blueeyes = {"olivia", "harry", "lily", "jack"}
    blondehair = {"harry", "jack", "amelia", "mia", "joshua"}
    smellhcn = {"harry", "amelia"}
    tasteptc = {"harry", "lily", "amelia", "lola"}
    oblood = {'mia','joshua','lily','olivia'}
    bblood = {'amelia','jack'}
    ablood = {'harry'}
    abblood = {"joshua","lola"}

    print(blueeyes.union(blondehair))
    print(blueeyes.intersection(tasteptc))
    print(smellhcn.symmetric_difference(ablood))
    print(blondehair.difference(ablood))
    print(tasteptc.issuperset(smellhcn))


if __name__ == '__main__':
    main()
    exit(0)