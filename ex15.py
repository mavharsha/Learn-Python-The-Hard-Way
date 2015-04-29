from sys import argv

script, filename = argv

txt = open(filename)

print "Here's iyour file %r" % filename
print txt.read()

print "Type your filename:"
filename = raw_input(">")

txt_again = open(filename)

print txt_again.read()
