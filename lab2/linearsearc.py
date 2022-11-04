# linear search

def linear_search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None
# call the function 

my_list = [1, 3, 5, 7, 9]
print(linear_search(my_list, 3))  # => 1
print(linear_search(my_list, 3))  # => 1