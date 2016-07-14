def nbox(n):
    stars = ""
    count = 0
    count2 = 0
    while count < n:
        stars += "*"
        count += 1
    while count2 < n:
        print stars
        count2 += 1


nbox(5)

def square(n):
    for i in xrange(0, n):
        print "*" * n

n = int(raw_input("Enter a number:"))
square(n)

def empty_box(height, width):
    stars_width = ""
    counter = 0
    while counter < width:
        stars_width += "*"
        counter += 1
    print stars_width
    counter = 0
    stars_height = "*"
    while counter < width - 2:
        stars_height += " "
        counter += 1
    stars_height += "*"
    counter = 0
    while counter < height - 2:
        print stars_height
        counter += 1
    print stars_width

empty_box(10, 10)

def box(h, w):
    print "*" * w
    star_w = "*"
    for i in xrange(0, w):
        if i < w:
            star_w += " "
        elif i == (w - 1):
            star_w += "*"
    for i in xrange(0, h - 2):
        print star_w
    print "*" * w

def string_split(string, delim):
    result = []
    startIndex = 0
    endIndex = string.index(delim)

    while True:
        part = string[:endIndex]
        result.append(part)
        startIndex = endIndex + len(delim)
        string = string[startIndex:]

        if delim in string:
            endIndex = string.index(delim)
        else:
            result.append(string)
            break
    return result

print string_split('JavaScript', 'a')
