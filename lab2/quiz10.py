def printSequence(s1: str, s2: str) -> str:
    s3 = ""
    for i in range(len(s1)):
        s3 += (s1[i] + s2[i])
    return s3


s1: str = input("Enter a string : ")
s2: str = input("Enter string 2 : ")
print(printSequence(s1, s2))
