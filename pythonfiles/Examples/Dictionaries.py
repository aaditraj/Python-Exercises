customer = {
    "name": "John Smith",
    "age":30,
    "is_verified":True
}

print(customer["name"])

# this will fail because birthdate is not a key: print(customer["birthdate"])

customer["name"] = "Jack Smith"
print(customer["name"])
print(customer.get("birthdate", "Jan 1 1980"))

phone = input("Phone: ")

numbers = {
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output = ""
for i in phone:
    output += numbers.get(i, "!")
    output += " "
    
print(output)
    
    




