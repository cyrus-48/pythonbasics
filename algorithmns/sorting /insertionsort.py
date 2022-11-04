#insertion sort 
# run time: O(n^2)
# space complexity: O(1)
# best case: O(n)
# worst case: O(n^2)
# average case: O(n^2)
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([9, 7, 4, 8, 6, 5, 3, 1, 2]))