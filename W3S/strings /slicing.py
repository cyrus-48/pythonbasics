# ypu can return a range of charcaters ina string by using the slice syntax.
# specify the start index and the end index, seperated by a colon to return a part of a string
b = "Hello, World!"
print(b[2:5])

# SLICE FROM THE START
# By leaving out the start index, the range will start at the first character:

b = "Hello, World!"
print(b[:5])

#slice to the end -> By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])
