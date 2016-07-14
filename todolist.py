from sys import argv

script, command = argv

txt = open('tasks.txt')


def print_todoList():
    line_num = 1
    line = txt.readline()
    print "%r %r" % (line_num, line)
    line_num += 1

# def add_todoList()


def todoList(command):
    if command == 'list':
        print_todoList()


todoList(command)
