"""
working with dictionaries (hashes)
dictionaries maps keys to values.
in some languages are know as associative arrays, hashes, or maps
create them using {} containing a key value pair
retrieve them by [key value]
"""

d = {'alice':'801-123-45-8998',
     'pedro': '956-445-78-8996',
     'john':'654-321-66-4477'}

print(d, type(d))

print(d['alice'])


#add memebers to the dictionary, of names -> grades

roster = {} #empty dictionary


count = 0

while count < 3:
     name = input("enter name of student: ")
     grade =input ("enter grade of student: ")

     roster[name] = grade

     count +=1

print(roster)
print(roster['kacey'])

