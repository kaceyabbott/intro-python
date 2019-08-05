"""

Learn conditional repetition
two loops: for loops and while loops

"""

counter = 5

while counter != 0:
    print(counter)
    # augmented operators
    counter -= 1

print("outside while loop")

counter = 5

while counter:
    print(counter)
    counter -= 1

print("outside while loop")


# run forever
while True:
    print("enter a number")
    response = input()  #take user input
    if int(response) % 7 == 0:
            break       #exit loop


print("outside while loop")

