
def add1(a: int, b: int):
    return a + b


def also_add(a, b):
    return a + b


def last_letter_firstname(fullname):
    firstname = fullname.split()[0]
    return firstname[-1]


if __name__ == '__main__':
    first, second = 10, 20
    third, fourth = 3.2, 1.7
    print(add1(first, second))
    print(also_add(first, second))
    print(also_add(third, fourth))
    print(last_letter_firstname("Joe Biden"))
