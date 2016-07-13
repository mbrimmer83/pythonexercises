# def nbox(n):
#     stars = ""
#     count = 0
#     count2 = 0
#     while count < n:
#         stars += "*"
#         count += 1
#     while count2 < n:
#         print stars
#         count2 += 1
#
#
# nbox(5)

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


# def string_split(str):
#     string = split(str)
#     print string
#     return
#
# string_split("I am learning the Python language!")
