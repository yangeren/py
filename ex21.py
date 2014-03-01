#from sys import argv
#script, fi2 = argv
#
#def file_1(f1):
#	a = open(f1)
#	print a.read()
#	pass

#def file_2(f2):
#	b = open(f2,"w")
##	w = raw_input("please input something on this ~~\n> ")
#	w = "1234567890\nabcdefghigklmnopqrstuvwxyz\n!@#$%^&*()\n"
#	b.write(w)
#	pass
#
##file_1(fi1)
#file_2(fi2)
#
#

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b 
	pass

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 
	pass

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b 
	pass

def divide(a, b):
	print "DIVIDING %d / %d " % (a, b)
	return a / b
	pass

print "Let's do some math with just functions"

age = add(30, 5) #35 
height = subtract(78, 4) #74
weight = multiply(90, 2) #180
iq = divide(100, 2) #50

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height,weight,iq)



#A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print 4391
print "That becomes: ", what, "Can you do it by hand?"
