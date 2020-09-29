# 9.4 Write a program to read through the mbox-short.txt and figure out who has the
# sent the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail. The program
# creates a Python dictionary that maps the sender's mail address to a count of the
# number of times they appear in the file. After the dictionary is produced, the
# program reads through the dictionary using a maximum loop to find the
# most prolific committer.

fil = input("File name: ")
handle = open(fil, 'r')
counts = dict()

for line in handle:
    if line.startswith("From"):
        spl_line = line.split()
        counts[spl_line[1]] = counts.get(spl_line[1], 0) + 1

bigperson = None
bigcount = None
for address in counts:
    if bigcount is None or counts[address] > bigcount:
        bigcount = counts[address]
        bigperson = address

print(bigperson + " is the most prolific committer with " + str(bigcount) + " messages")
