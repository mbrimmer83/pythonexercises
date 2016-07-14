
import json
abbv = open('abbv.json', 'r')
abbreviations = json.loads(abbv.read())
# print abbreviations
abbv.close()

def text_interpretor(message):
    message_list = message.split(' ')
    for word in message_list:
        print abbreviations.get(word.upper())


text_interpretor(message = raw_input("Enter a message:"))
