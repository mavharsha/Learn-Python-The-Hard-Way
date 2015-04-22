print "How old are you?",
age = int( raw_input())
print "How tall are you?",
height = raw_input()
print "How much does an elephant weight?",
weight = raw_input()

print "So, you're %r old, %rtall and %r heavy." % (age,
height, weight)

# check the difference of typecasted and non typecasted
# once typecasted the string is converted into integer
# %r of height gives a string '<value entered>'
