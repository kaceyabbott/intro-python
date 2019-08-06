"""
learn about scoping in python
"""
count = 0 #global object

def show_count():
    """
    display current count
    :return: nothin
    """
    print(count)

def set_count(num):
    global count
    count = num

def main():
    """
    test function
    :return: 
    """
    show_count()
    set_count(9)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)