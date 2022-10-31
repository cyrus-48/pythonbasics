items = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
beg = int(items[1])
end = int(items[len(items) - 1])
mid_value = int((beg + end) / 2)
item = 10
while beg <= end and items[mid_value] != item:
    if item < items[mid_value]:
        end = mid_value - 1
    else:
        beg = mid_value + 1
    mid_value = int(beg + end) / 2
if items[mid_value] == item:
    print("item exists : ", items)
else:
    print("item does not exist")

print(int(mid_value))
