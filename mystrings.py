"""
playing with strings
"""


def main():
    """
    test function
    :return: 
    """
    s1 = "this is super cool"

    print(len(s1))
    #concatination "+'
    s2 = "weber " + "state "+ "university"
    print(s2)
    #if you need to join big strings join()

    teams = ["real madrid", "barcelona", "manchester united"]
    combine = " : ".join(teams)
    print(combine)


if __name__ == '__main__':
    main()
    exit(0)