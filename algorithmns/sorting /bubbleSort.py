#  pairs of adjacent elements are compared and the elements are swapped if they are not in order
# time complexity of O(n^2)
# space complexity of O(1)
# stable sort
# in place sort
#best case: O(n)
# worst case: O(n^2)
# average case: O(n^2)
 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([9, 7, 4, 8, 6, 5, 3, 1, 2]))
