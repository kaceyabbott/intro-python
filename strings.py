"""
Learning strings and collections

A string is a immutable sequence of unicode code-points
"""

print('This is a string')
print("this is a string too")


# concatenation and adjacent strings

s1 = "First"
s2 = "Second"

print(s1 + s2)

# Multi line strings and new lines

s3 = """This is a
multi line
string"""

print(s3)

s4 = "this is\na mulitline \nstring"
print(s4)

#Support for backslash

s5 = "A\\in a string"

print(s5)

s6 = 'this is " wow'
print(s6)

#raw strings

raw_string = r'c:\User\documents\books'
print(raw_string)

# string as sequence

s = "parrot"
print("s[4]", s[4], type(s))  #index notation: 0, 1, 2...

print(s, s.capitalize())





