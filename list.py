"""
working with lists
unlike strings, lists are mutable.
you can update and append elements to it.

"""
#use [] to define a list
l = [1, 2, 3]
print("list", l, type(l))
#a list of objects (any type)

a = ["apple", "orange", "pear"]
#access by index notatoin
print(a, a[1])

#replace an element
a[0] = "tomatoes"

print(a, a[0])

a[1] = 3.14
print(a)

#begin with an empty list

names = []

count = 0

while count < 3:
    name = input("enter a name: ")
    #print(name)
    names.append(name)
    count += 1

print(names)