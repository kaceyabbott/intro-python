"""
playing with random and magic
simulate 6000 roles of a die (1-6)
"""

import random
import statistics

def roll_die(num=6000):
    """
    random roll of a die
    :param num: number of rolls
    :return: list of frequencies
    index 0 maps to 1
    """
    freq = [0]*6 #initalize values to zero

    for roll in range(num):
        n = random.randrange(1, 7)
        freq[n-1] +=1
        #print(freq)
        #freq.append(random.randint(1, 6))

    return freq






def main():
    """
    test function
    :return: 
    """
    num = int(input("how many rolls"))
    results = roll_die(num)
    for roll, total in enumerate(results):
        print("total rolls of {} = {}".format(roll+1,total))

    print("average = {}".format(sum(results)/len(results)))
    print("median = {}".format(statistics.median(results)))



if __name__ == '__main__':
    main()
    exit(0)