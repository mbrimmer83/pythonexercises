# mysql returns tuple which is like a list of lists
data = [
    ['title1', 'content', 'image_url'],
    ['title1', 'content', 'image_url'],
    ['title1', 'content', 'image_url'],
    ['title2', 'content', 'image_url'],
    ['title2', 'content', 'image_url'],
    ['title2', 'content', 'image_url'],
    ['title3', 'content', 'image_url'],
    ['title3', 'content', 'image_url'],
    ['title3', 'content', 'image_url']
]
# The new data will be a list of dictionaries
def create_dictionary(data):
    new_data = []
    counter = 0
    content = []
    for idx in data:
        new_content = [
        idx[1],
        idx[2]
        ]
        content.append(new_content)
        counter += 1
        if counter == 3:
            counter = 0
            new_dict = {
                'title': idx[0],
                'content': content
            }
            new_data.append(new_dict)
            content = []
    return new_data
the_data = create_dictionary(data)
for data in the_data:
    print data['title']
    print data['content']
