import out as out

s1 = "hello"
s2 = "wprld"

def printSequence(s1, s2):
    s3 = ""
    for i in range(len(s1)):
         s3 += (s1[i] + s2[i])
    print(s3)


printSequence(s1, s2)
