numbers = [1,54,2,6,42,5,6,3,4,6,4,5,6,2,6,4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
