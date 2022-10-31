#Write a Python program that accepts six numbers as input and sorts them in descending order.
print("Input six integers:")
list1:list= []
for n in range(0, 6):
    elem = int(input("Enter Element to be added in the list : "))
    list1.append(elem)
    print(list1)
nums = list(map(int, list1))
print(nums.reverse())
print('Before sorting the set of numbers : ')
print(list1)
print("After sorting the set of numbers ")
print(*nums)
