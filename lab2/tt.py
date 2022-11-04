my_list = [3, 1, 2, 4]
my_tuple = ('A', 'b', 'c', 'd')
my_list.sort()
counter = 0
for a in my_tuple:
  my_list[counter] += int(a)
  counter += 1
  break
print(my_list)