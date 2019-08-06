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
    #split record
    print(combine.split(" : "))
    departure, _, arrival = "london:edinburgh".partition(":")
    print(departure, arrival)

    print("the age of {0} is {1}".format("mario", 34))
    print("the age of {0} is {1}, and the birthday of {0} is {2}".format("mario", 34, "august 12"))

    print("the age of {} is {}".format("mario", 34))

    #by field name
    print("current position {latitude} {longitude}".format(latitude = "60 N", longitude = "5E"))

    x = 10
    y = 20
    #prints elements of list
    print("galatic position x = {pos[0]}, y = {pos[1]}".format(pos=(x,y)))





if __name__ == '__main__':
    main()
    exit(0)