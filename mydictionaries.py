"""
playing with dictionaries
"""
from pprint import pprint as pp


def main():
    """
    test function
    :return: 
    """
    urls = {
        "google": "www.google.com",
        "yahoo": "yahoo.com",
        "twitter": "www.twitter.com",
        "wsu": "weber.edu"
    }

    print(urls,type(urls))
    # access by key: [key]
    print(urls["wsu"])
    #build dict with dict() constructor
    names_age = [('Alice',32),('mario',32),('hugo',21)]
    d = dict(names_age)
    print(d)
    #another way
    phonetic = dict(a = 'alpha', b = 'bravo', c = 'charlie', d = 'delta')
    print(phonetic)
    #make a copy
    e = phonetic.copy()
    print(e)
    #updating a dictionary update()
    stock = {'goog': 897, 'AAPL': 416, 'ibm':194}
    print(stock)
    stock.update({'goog':999, 'Yhoo':2})
    print(stock)
    #iteration default is by key value
    for key in stock:
        print('{k} = {v}'.format(k = key, v = stock[key]))

    #iterate by values
    for val in stock.values():
        print('val = ', val)

    #iterate by both key and value with: items()
    for items in stock.items():
        print(items)
    for key, val in stock.items():
        print(key, val)

    # test for membership in, not in via key
    print("goog" in stock)
    print("win" not in stock)

    #deleting: del keyworkd
    print(stock)
    del stock['Yhoo']
    print(stock)

    #mutablility of dictionaries
    isotopes = {
        'H': [1,2,3],
        'He': [3,4],
        'Li': [6,7],
        'Be': [7,9,10],
        'B': [10,11],
        'C': [11,12,13,14]
    }

    pp(isotopes)
    isotopes['H'] += [4,5,6,7]
    pp(isotopes)
    isotopes['N'] = [13,14,15]
    pp(isotopes)










if __name__ == '__main__':
    main()
    exit(0)