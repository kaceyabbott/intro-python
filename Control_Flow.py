"""
Learn about control cflow in python.
"""

# IF statement
# indentation is 4 spaces

if True:
    print("it is true")

if bool("eggs"):
    print("yes please!")
if "eggs":
    print("Yes, why not")

#flat is better than nested

h = 101

if h> 50:
    print("greater than 50")
    if h > 100:
        print("greater than 100")

elif h < 50 :  # else if

    print('less than 50')

else:
    print("equals 50")



#######
print("done")