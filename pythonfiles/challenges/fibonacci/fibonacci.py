while True:
    fibonacci = [1, 1]
    first = 0
    second = 1
    number = int(input("Please enter a number: "))
    if number > len(fibonacci):
        for i in range(number - len(fibonacci)):
            fibonacci.append(fibonacci[first] + fibonacci[second])
            first += 1
            second += 1
        print(fibonacci[number-1])
    else:
        print(1)
