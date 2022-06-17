#!/usr/bin/python3

list1 = [0,1,2,4]
new_list = []
for index, value in enumerate(list1):
    print(value, index)
    rslt = value % 10
    print(rslt)
    if rslt == index:
        new_list.append(index)
print(new_list)
minimum_value = min(new_list)
print(minimum_value)

