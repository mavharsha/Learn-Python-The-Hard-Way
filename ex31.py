
print "You enter a dark room with two doors. Do you want to go through door #1 or #2"

door = raw_input(">")

if door == "1":
	print "There is a giant bear here, eating cheese cake. What do you want to do?"
	print "1. Take the cheese cake."
	print "2. Scream at the bear."

	bear = raw_input(">")

	if bear == "1":
		print "You were hungry, you ate the cake. The bear was hungry, it ate you! Good Job!"
	elif bear == "2":
		print "Better luck finding food!"
	else:
		print "Bad option"

else:
	print "You entered door #2. KAABOOM! You are dead!"
