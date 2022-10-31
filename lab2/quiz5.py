# 5. A regular polygon is an n-sided polygon in which all sides are of the same length and all angles have the same
# degree (i.e., the polygon is both equilateral and equiangular). The formula for computing the area of a regular
# polygon is area = (n * s^2) / (4 * tan(PI / n) Here, s is the length of a side. Write a program that prompts the
# user to enter the number of sides and their length of a regular polygon and displays its area.
import math
from math import tan


def areaOfPolygon(n: int, l: float) -> float:
    area: float = (n * pow(l, 2)) / (4 * tan(math.pi / n))
    return area


numberOfSides = int(input("Enter number of sides : "))
length = float(input("Enter length of the polygon : "))

area: float = areaOfPolygon(numberOfSides, length)
print(area)
