# quick sort
# run time: O(n log n)
# space complexity: O(n)
# best case: O(n log n)
# worst case: O(n^2)
# average case: O(n log n)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    items_greater = []
    items_lower = []
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([9, 7, 4, 8, 6, 5, 3, 1, 2]))