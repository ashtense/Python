ten_things = "Apples oranges crows telephone light sugar"

print "Wait there's not 10 things in that list. lets fix that!!"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Evening", "Geronimo", "THC", "Uncle Joey"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding %s" % next_one
    stuff.append(next_one)
    print "there are %d items now" % len(stuff)

print "There we go: ", stuff

print "Lets do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print ' # '.join(stuff[3:5])
