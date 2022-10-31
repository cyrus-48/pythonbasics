# string in pyton is an array of characters surrounded by single or doubel quotation marks
# 'hello' or "hello"

print("Hello")
print('Hello')

# ASSIGNING A STRING TO VARIABLE
# Assigning string to variable is done with the variable name followed by an equal sign and the string
a = 'hello'
print(a)

# MULTILINE STRINGS
# You can assign multiline string to a variable using 3 qoutes
c = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(c)

# Strings are arrays
# like any other programming language , strings in python are arrays of bytes representing unicode characters
# however python does not have character data type, a single character is simply a string with a length of 1

# square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])

# LOOPING THORUGH A STRING
# since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in 'banana':
    print(x)

# String length -> to get the length of a string use the function >> len()
a = 'hello world'
print(len(a))

# CHECK STRING ->  to check if a certain phrase or character is present ina string, we can use the keyword in
txt = 'the best things in life are free'
print("free" in txt)  # this statement will return true

