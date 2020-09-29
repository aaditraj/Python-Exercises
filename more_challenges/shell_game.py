info = input().split()
# print(info)
location = info[1]
# print(location)
for i in range(int(info[0])):
    swap = input()
    swap_list = swap.split()
    if location in swap_list:
        if swap_list.index(location) == 0:
            location = swap_list[1]
        elif swap_list.index(location) == 1:
            location = swap_list[0]

print(location)
