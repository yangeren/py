#from sys import argv
#
#script, filename = argv
#txt = open(filename)
#print "Here's your file %r" % filename
##print txt.read()
#print txt.readline(20)
#print txt.readlines(2)
#print txt.name
#print txt.encoding
#txt.close()
#
#print "Type the filename again:"
#file_again = raw_input("> ")
#
#txt_again = open(file_again)
#
#print txt_again.read()




from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, his RETURN."


raw_input("? ")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

target = open(filename)
print target.read()