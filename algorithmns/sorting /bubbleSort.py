#  pairs of adjacent elements are compared and the elements are swapped if they are not in order
# time complexity of O(n^2)
array = [9, 7, 4, 8, 6, 5, 3, 1, 2]


def bubbleSort(array):
    for i in range(len(array)-1):
        for x in range(0, len(array)-i-1):
            if array[x] < array[x + 1]:
                temp = array[x]
                array[x] = array[x + 1]
                array[x + 1] = temp


print(bubbleSort([9, 7, 4, 8, 6, 5, 3, 1, 2]))
