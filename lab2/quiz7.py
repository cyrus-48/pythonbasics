  # 7. In this exercise, use the following variables: i, lo, hi, and result. Assume that lo and hi each are
  # associated with an integer and that result refers to 0. Write a while loop that adds the integers from lo up
  # through hi (inclusive), and associates the sum with result.
lo = int(input("Enter integer associated to lo and hi : "))
result = 0
i = lo

while i <= hi:

       result = result + i

       i += 1