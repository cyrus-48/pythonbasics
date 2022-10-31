# Python has a set of built-in methods that you can use on strings.

# uppercase -> upper()
a = "Hello, World!"
print(a.upper())

# lowercase -> lower()
a = "Hello, World!"
print(a.lower())
# remove whitespace -> strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# replace string -> replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# split string -> method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# string concatenation -> to concatenate, or combine, two strings you can use the + operator.


# format string ->
# e can combine strings and numbers by using the format() method
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

