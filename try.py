print "How old are you?"
user_input = raw_input()

try:
    inp = int(user_input)
    print inp * inp
except ValueError:
    print "Please enter an integer"
    user_input = raw_input()
try:
    inp = int(user_input)
    print inp * inp
except ValueError:
    print "You are an idiot!"
