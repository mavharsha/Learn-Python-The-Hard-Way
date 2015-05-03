def add(a, b):
	return a +b
def sub(a, b):
	return a -b

def divide(a, b):
	return a * b

def multiply(a, b):
	return a * a

temp = add(10, 10)
print "Adding 10 and 10, result is %d" % (temp)
temp = sub(10, 10)
print "Sub 10 and 10, result is %d " % (temp)
temp = divide(10, 10)
print "Divide 10 by 10, result is % d " % (temp)
temp = multiply(10, 10)
print "Multiply 10 wtih 10 result is %d" % (temp)


# Puzzle 
temp = add(10, sub(10, multiply(10, divide(10,1))))
print "Result of the puzzle is %d" % temp
