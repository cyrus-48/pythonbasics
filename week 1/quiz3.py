# Write a Python program to find the digits which are absent in a given mobile number.
def absent_digits(n) -> set:
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    n = set([int(i) for i in n])
    n = n.symmetric_difference(all_nums)
    n = sorted(n)
    return n


mobile_num = (input('Enter mobile number : '))

print(mobile_num)

list1 = list(map(int, mobile_num))
if len(mobile_num) == 10:
    print(list1)
    print("missing numbers : ",absent_digits(list1))

else:
    print('Please enter 10 digits!!')
