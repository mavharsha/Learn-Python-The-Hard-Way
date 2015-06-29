# split(' ')
# sorted(words)
# pop(0) prints the first word after popping it off
# pop(-1) prints the last word after popping it off


def break_to_words(stuff):
	"""This function will break up words for us"""
	words = stuff.split(' ')
	return words

#print break_to_words("Dumbo is too good to be awesome!")

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)
#print sort_words(break_to_words("c b a da aa"))

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print "Print the first word"
	print word


array = "DUMBO is too good"
words = array.split(' ')

print_first_word(words)
print_first_word(words)

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print "Printing the last word"
	print word

print_last_word(words)



#print print_first_word(break_to_words("First Second Third"))
