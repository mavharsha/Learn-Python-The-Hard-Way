from sys import argv

script, filename = argv

print "We are going to erase %r. " %filename
print "If you don't want that, hit CTRL - C(^C)"
print "If you do wabt that, hit return."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going ask you for three lines"

line1 = raw_input("Line1 :")
line2 = raw_input("Line2 :")
line3 = raw_input("Line3 :")
print "I'm going to write these lines to the file %r. " % filename

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we are closing it!"
target.close()






