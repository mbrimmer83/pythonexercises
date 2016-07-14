from sys import argv

script, file_name = argv


def word_summary(file_name):
    word_sum = {}
    txt = open(file_name)
    the_txt = txt.read().lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('\n', ' ').split(' ')
    txt.close()

    for word in the_txt:
        if word not in word_sum:
            word_sum[word] = 0
        word_sum[word] = word_sum[word] + 1
    print word_sum


word_summary(file_name)
