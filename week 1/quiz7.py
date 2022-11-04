# Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the
# list is equal to k or not.  For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.
def check_sum(nums, k)->bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                print("Numbers found : ",nums[i], " " , nums[j])
                print("sum : ", nums[i]+nums[j],"value of K : ", k)
                return True
    return False


num_of_element = int(input('Enter number of elements to be entered in the list: '))
list1 = []
for i in range(0, num_of_element):
    num = int(input(f'Enter element {i} of the list'))
    list1.append(num)
    print(list1)
k = int(input("Enter to number be compared with sum : "))
print(check_sum(list1 , k))
