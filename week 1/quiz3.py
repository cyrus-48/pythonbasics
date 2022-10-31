def absent_digits(n):
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    n = set([int(i) for i in n])
    n = n.symmetric_difference(all_nums)
    n = sorted(n)
    return n

mobile_num = int(input('Enter mobile number : '))

print(mobile_num)

list1 = list(map(int, str(mobile_num)))
if len(list1) == 10:
    print(list1)
    print(absent_digits(list1))

else:
    print('Please enter 10 digits!!')






