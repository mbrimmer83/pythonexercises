print "How old are you?"
user_input = raw_input()

try:
    print user_input * user_input
    print user_input
    print user_input + user_input
except:
    print "Cant perform that operation"
