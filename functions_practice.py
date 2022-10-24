def hello():
    print('hello world!')


def pack(a, b, c):
    return [a, b, c]


def eat_lunch(*items):
    print('First I eat ' + items[0])
    for i in items[1:]:
        print('Next I eat ' + i)


hello()
print(pack('a', 'b', 'c'))
eat_lunch('a', 'b', 'c', 'd', 'e', 'f')
