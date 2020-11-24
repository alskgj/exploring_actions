import typing

def builder(n: int) -> typing.List[int]:
    """
    >>> builder(3)
    [0, 3, 6]
    """
    return [i*3 for i in range(n)]

def double_the_builder(n):
    if n == 0:
        return [1337]
    else:
        return builder(n)

if __name__ == '__main__':
    double_the_builder(2)




