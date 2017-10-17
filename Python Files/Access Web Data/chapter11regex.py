import re

name = input("Enter file:")
if len(name) < 1 : name = "sample"
handle = open(name)

numbers = list()

for line in handle:
	line = line.rstrip()
	if re.findall("[0-9]+", line):
		lineNumbers = re.findall("[0-9]+", line)
		numbers.extend(lineNumbers)
	else:
		continue

for x in range(0,len(numbers)):
	numbers[x] = int(numbers[x])

total = sum(numbers)
print (total)