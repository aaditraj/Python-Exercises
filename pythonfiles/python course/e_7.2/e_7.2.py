# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# When you are testing below enter mbox-short.txt as the file name.
# Desired Output:
# Average spam confidence: 0.750718518519

fil = input("File name: ")
fh = open(fil, 'r')
count = 0
prep_sum = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        bgn = line.find(':')
        no_sect = line[bgn+1:]
        prep_sum = prep_sum + float(no_sect)
avg = prep_sum/count
print("Average spam confidence: " + str(avg))
