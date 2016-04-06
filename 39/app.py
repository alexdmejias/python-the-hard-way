states = {
  'oregon': 'or',
  'florida': 'fl',
  'california': 'ca',
  'new york': 'ny',
  'michigan': 'mi'
}

cities = {
  'ca': 'san francisco',
  'mi': 'detroit',
  'fl': 'jacksonville'
}

cities['ny'] = 'new york'
cities['or'] = 'portland'

# print out some cities
print '-' * 10
print 'ny state has: ', cities['ny']
print 'or state has: ', cities['or']

# print out some states
print '-' * 10
print 'michigan\'s abbreviation is: ', states['michigan']
print 'florida has: abbreviation is: ', states['florida']

# do it by using the state then cities dict
print '-' * 10
print 'michigan has: ', cities[states['michigan']]
print 'florida has: ', cities[states['florida']]

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
  print "%s is abbreviated %s" % (state, abbrev)

#print every city in state
print '-' * 10
for city, abbrev in cities.items():
  print "%s has the city %s" % (abbrev, city)

#now do both at the same time
print '-' * 10
for state, abbrev in states.items():
  print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('texas')

if not state:
  print "sorry, no texas"

#get a city with a default value
city = cities.get('tx', 'does not exist')
print "the city for the state 'tx' is: %s" % city