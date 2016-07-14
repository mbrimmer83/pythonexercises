aditi = {
  'name': 'Aditi',
  'email': 'aditi@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print aditi['email']
print aditi['interests']

for friend in aditi['friends']:
    if friend['name'] == 'Jasmine':
        print friend['email']

for friend in aditi['friends']:
    if friend['name'] == 'Jan':
        print friend['interests'][1]
