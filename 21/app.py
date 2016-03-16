def add(a, b):
  print "adding %d + %d" % (a, b)
  return a + b

def subtract(a, b):
  print "subtracting %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "multiplying %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "divinding %d / %d" % (a, b)
  return a / b

age = add(20, 5)
height = subtract(20, 5)
weight = multiply(20, 6)
iq = divide(50, 10)

print "age %d, height %d, weight %d, iq %d" % (age, height, weight, iq)

print "here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "that becomes: ", what, "can you do it by hand?"
