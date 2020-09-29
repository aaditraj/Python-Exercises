def isprime(num):
    integer = int(num)
    for i in range(2, (integer//2)):
        if integer%i == 0:
            return "This is a composite number"
    return "This is a prime number"

while True:
    number = input("Enter a number:")
    print(isprime(number))
