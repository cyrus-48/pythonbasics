# Given the variable x, y, and z, each associated with an int, write a fragment of code that assigns the largest of these to max.
def returnMax(x, y, z):
    max = 0
    if x > y and x > z:
        max = x
        print(max)
    if y > x and y > z:
        max = y
        print(max)
    if z > y and z > x:
        max = z
        print(max)


returnMax(34, 44, 56)
returnMax(30084,3454443234,45555)