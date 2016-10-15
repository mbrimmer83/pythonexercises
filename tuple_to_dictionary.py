# mysql returns tuple which is like a list of lists
data = [
    ['title1', 'content1', 'image_url1'],
    ['title1', 'content2', 'image_url2'],
    ['title1', 'content3', 'image_url3'],
    ['title2', 'content4', 'image_url4'],
    ['title2', 'content5', 'image_url5'],
    ['title2', 'content6', 'image_url6'],
    ['title3', 'content7', 'image_url7'],
    ['title3', 'content8', 'image_url8'],
    ['title3', 'content9', 'image_url9']
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
