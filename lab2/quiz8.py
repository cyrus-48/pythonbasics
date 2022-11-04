from math import sqrt
from tracemalloc import start


def computePerfectSqaures(k: int, m:int) -> None:
    q = 0
    for i in range(k, m):
        sr = int(sqrt(i))
        if (sr * sr) == i:
            q = q + 1
            print(i)

    print("number of perfect squares : ", q)

print("Enter the range of numbers : ")
start:int = int(input("Enter the start of the range : "))
end:int = int(input("Enter the end of the range : "))
computePerfectSqaures(start, end)
 
