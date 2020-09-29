
handle = open(input('Enter file name: '), 'r')

grades = dict()
for line in handle:
    line_list = line.split()
    grades[line_list[0]] = grades.get(line_list[0], 0) + int(line_list[1])
    grades[line_list[0] + '_count'] = grades.get(line_list[0] + '_count', 0) + 1

while True:
    name = input("Enter name: ")
    if name in grades:
        print("The average for " + name + " is " + str(grades[name]/grades[name + '_count']))
    else:
        print("Sorry, I don't have information about that person.")
