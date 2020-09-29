# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the
# number. Enter the numbers from the book for problem 5.1 (4,5,junk,7) and match the desired output as follows:
# Invalid input
# Maximum is 7
# Minimum is 4

largest = None
smallest = None
while True:
    current_num = input("Give me a number: ")
    if current_num == 'done':
        print(largest, smallest)
        break
    try:
        current_num = float(current_num)
        if largest is None:
            largest = current_num
        elif current_num > largest:
            largest = current_num
        if smallest is None:
            smallest = current_num
        elif current_num < smallest:
            smallest = current_num

    except:
        print("That is not a valid number.")
        
    
