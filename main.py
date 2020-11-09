
def add1(a: int, b: int):
    return a + b


def also_add(a, b):
    return a + b


if __name__ == '__main__':
    first, second = 10, 20
    print(add1(first, second))
    print(also_add(first, second))
