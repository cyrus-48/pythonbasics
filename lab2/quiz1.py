# Given the variable x, y, and z, each associated with an int, write a fragment of code that assigns the largest of these to max.

def returnMax(x: int, y: int, z: int) -> int:
    max = 0
    if x > y and x > z:
        max = x
        return max
    if y > x and y > z:
        max = y
        return max
    if z > y and z > x:
        max = z
        return max
    return 0


x: int = int(input("Enter first number :"))
y: int = int(input("Enter second number: "))
z: int = int(input("Enter third number: "))
maxNum = returnMax(x, y, z)
print(maxNum, " : is the maximum number")
