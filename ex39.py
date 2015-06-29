# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
	}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Fancisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
	}

# add some more cities

cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

# print out some cities
print '-'* 10
print "Ny state has: ", cities ['NY']
print "OR state has: ", cities ['OR']

# print some states
print '-'* 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]


print "-"*20
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)


print "-"*20
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

print "-"*20
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])


print "Texas in states? ", states.get('Texas')
print "Texas in states? ", states.get('Texas','Does not Exist')
