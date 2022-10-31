def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                 return True
    return False


num_of_element = int(input('Enter number of elements to be entered in the list: '))
list1 = []
for i in range(0, num_of_element):
    num = int(input('Enter element of the list'))
    list1.append(num)
    print(list1)

print(check_sum(list1 , 5))

for i in list1:
     print(i)