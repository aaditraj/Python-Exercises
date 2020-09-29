matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

#List functions
numbers = [5, 2, 1, 7, 4]

numbers.sort()

numbers.reverse()

numbers.append(20)
print(numbers)

numbers.insert(2, 20)
print(numbers)

numbers.remove(4)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(5))
print(1 in numbers)

numbers.clear()
print(numbers)





