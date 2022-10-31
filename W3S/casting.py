# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an
# object-orientated language, and as such it uses classes to define data types, including its primitive types.

# casting in python is therefore done using constructor functions:
# int() -> constructs an integer from an integer

x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

# literal, a float literal(by removing all decimals) ,or a string literal (provided the string represents a whole
# number).

# float() -> construct a float number from an integer literal, a float literal or a string literal(provided the string represents a float or an integer)

x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2

# str() -> constructs a string from wide variety of data types including strings , int and float literals.
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'