i = 0
numbers = []
a = int(raw_input("please type the numbers > "))
while i < a:
	print "At the top i is %d" %i
	numbers.append(i)
	i = i + 1
	print "Numbers now: ",numbers
	print "At the bottom i is %d" %i

print "The numbers: "
for num in numbers:
	print num