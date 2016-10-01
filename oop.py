import sys
response = 'flee'
exit = raw_input("Type yes or no")
while response != 'fight':
    if exit != 'no' and  exit != 'yes':
        print "This is not a valid choice!"
        exit = raw_input("Type yes or no")
    elif exit == 'yes':
        print "Get ready to fight!"
        response = 'fight'
    elif exit == 'no':
        sys.exit()

print "This happened!"
