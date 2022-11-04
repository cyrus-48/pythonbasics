# 7. In this exercise, use the following variables: i, lo, hi, and result. Assume that lo and hi each are
# associated with an integer and that result refers to 0. Write a while loop that adds the integers from lo up
# through hi (inclusive), and associates the sum with result.

lo=int(input("Enter the value of lo: "))
hi=int(input("Enter the value of hi: "))
results=0

while lo<=hi:
    results+=lo
    lo+=1
    i=results
print(i)
 
