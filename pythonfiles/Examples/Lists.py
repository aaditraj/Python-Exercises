numbers = [5,8,2,6,4,0,8, 3, 4, 5, 2, 4, 5, 9, 7, 8, 6,4, 3,24,5,77,44,3]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)
