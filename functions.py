def print_two(*args):
    arg1, arg2, = args
    print "args1: %r, args2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "args1: %r, args2: %r" % (arg1, arg2)

def print_one(arg1):
    print "args1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("Matthew", "Brimmer")
print_two_again("Matthew", "Brimmer")
print_one("First!")
print_none()
