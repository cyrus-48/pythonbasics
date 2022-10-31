from math import sqrt


def computePerfectSqaures(k: int, m:int) -> None:
    q = 0
    for i in range(k, m):
        sr = int(sqrt(i))
        if (sr * sr) == i:
            q = q + 1
            print(i)

    print("number of perfect squares : ", q)


computePerfectSqaures(100, 400)
