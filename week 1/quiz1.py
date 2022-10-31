# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from
# each other.

def test_distinct(data:list)->bool:
    # len(data) return the length of the list , len(set(data)) returns the lenght of the set formed after parding the
    # list to set.
    if len(data) == len(set(data)):
        return True
    else:
        return False;


num_of_element = int(input('Enter number of elements to be entered in the list: '))
list1 = []
for i in range(0, num_of_element):
    num = int(input('Enter element of the list'))
    list1.append(num)
    print(list1)

print(test_distinct(list1))
